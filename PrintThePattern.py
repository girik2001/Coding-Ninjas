'''
Sample Input :
4
Sample Output :
1  2  3  4
9 10 11 12
13 14 15 16
5  6  7  8
'''

n=int(input())
a=[[0 for x in range(n)]for y in range(n)]
c=1
if n%2!=0:
    half=n//2+1
else:
    half=n//2
ex=False
for x in range(half):
    for y in range(n):
        a[x][y]=c
        c+=1
        if c==n*n+1:
            ex=True
            break
    if ex:
        break
    k=n-x-1
    for y in range(n):
        a[k][y]=c
        c+=1
        if c==n*n+1:
            ex=True
            break
    if ex:
        break
for i in range(n):
    for j in range(n):
        print(a[i][j],end="  ")
    print()