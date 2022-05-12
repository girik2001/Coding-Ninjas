'''
Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333
'''

n=int(input())
s=2*n-1
a=[[0 for x in range(s)] for y in range(s)]
start=0
end=s

while n!=0:
    for i in range(start,end):
        for j in range(start,end):
            if i==start or i==end-1 or j==start or j==end-1:
                a[i][j]=n
    start+=1
    end-=1
    n-=1
for i in range(s):
    for j in range(s):
        print(a[i][j],end="")
    print()