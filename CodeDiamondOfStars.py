'''
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *

Sample Input 2:
3
Sample Output 2:
 *
***
 *
'''

n=int(input())
half=n//2+1
for i in range(1,n+1):
    if i<=half:
        print(" "*(half-i),end="")
        print("*"*(2*i-1),end="")
    else:
        print(" "*(i-half),end="")
        print("*"*(2*(n-i)+1),end="")
    print()