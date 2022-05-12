'''
Sample Input 1 :
1234
Sample Output 1 :
4321

Sample Input 2 :
1980
Sample Output 2 :
891
'''

n=int(input())
reverse=0
while n!=0:
    last=n%10
    reverse=reverse*10+last
    n=int(n/10)
print(reverse)