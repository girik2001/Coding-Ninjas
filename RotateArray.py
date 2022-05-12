'''
Sample Input 1:
1
7
1 2 3 4 5 6 7
2
Sample Output 1:
3 4 5 6 7 1 2

Sample Input 2:
2
7
1 2 3 4 5 6 7
0
4
1 2 3 4
2
Sample Output 2:
1 2 3 4 5 6 7
3 4 1 2
'''

def rotate(arr, n, d):
    if d==0 or n==1:
        return arr
    res=[0]*n
    for i in range(n):
        ri=(n+i-d)%n
        res[ri]=arr[i]
    return res
    
for i in range(int(input())):
    n=int(input())
    if n:
        a=list(map(int,input().strip().split()))[:n]
        d=int(input())
        print(*rotate(a,n,d))