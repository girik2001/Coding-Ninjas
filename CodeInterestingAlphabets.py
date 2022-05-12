'''
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH

Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''

n=int(input())
for i in range(1,n+1):
    ch=ord('A')+n-i
    for j in range(i):
        print(chr(ch+j),end="")
    print()