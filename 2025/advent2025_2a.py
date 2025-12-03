#untested code .
from math import ceil 
from math import log10 


import re 

INI_FILE="2025/advent2025_2-input.txt"
def is_odd(x): return x % 2 == 1

def rangeBoundary_spliter( rangeBoundary:str ):
    length=len(rangeBoundary)
    firsthalf = length//2 
    if firsthalf == 0:
        print(f"strange boundary {rangeBoundary}")
        return ( "1",rangeBoundary,1)
    secondhalf=length-firsthalf
    return ( rangeBoundary[:firsthalf], 
        rangeBoundary[-secondhalf:],secondhalf)

def range_analysis( range:str ):
    pattern = re.compile(r"^([0-9]+)\1$") 
    results=[]
    (bottom,top) = range.split("-",2)
    bo = int(bottom)
    to = int(top)
    if  bo > to :
        raise ValueError(f"Please verify  {range=} {bo=} > {to=}")
    
    (bleft,bright,bexp)=rangeBoundary_spliter(bottom)
    #(tleft,tright,texp)=rangeBoundary_spliter(top)
    iterator = int(bleft)
    exposant = bexp 
    max_exp = 10**exposant
    min_exp = 10**(exposant-1)
    print(f"iterator initialisation {min_exp=} {max_exp} {iterator}")
    while( True  ):
        candidat = iterator*10**exposant + iterator 
        #print(f"{candidat=}")
        if  to < candidat : 
            break
       
        if bo <= candidat:
            s = str(candidat)
            if pattern.findall(s):
                #print(f"success {candidat=} ")
                results.append(candidat)
            else:
                print(f"last minute : erreur {s}")
        #else candidat trop petit 

        iterator+=1
        """
        if   iterator >= max_exp or iterator < min_exp :
            print(f"{candidat=}")
            tmp = f"{min_exp=} {max_exp=} {iterator=}"
            #there is a rule for no leading 0 
            iterator=10**(exposant)
            min_exp=max_exp
            exposant+=1
            max_exp = 10**exposant
            print(f"iterator adjustment {tmp} => {min_exp=} {max_exp=} {iterator=}")
        """
    #endwhile    
    return results



with open(INI_FILE, "r") as input:
    for lines in input:
        my_ranges= lines.split(',')
        accumul = []
        for my_range in my_ranges:
            print(f"**** {my_range} ****")
            results = range_analysis( my_range ) 
            print("ID :",results)
            tmp = sum( results )
            accumul.append( tmp )
    tmp = sum(accumul)
    print(f"somme des id du lutin: {tmp}")