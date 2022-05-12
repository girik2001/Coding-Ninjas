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

def insertionSort(arr, n) :
    for i in range(1,n):
        j=i-1
        temp=arr[i]
        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    insertionSort(a,n)
    print(*a)