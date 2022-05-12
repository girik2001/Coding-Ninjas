'''
Sample Input 1:
aabccbaa
a
Sample Output 1:
bccb

Sample Input 2:
xxyyzxx
y
Sample Output 2:
xxzxx
'''

def removeAllOccurrencesOfChar(string, ch) :
    res=""
    for i in string:
        if i!=ch:
            res+=i
    return res

s=input().strip()
c=input().strip()
print(removeAllOccurrencesOfChar(s, c))