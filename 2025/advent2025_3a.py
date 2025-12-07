#untested code .
from math import ceil 
from math import log10 


import re 

INI_FILE="2025/advent2025_3-input.txt"

def solver( bank:str ):
    max=len(bank)
    if max<3:
        raise ValueError("batteries banks too small")
    #init sur  b[0] et b[1]
    di=bank[0]
    un=bank[1]
    pos=1
    max-=1
    while(pos<max):
        c=bank[pos]
        if c>di:
            #c'est le bordel
            di=c
            un=bank[pos+1]
        elif c>un:
            un=c
        #else nothing
        pos+=1
    #il faut traiter la derniere unité
    if bank[max]>un:
        un=bank[max]
    print(f"{di=}{un=}")
    return int(di+un)




with open(INI_FILE, "r") as input:
    total=0
    for line in input:
        jolts=solver(line.strip())
        total+=jolts
    print(f"somme des id du lutin: {total}")