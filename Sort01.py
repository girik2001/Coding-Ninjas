'''
Sample Input 1:
1
7
0 1 1 0 1 0 1
Sample Output 1:
0 0 0 1 1 1 1

Sample Input 2:
2
8
1 0 1 1 0 1 0 1
5
0 1 0 1 0
Sample Output 2:
0 0 0 1 1 1 1 1
0 0 0 1 1 
'''

def sortZeroesAndOne(arr, n) :
    zero=arr.count(0)
    one=arr.count(1)
    arr.clear()
    for i in range(zero):
        arr.append(0)
    for j in range(one):
        arr.append(1)
    return arr
        
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))[:n]
    print(*sortZeroesAndOne(a,n))