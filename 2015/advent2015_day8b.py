INI_FILE="advent2015_day8-input.txt"
total_encoded=0
total_code=0
from pprint import pprint


with open(INI_FILE, "r") as f:
    for line in f:
        string = line.strip()
        length_python=len(string)
        if length_python == 0:
            continue
        #encoded=[]
        length_encoded=2
        length_code=0
        for char in string :
            length_code+=1
            if ( char in '\\"'  ):
                #encoded.append('\\\\')
                length_encoded+=2
            else:
                length_encoded+=1
                    
            #endif
        #endfor
            

        #endfor
        delta=length_encoded-length_python
        print(f"{length_python=:<3} {length_encoded=:<3}  {length_code=:<3} {delta=:<3}  {string}")
        total_encoded+=length_encoded
        total_code+=length_python
        
    #endfor
    
delta=total_encoded-total_code
print(f"{total_code=:>3} {total_encoded=:>3} {delta=:>3} ")        

