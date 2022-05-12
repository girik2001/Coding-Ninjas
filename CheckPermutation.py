'''
Sample Input 1:
abcde
baedc
Sample Output 1:
true

Sample Input 2:
abc
cbd
Sample Output 2:
false
'''

s1=input().strip()
s2=input().strip()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print('true')
    else:
        print('false')
else:
    print('false')