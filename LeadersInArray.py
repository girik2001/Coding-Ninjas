'''
Sample Input 1 :
6
3 12 34 2 0 -1
Sample Output 1 :
34 2 0 -1

Sample Input 2 :
5
13 17 5 4 6
Sample Output 2 :
17 6
'''

s=input().split()
l=len(s[0])
res=s[0]
for i in range(len(s)):
    if len(s[i])<l:
        l=len(s[i])
        res=s[i]
print(res)