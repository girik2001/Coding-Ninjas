'''
Sample Input 1:
abdefgbabfba
Sample Output 1:
b

Sample Input 2:
xy
Sample Output 2:
x
'''

ASCII_SIZE=256
def highestOccuringChar(string) :
    count=[0]*ASCII_SIZE
    max=-1
    c=" "
    for i in string:
        count[ord(i)]=count[ord(i)]+1
    for i in string:
        if max<count[ord(i)]:
            max=count[ord(i)]
            c=i
    return c

s=input().strip()
print(highestOccuringChar(s))