'''
Sample Output 1:
*
**
***
****
*****

Sample Input 2:
6
Sample Output 2:
*
**
***
****
*****
******
'''

n=int(input())
for i in range(n):
    print("*"*(i+1))