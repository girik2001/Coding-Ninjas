'''
Sample Input 1:
5
Sample Output 1:
A
BC
CDE
DEFG
EFGHI

Sample Input 2:
6
Sample Output 2:
A
BC
CDE
DEFG
EFGHI
FGHIJK
'''

n=int(input())
for i in range(1,n+1):
    ch=ord('A')+i-1
    for j in range(i):
        print(chr(ch+j),end="")
    print()