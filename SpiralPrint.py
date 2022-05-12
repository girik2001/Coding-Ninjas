'''
Sample Input 1:
1
4 4 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16
Sample Output 1:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

Sample Input 2:
2
3 3 
1 2 3 
4 5 6 
7 8 9
3 1
10
20
30
Sample Output 2:
1 2 3 6 9 8 7 4 5 
10 20 30
'''

def spiralPrint(mat, nRows, mCols):
    if not mat or not len(mat):
        return
    top=left=0
    bottom=len(mat)-1
    right=len(mat[0])-1
    while True:
        if left> right:
            break
        for i in range(left,right+1):
            print(mat[top][i],end=" ")
        top=top+1
        if top>bottom:
            break
        for i in range(top,bottom+1):
            print(mat[i][right],end=" ")
        right=right-1
        if left>right:
            break
        for i in range(right,left-1,-1):
            print(mat[bottom][i],end=" ")
        bottom=bottom-1
        if top>bottom:
            break
        for i in range(bottom,top-1,-1):
            print(mat[i][left],end=" ")
        left=left+1
    
for i in range(int(input())):
    r,c=map(int,input().split())
    a=[]
    for i in range(r):
        ai=list(map(int,input().split()))
        a.append(ai)
    spiralPrint(a,r,c)
    print()