'''
Sample Input 1 :
1
5
1 3 4 7 11
4
2 4 6 13
Sample Output 1 :
1 2 3 4 4 6 7 11 13 

Sample Input 2 :
2
3
10 100 500
7
4 7 9 25 30 300 450
4
7 45 89 90
0
Sample Output 2 :
4 7 9 10 25 30 100 300 450 500
7 45 89 90
'''

def merge(arr1, n, arr2, m) : 
    i=j=0
    res=[]
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while i<n:
        res.append(arr1[i])
        i+=1
    while j<m:
        res.append(arr2[j])
        j+=1
    return res

for i in range(int(input())):
    n1=int(input())
    if n1:
        a1=list(map(int,input().strip().split()))[:n1]
    n2=int(input())
    if n2:
        a2=list(map(int,input().strip().split()))[:n2]
    if n1 and n2:
        print(*merge(a1,n1,a2,n2))
    elif n1:
        print(*a1)
    elif n2:
        print(*a2)