'''
Sample Input 1 :
5
Sample Output 1 :
true

Sample Input 2 :
14
Sample Output 2 :
false    
'''

def checkMember(n):
    a,b=0,1
    c=a+b
    while c<=n:
        c=a+b
        a=b
        b=c
        if c==n:
            return True
    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")