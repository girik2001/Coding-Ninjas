'''
Sample Input :
11
Sample Output :
*
 * *
  * * *
   * * * *
    * * * * *
     * * * * * *
    * * * * *
   * * * *
  * * *
 * *
*
'''

n=int(input())
half=n//2+1
for i in range(1,n+1):
    if i<=half:
        print(" "*(i-1),end="")
        print("* "*i,end="")
    else:
        print(" "*(n-i),end="")
        print("* "*(n-i+1),end="")
    print()