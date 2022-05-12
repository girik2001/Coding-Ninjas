'''
Sample Input 1:
1
9
1 3 6 2 5 4 3 2 4
7
Sample Output 1:
7

Sample Input 2:
2
9
1 3 6 2 5 4 3 2 4
12
6
2 8 10 5 -2 5
10
Sample Output 2:
0
2
'''

def pairSum(arr, n, x) :
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==x:
                count+=1
    return count
    
for i in range(int(input())):
    n=int(input())
    if n:
        a=list(map(int,input().strip().split()))[:n]
        x=int(input())
        print(pairSum(a,n,x))
    else:
        print(0)