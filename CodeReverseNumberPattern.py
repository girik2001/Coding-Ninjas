'''
Sample Input 1:
5
Sample Output 1:
1
21
321
4321
54321

Sample Input 2:
6
Sample Output 2:
1
21
321
4321
54321
654321
'''

n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()