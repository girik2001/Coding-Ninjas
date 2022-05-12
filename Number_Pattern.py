'''
Sample Input 1 :
4
Sample Output 1 :
1      1
12    21
123  321
12344321
'''

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print(" "*(2*(n-i)),end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()