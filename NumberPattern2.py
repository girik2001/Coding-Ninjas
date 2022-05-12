'''
Sample Input :
5
Sample Output :
1
11
202
3003
40004
'''

n=int(input())
print(1)
for i in range(2,n+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(i-1,end="")
        else:
            print("0",end="")
    print()