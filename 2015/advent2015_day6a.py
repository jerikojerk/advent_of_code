INI_FILE="2015\\advent2015_day6-input.txt"

class LigthAction:
    def __init__ ( self, rule:str ):
        tab=rule.split(" ")
        token = tab.pop()
        self.end=self.read_coordonnate(token) 
        tab.pop() # retire le though
        token = tab.pop()
        self.start=self.read_coordonnate(token) 
        self.do=tab.pop() #on, off, toggle 
       

    def read_coordonnate(self, xy:str ):
        tab=xy.split(",")
        return int(tab[0]),int(tab[1])

    def get_cols(self):
        return range(self.start[1],self.end[1]+1)
    
    def get_rows(self):
        return range(self.start[0],self.end[0]+1)


    def apply(self,grid):
        if ("on"==self.do):
            return self._turn_on(grid)
        elif ("off"==self.do):
            return self._turn_off(grid)
        elif ("toggle"==self.do):
            return self._toggle(grid)
        else:
            raise ValueError("unexpected key word")

    def _turn_on(self,grid):
        cnt = 0
        for row in self.get_rows():
            for col in self.get_cols():
                if not (row,col) in grid:
                    grid[(row,col)]=1
                    cnt+=1
        return cnt
    
    def _turn_off(self,grid):
        cnt = 0
        for row in self.get_rows():
            for col in self.get_cols():
                if (row,col) in grid:
                    del grid[(row,col)]
                    cnt+=1
        return cnt 

    def _toggle( self,grid):
        cnt = 0
        for row in self.get_rows():
            for col in self.get_cols():
                if (row,col) in grid:
                    del grid[(row,col)]
                else:
                    grid[(row,col)]=1
                cnt+=1
        return cnt



grid ={}

with open(INI_FILE, "r") as instructions:   
    for instruction in instructions:
        la = LigthAction(instruction.strip())
        cnt = la.apply(grid)
        print(  instruction , " impacts ", cnt , "ligths" )

result=len(grid)
print( "hello santa,   = ",result," light are lit." )

