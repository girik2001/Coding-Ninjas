'''
Sample Input 1 :
2
6
2 6 8 5 4 3
4
2 3 4 7 
2
10 10
1
10
Sample Output 1 :
2 4 3
10

Sample Input 2 :
1
4
2 6 1 2
5
1 2 3 4 2
Sample Output 2 :
2 1 2
Explanation for Sample Output 2 :
Since, both input arrays have two '2's, the intersection of the arrays also have two '2's. 
The first '2' of first array matches with the first '2' of the second array. 
Similarly, the second '2' of the first array matches with the second '2' if the second array.
'''

def intersections(arr1, n, arr2, m) :
    count=False
    for i in arr1:
        if i in arr2:
            print(i,end=" ")
            arr2.remove(i)
    print()
    
for i in range(int(input())):
    n1=int(input())
    if n1:
        a1=list(map(int,input().strip().split()))[:n1]
    n2=int(input())
    if n2:
        a2=list(map(int,input().strip().split()))[:n2]
    if n1 and n2:
        intersections(a1,n1,a2,n2)