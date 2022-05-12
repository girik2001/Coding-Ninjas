'''
Sample Input 1:
1
3 4 
1  2  3  4 
5  6  7  8 
9 10 11 12
Sample Output 1:
1 5 9 10 6 2 3 7 11 12 8 4

Sample Input 2:
2
5 3 
1 2 3 
4 5 6 
7 8 9 
10 11 12 
13 14 15
3 3
10 20 30 
40 50 60
70 80 90
Sample Output 2:
1 4 7 10 13 14 11 8 5 2 3 6 9 12 15 
10 40 70 80 50 20 30 60 90 
'''

def wavePrint(li,r,c):
    for j in range(c):
        if j%2==0:
            for i in range(r):
                print(li[i][j],end=" ")
        else:
            for i in range(r-1,-1,-1):
                print(li[i][j],end=" ")
            
    
for i in range(int(input())):
    r,c=map(int,input().split())
    a=[]
    for j in range(r):
        ai=list(map(int,input().split()))
        a.append(ai)
    wavePrint(a,r,c)
    print()