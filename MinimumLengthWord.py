'''
Sample Input 1 :
this is test string
Sample Output 1 :
is

Sample Input 2 :
abc de ghihjk a uvw h j
Sample Output 2 :
a
'''

s=input().split()
l=len(s[0])
res=s[0]
for i in range(len(s)):
    if len(s[i])<l:
        l=len(s[i])
        res=s[i]
print(res)