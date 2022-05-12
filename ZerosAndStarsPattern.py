'''
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00

Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

n=int(input())
for i in range(n):
    print("0"*i,end="")
    print("*",end="")
    print("0"*(n-i-1),end="")
    print("*",end="")
    print("0"*(n-i-1),end="")
    print("*",end="")
    print("0"*i,end="")
    print()