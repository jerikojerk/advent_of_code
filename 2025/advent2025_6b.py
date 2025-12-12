
from  math import prod 

INI_FILE="2025/advent2025_6-ex.txt"
INI_FILE="2025/advent2025_6-input.txt"



def compute2(table:list):
    result = []
    row_count = len(table)-1
    opera_pos = len(table)-1
    column_ct = len(table[0])
    #print(f"{row_count=} {opera_pos=} {column_ct=}")
    need_operator = True 
    answer = []
    for pos in range(0,column_ct):
        tmp = ""
        for row in range( 0, row_count ):
            tmp = tmp+table[row][pos]
        
        if need_operator : 
            operator = table[opera_pos][pos]
            need_operator = False
        #print(f"{tmp=} {operator}")

        if tmp.isspace():
            if "*" == operator:
                tmp = prod( answer )
            elif "+" == operator:
                tmp = sum(answer)
            print(f"local result {tmp}")
            result.append(tmp)
            need_operator = True 
            answer=[]
        else: 
            answer.append(int(tmp))
    return result




table=[]
with open(INI_FILE, "r") as input:
    for line in input:
        table.append( line )
    #for
#with
r = compute2( table )
final = sum( r )
print(f"{final=}")