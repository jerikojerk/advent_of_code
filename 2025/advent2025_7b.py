INI_FILE="2025/advent2025_7-ex.txt"
INI_FILE="2025/advent2025_7-input.txt"




def find_the_source(tr):
    print( f"****{tr}****"  )
    print (f"{len(tr)=}")
    for pos in range(0, len(tr)):
        if "S"==tr[pos]:
            return pos 
    raise ValueError("missing S mark")


#this is a total rewrite of the function as i'm not the happy owner of a supercomputer
def compute2(table):
    start = find_the_source(table[0])
    nb_col=len(table[0])
    nb_row=len(table)
    table[1][start]=1

    for r in range( 1, nb_row-1):
        next = r+1
        print (f"{r=}")
        for col in range(0, nb_col ):
            val = table[r][col]
            
            if isinstance(val,int): 
                tmp = table[next][col]
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



def print_screen2(table):
    for r in range( 0, len(table)):
        buf =""
        for c in range( 0, len( table[r])):
            tmp = table[r][c]
            if tmp == "^" or tmp == "S":
                buf = buf + tmp 
            elif tmp <10: 
                buf = buf + f"{tmp}"
            elif tmp < 100 :
                buf =buf +"a"
            elif tmp < 1000 :
                buf = buf +"b"
            elif tmp < 10000 :
                buf = buf + "c"
            elif tmp < 100000 :
                buf = buf + "d"
            elif tmp < 1000000 :
                buf = buf + "e"
            elif tmp < 10000000 :
                buf = buf + "f"
            elif tmp < 100000000 :
                buf = buf + "g"
            elif tmp < 1000000000 :
                buf = buf + "h"
            elif tmp < 10000000000 :
                buf = buf + "i"
            elif tmp < 100000000000 :
                buf = buf + "j"
            elif tmp < 1000000000000 :
                buf = buf + "k"
            else :
                buf = buf + "#"
        print(buf)
            


table2=[]
with open(INI_FILE, "r") as input:
    for line in input:
        line = line.strip()

        table2.append( [c if c != "." else 0 for c in line ])
        
    #for
#with
print_screen2(table2)
r= compute2( table2)
print_screen2(table2)
print( f"timelines = {r}")
