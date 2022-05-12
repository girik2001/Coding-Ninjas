'''
Sample Input 1 :
3
Sample Output 1 :
  *
 *** 
*****

Sample Input 2 :
4
Sample Output 2 :
   *
  *** 
 *****
*******
'''

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*((2*i)-1))