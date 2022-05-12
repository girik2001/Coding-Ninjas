'''
Sample Input 1 :
4
Sample Output 1 :
1234
 234
  34
   4
  34
 234
1234
'''

n=int(input())
for i in range(1,2*n):
    if i<=n:
        print(" "*(i-1),end="")
        for j in range(i,n+1):
            print(j,end="")
        print()
    else:
        print(" "*(2*n-i-1),end="")
        for j in range(2*n-i,n+1):
            print(j,end="")
        print()