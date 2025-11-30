INI_FILE="advent2015_day8-input.txt"
total_mem=0
total_code=0
line_count=0
ghost_chars=0
from pprint import pprint


with open(INI_FILE, "r") as f:
    for line in f:
        string = line.strip()
        length_python=len(string)
        if length_python == 0:
            continue
        ghost_chars+=2
        line_count+=1
        length_code=0
        mode="r"
        length_mem=-2
        # mode name
        # r regular
        # e escape
        # h hexa  ()
        for char in string :
            length_code+=1
            if ( 'r' == mode ):
                if ( '\\' == char ):
                    ghost_chars+=1
                    mode='e'
                else:
                    length_mem+=1
            elif ( 'e' == mode ):
                if (  'x' == char  ):
                    mode='h1'
                elif ( char in '"\\' ):
                    length_mem+=1
                    mode='r'
            elif ( 'h1' == mode ):
                mode='h2'
                ghost_chars+=1
            elif ( 'h2' == mode ):
                length_mem+=1
                mode='r'
                ghost_chars+=1
            else:
                raise ValueError( f"missing a char {char=} {mode=}")
            #endif
            

        #endfor
        delta=length_code-length_mem
        print(f"{length_code=:>3} {length_mem=:>3} {delta=:>3} {length_python=:>3} {string}")
        total_mem+=length_mem
        total_code+=length_code
    #endfor
    
delta=total_code-total_mem
print(f"{total_code=:>3} {total_mem=:>3} {ghost_chars=:>3} {delta=:>3} ")        

