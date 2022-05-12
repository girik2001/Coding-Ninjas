'''
Sample Input 1:
1
6
9 3 6 12 4 32
Sample Output 1 :
3 9 12 6 32 4

Sample Input 2:
2
9
9 3 6 12 4 32 5 11 19
4
1 2 3 4
Sample Output 2 :
3 9 12 6 32 4 11 5 19 
2 1 4 3 
'''

def swapAlternate(arr, n) :
    for i in range(0,n-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    res=swapAlternate(a,n)
    print(*res)