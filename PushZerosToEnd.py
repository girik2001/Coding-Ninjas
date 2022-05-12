'''
Sample Input 1:
1
7
2 0 0 1 3 0 0
Sample Output 1:
2 1 3 0 0 0 0

Explanation for the Sample Input 1 :
All the zeros have been pushed towards the end of the array/list. 
Another important fact is that the order of the non-zero elements have been maintained as they appear in the input array/list.

Sample Input 2:
2
5
0 3 0 2 0
5
9 0 0 8 2
Sample Output 2:
3 2 0 0 0
9 8 2 0 0 
'''

def pushZerosAtEnd(arr, n) :
    c=0
    for i in range(n):
        if arr[i]!=0:
            arr[c]=arr[i]
            c+=1
    while c<n:
        arr[c]=0
        c+=1

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    pushZerosAtEnd(a,n)
    print(*a)