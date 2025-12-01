INI_FILE="2015\\advent2015_day5-input.txt"

def word_name( cond:bool ):
    if cond :
        return "nice"
    else:
        return "naughty"

def is_nice_word ( token:str):
    previous=""
    vowel_count=0
    vowel_def=["a","e","i","o","u"]
    ban_seq=["ab", "cd", "pq", "xy"]
    repeat_count=0

    for char in token:
        if char in vowel_def:
            vowel_count+=1

        if previous==char:
            repeat_count+=1
        elif previous+char in ban_seq:
            print(token, " => found banned ",previous+char)
            return False

        #before the end of the loop
        previous=char
    
    return vowel_count > 2 and repeat_count > 0


def is_nice_word2 ( token:str):
    length = len(token)
    pair_count=0
    rpt_count=0
    for pos in range(length):
        pos_np1=pos+1
        pos_np2=pos+2
        if pos_np2<length:
            needle=token[pos:pos_np2]
            if  token.find(needle,pos_np2) > 0 :
                pair_count+=1
            if token[pos_np2]==token[pos] :
                rpt_count+=1
        
        if pair_count>0 and rpt_count>0 :
            return True
    #end for
    return False
        
    
        
        


naughty_count=0
nice_count=0

with open(INI_FILE, "r") as words:  
    for word in words:
        if word.strip() == "":
            continue
        
        if is_nice_word2(word):
            nice_count+=1

        else:
            naughty_count+=1
    




print( "hello santa, naughty = ",naughty_count," , nice = ", nice_count )

