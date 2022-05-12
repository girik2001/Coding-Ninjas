'''
Sample Input 1:
1
7
0 1 2 0 2 0 1
Sample Output 1:
0 0 0 1 1 2 2
 
Sample Input 2:
2
5
2 2 0 1 1
7
0 1 2 0 1 2 0
Sample Output 2:
0 1 1 2 2 
0 0 0 1 1 2 2
'''

def sort012(arr, n) :
    z=arr.count(0)
    o=arr.count(1)
    t=arr.count(2)
    arr.clear()
    arr.extend([0]*z)
    arr.extend([1]*o)
    arr.extend([2]*t)

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    sort012(a,n)
    print(*a)