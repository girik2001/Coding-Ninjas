'''
Sample Input :
5
Sample Output :
1
11
121
1221
12221
'''

n=int(input())
print(1)
for i in range(2,n+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end="")
        else:
            print(2,end="")
    print()