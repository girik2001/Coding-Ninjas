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

def checkPalindrome(num):
    temp=num
    res=0
    while temp!=0:
        last=temp%10
        res=res*10+last
        temp=temp//10
    if res==num:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')