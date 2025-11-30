#day 4


import hashlib

secretkey = "iwrupvqb"
expectedPrefix = "000000"
it=0

while (True):
    tmp=secretkey+str(it)
    tentative=hashlib.md5(tmp.encode()).hexdigest()

    if  tentative[:6] == expectedPrefix :
        break

    it+=1

print( "Santa, here is the answer ",it," md5=", tentative ," ." )