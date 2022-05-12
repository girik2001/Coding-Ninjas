'''
Sample Input 1 :
1
Sample Output 1 :
true

Sample Input 2 :
103
Sample Output 2 :
false
'''

def arm(n):
    c=len(str(n))
    if c==1:
        return True
    temp=n
    res=0
    while temp!=0:
        last=temp%10
        res=res+last**c
        temp=temp//10
    if res==n:
        return True
    else:
        return False

n=int(input())
if arm(n):
    print("true")
else:
    print("false")