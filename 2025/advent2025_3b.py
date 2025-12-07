#untested code .


import re 

INI_FILE="2025/advent2025_3-input.txt"


def subsolver( select:list, size:int, optimize):
    n = optimize
    m = optimize+1
    while ( m < size ):
        if select[n]<select[m]:
            return n
        n=m
        m+=1
    return -1


def solver( bank:str ,size:int, correction:int ):
    maximum=len(bank)
    if maximum<size:
        raise ValueError("batteries banks too small")
    #init sur  b[0] et b[1]
    select=list(bank[:size])
    pos=size
    jump_boundary= maximum-size 
    optimized=0
    var_size=size 
    while(pos<maximum):
        c=bank[pos]
        if c>select[0] and pos < jump_boundary :
            #let jump
            before = int("".join(select)) 
            select=list(bank[pos:pos+size])
            after = int("".join(select))
            print( f"{pos=} {select=} {before=} {after=}")
            if before>after:
                raise RuntimeError(f" Erreur {before=} {after=} ")
            if c!=select[0]:
                raise RuntimeError('inproper copy')
            optimized=0
        else:
            tmp=subsolver(select,size,optimized)
            if -1 == tmp :
                #pas d'optimisation de la selection
                optimized=0
                if c > select[-1] : 
                    select[-1]=c 
                    #otimized=size-1
                else:
                    #optimized=size
                    optimized=0
                    
                #sinon on fait rien
            else:
                #optimized=max(tmp-1,0)
                optimized=0
                del select[tmp]
                select.append(c)

        #else nothing
        pos+=1
    #il faut traiter la queue de comet
    tmp= int("".join(select))
    if tmp != correction:
        print(f"{bank=}")
        print(f"{tmp=}")
        print(f"{correction=}")
    return tmp

def solver_correct( bank:str ,size:int):
    maximum=len(bank)
    if maximum<size:
        raise ValueError("batteries banks too small")
    #init sur  b[0] et b[1]
    select=list(bank[:size])
    pos=size
    jump_boundary= maximum-size 
    optimized=0
    var_size=size 
    while(pos<maximum):
        c=bank[pos]
        tmp=subsolver(select,size,optimized)
        if -1 == tmp :
            #pas d'optimisation de la selection
            optimized=0
            if c > select[-1] : 
                select[-1]=c 
                #otimized=size-1
            else:
                #optimized=size
                optimized=0
                
            #sinon on fait rien
        else:
            #optimized=max(tmp-1,0)
            optimized=0
            del select[tmp]
            select.append(c)

        #else nothing
        pos+=1
    #il faut traiter la queue de comet
    return int("".join(select))



with open(INI_FILE, "r") as input:
    total=0
    for line in input:
        jolts1=solver_correct(line.strip(),12)
        jolts2=solver( line.strip(),12, jolts1 )
        print("")
        total+=jolts2
    print(f"somme des id du lutin: {total}")