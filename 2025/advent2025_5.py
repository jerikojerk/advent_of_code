from __future__ import annotations



INI_FILE="2025/advent2025_5-ex.txt"
INI_FILE="2025/advent2025_5-input.txt"




class IntervalNode: 
    def __init__(self, start:int, end:int ):
        self.start = start 
        self.end = end 
        self.right= None 
        self.left = None 
        self.end_max = end
        self.height = 0

    def insert( self, node:IntervalNode ):
        if node.start < self.start :
            #aller à gauche
            if node.start <= self.start and self.start <= node.end :
                print(f"fusion de node à gauche ! ")
                self.start = node.start 
                self.end = max(node.end,self.end)
            elif self.left is None :
                self.left = node 
                #self.left.height = self.height+1
            else:
                self.left.insert(node)
        else: 
            #aller à droite.
            #fusion de node
            if  self.start <= node.start and node.start <= self.end :
                print(f"fusion de node à droite ! ")
                self.end = max(node.end,self.end)
            elif self.right is None:
                self.right = node 
                #self.right.height = self.height+1
            else: 
                self.right.insert(node)
        self.end_max=max( self.end_max, node.end_max)
        
    def search( self, value ):
        if self.start <= value and value <= self.end:
            return True
        if value > self.end_max:
            return False
        if self.left is not None and value <= self.left.end_max:
            return self.left.search(value)
        if self.right is not None:
            return self.right.search(value)
        return False 

    def convert_to_list(self):
        #descendre dans l'arbre pour aller chercher le noeud le plus à gauche (rercussion)
        result = []
        self._convert_subtree_to_list( result )
        return result
            
    def _convert_subtree_to_list(self, result ):
        #les cas ou on fait rien 
        if self.left is not None :
            self.left._convert_subtree_to_list( result )
        result.append(self)
        if self.right is not None :
            self.right._convert_subtree_to_list( result )
    
    def get_intervalsize(self):
        return self.end+1 - self.start

    #methode rédigée par chatgtp
    def count_integers(self, hwm=-1):
        """
        Compte le nombre d'entiers représentés par l'arbre,
        en évitant les doublons si les intervalles se chevauchent.
        hwm: high water mark, la plus grande valeur déjà comptée
        """
        total = 0

        # 1. gauche
        if self.left is not None:
            left_count, hwm = self.left.count_integers(hwm)
            total += left_count

        # 2. courant
        start, end = self.start, self.end
        if end < hwm:
            add = 0  # intervalle déjà compté
        elif start >= hwm:
            add = end - start + 1
            hwm = end + 1
        else:  # start < hwm <= end
            add = end - hwm + 1
            hwm = end + 1
        total += add

        # 3. droite
        if self.right is not None:
            right_count, hwm = self.right.count_integers(hwm)
            total += right_count

        return total, hwm


def solve_part2( root: IntervalNode ):
    table = root.convert_to_list()

    if len(table)<1 :
        raise RuntimeError("attention pas assez d'éelement dans la table ")
    result = table[0].get_intervalsize()
    hwm = table[0].end+1
    
    for node in table :
        if hwm <= node.start :
            add = node.get_intervalsize()
            hwm = node.end+1 
            result += add 
        elif node.start <= hwm and hwm < node.end :
            add = node.end+1 -hwm 
            hwm = node.end+1 
            result += add 
    
    print (f"solution humain  {result}")




def read_freshRange(line:str):
    tab=line.split("-")
    return  IntervalNode( int(tab[0]), int(tab[1]))


reading_ranges=True
root = None
fresh_count = 0 
with open(INI_FILE, "r") as input:
    for line in input:
        line = line.strip()
        if reading_ranges :
            if  "" == line :
                reading_ranges=False 
                continue
            if isinstance(root,IntervalNode ) :
                #print(f"inserting {line=}")
                root.insert( read_freshRange(line ))
            else:
                root = read_freshRange( line )
        else :
            if  "" == line :
                continue
            needle = int(line)
            #print(f"{needle=}")
            if root.search( needle ) : 
                #print(f"found {needle=}")
                fresh_count += 1
        #if
    #for
#with

print (f"fresh count {fresh_count=}")

solve_part2( root )     

total_count, _ = root.count_integers()


print (f"solution machine {total_count}")

        





