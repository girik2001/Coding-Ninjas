'''
Sample Input 1:
5
Sample Output 1:
55555 
4444
333
22
1

Sample Input 2:
6
Sample Output 2:
666666
55555 
4444
333
22
1
'''

n=int(input())
for i in range(n,0,-1):
    print(str(i)*i)