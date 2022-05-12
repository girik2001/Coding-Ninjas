'''
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
1 2 3 4 6 13 28

Sample Input 2:
2
5
9 3 6 2 0
4
4 3 2 1
Sample Output 2:
0 2 3 6 9
1 2 3 4
'''

def bubbleSort(arr, n) :
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    bubbleSort(a,n)
    print(*a)