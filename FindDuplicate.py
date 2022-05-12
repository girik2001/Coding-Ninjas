'''
Sample Input 1:
1
9
0 7 2 5 4 7 1 3 6
Sample Output 1:
7

Sample Input 2:
2
5
0 2 1 3 1
7
0 3 1 5 4 3 2
Sample Output 2:
1
3
'''

def duplicateNumber(arr, n) :
    for i in arr:
        if arr.count(i)==2:
            return i

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    print(duplicateNumber(a,n))