INI_FILE="2025/advent2025_7-ex.txt"
INI_FILE="2025/advent2025_7-input.txt"




def find_the_source(tr):
    print( f"****{tr}****"  )
    print (f"{len(tr)=}")
    for pos in range(0, len(tr)):
        if "S"==tr[pos]:
            return pos 
    raise ValueError("missing S mark")

def compute1(table):
    start = find_the_source(table[0])
    nb_col=len(table[0])
    nb_row=len(table)
    rays=[(0,start)]
    splits = 0
    while( len(rays) > 0 ):
        (row,col) = rays.pop(0)
        for r in range( row, nb_row):
            tmp = table[r][col]
            if tmp == ".":
                table[r][col]="|"
            elif tmp == "|":
                break
            elif tmp == "^":
                splits+=1
                buf=col-1
                if buf >= 0:
                    rays.append((r,buf))
                buf=col+1
                if buf < nb_col:
                    rays.append((r,buf) )
                break
        #for
        
        print(f"{splits=}")
        #print_screen( table )
    #while
    return splits


def compute2(table):
    start = find_the_source(table[0])
    nb_col=len(table[0])
    nb_row=len(table)
    table[1][start]=1

    for r in range( 1, nb_row-1):
        next = r+1
        print (f"{r=}")
        for c in range(0, nb_col ):
            val = table[r][c]
            
            if isinstance(val,int): 
                tmp = table[next][c]
                if isinstance(tmp,int):
                    table[next][col]=val+table[next][col]
                elif tmp == "^":
                    buf=col-1
                    if buf >= 0:
                        table[next][buf]=val+table[next][buf]
                    buf=col+1
                    if buf < nb_col:
                        table[next][buf]=val+table[next][buf]
        print( table[next])
            
        #pour toutes les colonnes
    #for  toutes les lines (sauf la 1er et la derniere)
    #lets use a trick
    timeline=sum(table[next])
    #while
    return timeline

def print_screen(table  ):
    for r in range( 0, len(table)):
        print("".join(table[r]))


            

table1=[]

with open(INI_FILE, "r") as input:
    for line in input:
        line = line.strip()
        table1.append( list(line))
        
    #for
#with
r= compute1( table1 )
print( f"splits = {r}")