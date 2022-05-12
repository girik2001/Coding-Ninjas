'''
Sample Input 1:
7
Sample Output 1:
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

Sample Input 2:
6
Sample Output 2:
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''

n=int(input())
for i in range(1,n+1):
    print(chr(ord('A')+i-1)*i)