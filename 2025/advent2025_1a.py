from debug import debug_open 
from math import ceil

print
INI_FILE="2025/advent2025_1-input.txt"

debug_open( INI_FILE)
INI_DIAL_POSITION=100
sign = 1
position =50
pos_prev=position
rotation=0
instruction_counter=0
password1=0
password2=0
print(f"begin: {instruction_counter=}, {position=}, and {password1=} or {password2=}")
with open(INI_FILE, "r") as f:
    for line in f:
        string = line.strip()
        if 'R' == string[0]:
            sign =1
        elif 'L' == string[0]:
            sign=-1
        else:
            print(f"warning {string}")
            continue
    
        instruction_counter+=1
        rotation=int(string[1:])
        
        if  rotation > INI_DIAL_POSITION :
            print("multiple tours")
        gain=rotation//INI_DIAL_POSITION
        rotation=rotation%INI_DIAL_POSITION
        
        pos_prev = position
        pos_raw = (pos_prev + (sign*rotation))
        position = pos_raw %INI_DIAL_POSITION
        
        if ( 0 == position):
            password1+=1

        if sign > 0:
            had_zero = gain+(pos_raw//INI_DIAL_POSITION)
        else:
            had_zero = (1 if 0 == position  or ( position > pos_prev and pos_prev != 0 ) else 0)+ gain 
        
        password2+=had_zero

        
        print(f"instruction: {instruction_counter=}, {string=} {position=}  {had_zero=}")

print(f"final: {instruction_counter=}, {position=}, and {password1=} or {password2=}")
