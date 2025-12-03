#untested code .
from math import ceil 
from math import log10 


import re 

INI_FILE="2025/advent2025_2-ex.txt"



def range_analysis( range:str ):
    pattern = re.compile(r"^([0-9]+)\1+$") 
    results=[]
    (bottom,top) = range.split("-",2)
    bot = int(bottom)
    top = int(top)
    if  bot > top :
        raise ValueError(f"Please verify  {range=} {bo=} > {to=}")
    candidat = bot
    print(f"iterator initialisation {candidat=}")
    while( top > candidat  ):
        s = str(candidat)
        if pattern.findall(s):
            results.append(candidat)
        candidat+=1
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