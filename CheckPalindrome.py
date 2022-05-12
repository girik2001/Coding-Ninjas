'''
Sample Input 1 :
abcdcba
Sample Output 1 :
true 

Sample Input 2:
coding
Sample Output 2:
false
'''

def isPalindrome(string) :
    if string == string[::-1]:
        return True
    else:
        return False
	
s=input()
ans=isPalindrome(s)

if ans :
    print('true')
else :
    print('false')