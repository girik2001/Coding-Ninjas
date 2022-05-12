'''
Sample Input 1:
aabccbaa
Sample Output 1:
abcba

Sample Input 2:
xxyyzxx
Sample Output 2:
xyzx
'''

def removeConsecutiveDuplicates(string) :
    res=string[0]
    for i in range(len(string)):
        if res[-1]!=string[i]:
            res=res+string[i]
    return res
        
s=input().strip()
print(removeConsecutiveDuplicates(s))