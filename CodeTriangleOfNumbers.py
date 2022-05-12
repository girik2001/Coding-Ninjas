'''
Sample Input 1:
5
Sample Output 1:
    1
   232
  34543
 4567654
567898765

Sample Input 2:
4
Sample Output 2:
   1
  232
 34543
4567654
'''

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,(2*i)):
        print(j,end="")
    for k in range((2*i)-2,i-1,-1):
        print(k,end="")
    print()