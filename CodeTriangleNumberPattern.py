'''
Sample Input 1:
5
Sample Output 1:
1
22
333
4444
55555

Sample Input 2:
6
Sample Output 2:
1
22
333
4444
55555
666666
'''

n=int(input())
for i in range(n):
    print(str(i+1)*(i+1))