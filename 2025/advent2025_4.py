from math import ceil 
from math import log10 


import re 

INI_FILE="2025/advent2025_4-ex.txt"
INI_FILE="2025/advent2025_4-input.txt"

def evaluate(char:str):
    return 1 if char=='@' else 0 


def map_line( row:str ):
    #print(row)
    direct=[0]
    max=len(row)
    if max<1:
        raise ValueError("input  too small")
    #init sur  b[0] et b[1]
    pos=0
    while(pos<max):
        direct.append(evaluate(row[pos]))
        pos += 1 
    #while
    direct.append(0)
    return direct

def evaluate_removal( row:int , col:int, pending:list , stack:list):
    if stack[row][col]>0 :
        tmp = sum( stack[row-1][col-1:col+2] ) + sum( stack[row+1][col-1:col+2] ) + stack[row][col-1] + stack[row][col+1]
        #print(f"{row}:{col} {stack[row-1][col-1:col+2]} {stack[row][col-1] } {stack[row][col+1]} {stack[row+1][col-1:col+2]} {tmp=}" )
        if tmp < 4 :
            pending.append((row,col))

def print_stack(stack:list, recalculate:list ):
    print("*** status stack **** ")
    for row in range( 0, len(stack)):
        tmp = ""
        for col in range( 0, len(stack[row])):
            t=(row,col)
            if  stack[row][col]:
                if t in recalculate :
                    tmp = tmp + "?"
                else :
                    tmp = tmp + "@"
            else:
                if t in recalculate:
                    tmp += ":"
                else:
                    tmp = tmp + "."
        print(tmp)


def send_to_recalculate ( row, col, recalculate:list, stack:list ):
    cols = range(max(col-1,0), 1+min(col+1,len(stack[0])) )
    rows = range(max(row-1,0), 1+min(row+1,len(stack)) )
    #it=0
    for r in rows :
        for c in cols:
            #it+=1
            if stack[r][c]:
                recalculate.append(( r, c ))
    #if it != 8:
    #    print(f"{row=} {col=} / {cols=} {rows=}")
    

#now for part 2
recalculate=[]
stack=[]
pending_removal=[]
max_row =0
max_col = 0
do_init = True 
with open(INI_FILE, "r") as input:
    for line in input:
        row = line.strip()
        if do_init : 
            size = len(row)+2
            do_init = False
            stack.append([0]*size)
        tab=map_line( row )
        stack.append(tab)
    stack.append([0]*size)
print("ended reading the file")
#with file 
max_row=len(stack)-1 
max_col = size-1
for row in range(1,max_row):
    for col in range( 1, max_col):
        evaluate_removal( row, col, pending_removal, stack)
    #for
#for
print( f"found {len(pending_removal)} item removable at first pass ")


removed = 0
while( len(pending_removal) ):
    #print(f"=> pending = {len(pending_removal)}" )
    #print_stack(stack)
    while len(pending_removal)>0 :
        (row,col)=pending_removal.pop()
        if stack [row][col]:
            stack[row][col]=0
            removed+=1
            #print(f"neighboor {row=} {col=}")
            send_to_recalculate( row, col, recalculate, stack )
        else:
            print(f"pruned removal of removed {stack[row][col]}")
    #end while
    #suppression de doublons
    #print_stack(stack,recalculate)
    recalculate=list(set(recalculate))
    #verification de tout ce qu'on peut à nouveau supprimer
    #print(f"=> recalculate = {len(recalculate)}" )
    while len(recalculate)>0:
        (row,col)=recalculate.pop()
        #print(f" eval removal {row=} {col=}")
        evaluate_removal( row, col, pending_removal, stack)
    


print( f"nombre de roulaux : {removed}")
