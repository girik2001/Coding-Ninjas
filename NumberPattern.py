'''
Sample Input :
5
Sample Output :
12345
1234
123
12
1
'''

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()