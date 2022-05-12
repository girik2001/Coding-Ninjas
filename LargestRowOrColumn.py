'''
Sample Input 1 :
1
2 2 
1 1 
1 1
Sample Output 1 :
row 0 2

Sample Input 2 :
2
3 3
3 6 9 
1 4 7 
2 8 9
4 2
1 2
90 100
3 40
-10 200
Sample Output 2 :
column 2 25
column 1 342
'''

def largestRow(li,r,c):
    if r==0 and c==0:
        return 0,-2147483648
    mindex=0
    msum=0
    for i in range(r):
        s=0
        for j in range(c):
            s+=li[i][j]
        if s>msum:
            mindex=i
            msum=s
    return mindex,msum

def largestCol(li,r,c):
    if r==0 and c==0:
        return 0,-2147483648
    mindex=0
    msum=0
    for i in range(c):
        s=0
        for j in range(r):
            s+=li[j][i]
        if s>msum:
            mindex=i
            msum=s
    return mindex,msum
    

for i in range(int(input())):
    r,c=map(int,input().split())
    a=[]
    for i in range(r):
        ai=list(map(int,input().split()))
        a.append(ai)
    rindex,rsum=largestRow(a,r,c)
    cindex,csum=largestCol(a,r,c)
    if rsum>=csum:
        print("row",rindex,rsum)
    else:
        print("column",cindex,csum)