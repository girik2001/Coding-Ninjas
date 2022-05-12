'''
Sample Input 1 :
121
Sample Output 1 :
true

Sample Input 2 :
1032
Sample Output 2 :
false
'''

n=int(input())
temp=n
reverse=0
while temp!=0:
    last=temp%10
    reverse=reverse*10+last
    temp=temp//10
if n==reverse:
    print('true')
else:
    print('false')