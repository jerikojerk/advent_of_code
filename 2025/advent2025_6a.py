


INI_FILE="2025/advent2025_6-ex.txt"
INI_FILE="2025/advent2025_6-input.txt"

def compute(table:list):
    result = []
    row_count = len(table)-1
    opera_pos = len(table)-1
    for pos in range(0,len(table[opera_pos])):
        operator = table[opera_pos][pos]
        if "*" == operator:
            answer=1
            operate = lambda a,b: a*b 
        elif "+" == operator:
            answer=0
            operate = lambda a,b:a+b
        else:
            raise ValueError(f"Operator not recognized    {operator=}")
        for row in range( 0, row_count ):
            tmp= int(table[row][pos])
            print(f"operate {operator=} {answer=} {tmp=} at {row}:{pos}")  
            
            answer = operate( answer, tmp )
        
        
        result.append(answer)
    
    return result




table=[]
with open(INI_FILE, "r") as input:
    for line in input:
        line = line.strip()
        tab = line.split()
        table.append( tab )
    #for
#with
r = compute( table )
final = sum( r )
print(f"{final=}")