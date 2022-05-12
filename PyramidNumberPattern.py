'''
Sample Input :
5
Sample Output :
    1
   212
  32123
 4321234
543212345
'''

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for k in range(i,0,-1):
        print(k,end="")
    if i>1:
        for l in range(2,i+1):
            print(l,end="")
    print()