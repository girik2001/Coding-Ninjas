'''
Sample Input 1:
3 3
1 2 3
4 5 6
7 8 9
Sample Output 1 :
1 2 3
1 2 3
1 2 3
4 5 6
4 5 6
7 8 9
'''

n,m=map(int,input().split())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))[:m]
    mat.append(a)
for i in range(n):
    for j in range(n-i):
        for k in mat[i]:
            print(k,end=" ")
        print()