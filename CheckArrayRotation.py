'''
Sample Input 1:
1
6
5 6 1 2 3 4
Sample Output 1:
2

Sample Input 2:
2
5
3 6 8 9 10
4
10 20 30 1
Sample Output 2:
0
3
'''

def arrayRotateCheck(arr, n):
    c=0
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return i+1
        else:
            c+=1
    if c==n-1:
        return 0

for i in range(int(input())):
    n=int(input())
    if n:
        a=list(map(int,input().strip().split()))[:n]
        print(arrayRotateCheck(a,n))
    else:
        print(0)