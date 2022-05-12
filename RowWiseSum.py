'''
Sample Input 1:
1
4 2 
1 2 
3 4 
5 6 
7 8
Sample Output 1:
3 7 11 15 

Sample Input 2:
2
2 5 
4 5 3 2 6 
7 5 3 8 9
4 4
1 2 3 4
9 8 7 6
3 4 5 6
-1 1 -10 5
Sample Output 2:
20 32 
10 30 18 -5 
'''

def rowWiseSum(mat, nRows, mCols):
    for i in range(nRows):
        s=0
        for j in range(mCols):
            s+=mat[i][j]
        print(s,end=" ")

for i in range(int(input())):
    r,c=map(int,input().strip().split())
    a=[]
    for j in range(r):
        ai=list(map(int,input().strip().split()))[:c]
        a.append(ai)
    rowWiseSum(a,r,c)
    print()