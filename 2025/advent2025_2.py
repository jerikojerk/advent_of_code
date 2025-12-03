#untested code .
from math import ceil 
from math import log10 
import re 

INI_FILE="2025/advent2025_2-input.txt"

def range_analysis( range:str ):
   results=() 
   (bottom,top) = range.split("-",2)
   bo = int(bottom)
   to = int(top)
    if  bo > to :
        raise ValueError(f"Please verify  {range=} {bo=} > {to=}")
    
   (bleft,bright,bexp)=rangeBoundary_spliter(bottom,False)
   (tleft,tright,texp)=rangeBoundary_spliter(top,True)

    if bexp > texp :
        raise ValueError(f" exposant non conforme {bexp=} {texp=} {range=} ")
   continuez=True 
   iterator = bleft 
   end = tleft 
   pattern = re.compile(r"([0-9]+)\1") 
   
   while( continuez  ):        
        candidat = iterator*10**bexp + iterator 
        if  bo > iterator :
            continue 
        if  to < iterator : 
            continuez = False
        iterator+=1
        
        s = str(candidat)
        if pattern.fullmatch(s):
            results.append(s)
        else:
            print(f"coucou, last minute : erreur {s}"
    #endwhile    
    
   return results

def rangeBoundary_spliter( rangeBoundary:str, isUpper:bool ):
    length=len(rangeBoundary)
    firsthalf = lenght//2 
    if ( 2*firsthalf<lenght):
        if isUpper:
            secondhalf=firsthalf
            firsthalf=length-secondhalf
        else:
            secondhalf=length-firsthalf
    else
        secondhalf= firsthalf
    return ( int(rangeBoundary[:firsthalf]), int(rangeBoundary[-secondhalf:]),secondhalf)

with open(INI_FILE, "r") as input:
  for lines in input:
      my_ranges= lines.split(',')
      for my_range in my_ranges:
        range_analysis( my_range ) 
