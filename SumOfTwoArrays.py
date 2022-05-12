'''
Sample Input 1:
1
3
6 2 4
3
7 5 6
Sample Output 1:
1 3 8 0

Sample Input 2:
2
3
8 5 2
2
1 3
4
9 7 6 1
3
4 5 9
Sample Output 2:
0 8 6 5
1 0 2 2 0 
'''

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    p1=0
    for i in range(n):
        p1=p1*10+arr1[i]
    p2=0
    for j in range(m):
        p2=p2*10+arr2[j]
    p=p1+p2
    for i in range(len(output)-1,-1,-1):
        output[i]=p%10
        p//=10

for i in range(int(input())):
    n1=int(input())
    if n1:
        a1=list(map(int,input().strip().split()))[:n1]
    n2=int(input())
    if n2:
        a2=list(map(int,input().strip().split()))[:n2]
    if n1 and n2:
        output = [0] *(max(n1,n2)+1)
        sumOfTwoArrays(a1,n1,a2,n2,output)
        print(*output)
    elif n1:
        print("0",*a1)
    elif n2:
        print("0",*a2)
    else:
        print(0)