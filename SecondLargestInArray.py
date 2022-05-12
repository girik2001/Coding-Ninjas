'''
Sample Input 1:
1
7
2 13 4 1 3 6 28
Sample Output 1:
13

Sample Input 2:
1
5
9 3 6 2 9
Sample Output 2:
6

Sample Input 3:
2
2
6 6
4
90 8 90 5
Sample Output 3:
-2147483648
8
'''

def secondLargestElement(arr, n):
    arr.sort()
    arr=list(set(arr))
    if len(arr)>1:
        return arr[-2]
    else:
        return -2147483648

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    print(secondLargestElement(a,n))