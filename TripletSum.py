'''
Sample Input 1:
1
7
1 2 3 4 5 6 7 
12
Sample Output 1:
5

Sample Input 2:
2
7
1 2 3 4 5 6 7 
19
9
2 -5 8 -6 0 5 10 11 -3
10
Sample Output 2:
0
5
'''

def findTriplet(arr, n, x) :
    c=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==x:
                    c+=1
    return c

for i in range(int(input())):
    n=int(input())
    if n:
        a=list(map(int,input().strip().split()))
        x=int(input())
        print(findTriplet(a,n,x))
    else:
        print(0)