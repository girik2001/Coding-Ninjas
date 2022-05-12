'''
Sample Input 1:
3
Sample Output 1:
  1 
 12
123

Sample Input 2:
4
Sample Output 2:
   1 
  12
 123
1234
'''

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(j+1,end="")
    print()