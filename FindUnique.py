'''
Sample Input 1:
1
7
2 3 1 6 3 6 2
Sample Output 1:
1

Sample Input 2:
2
5
2 4 7 2 7
9
1 3 1 3 6 6 7 10 7
Sample Output 2:
4
10
'''

def findUnique(arr, n) :
    for i in range(n):
        if arr.count(arr[i])==1:
            return arr[i]

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    print(findUnique(a,n))