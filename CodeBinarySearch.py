'''
Sample Input 1:
7
1 3 7 9 11 12 45
1
3
Sample Output 1:
1

Sample Input 2:
7
1 2 3 4 5 6 7
2
9
7
Sample Output 2:
-1
6
'''

def binarySearch(arr, n, x) :
    lower_bound=0
    upper_bound=n-1
    while lower_bound <= upper_bound:
        middle = (lower_bound+upper_bound)//2
        if x == arr[middle]:
            return middle
        elif x < arr[middle]:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return -1

n=int(input())
if n:
    a=list(map(int,input().strip().split()))[:n]
    for i in range(int(input())):
        print(binarySearch(a,n,int(input())))
else:
    print(-1)