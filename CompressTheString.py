'''
Sample Input 1:
aaabbccdsa
Sample Output 1:
a3b2c2dsa

Explanation for Sample Output 1:
In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is repeated 2 times and 'd', 
's' and 'a' and occuring 1 time hence no compression for last 3 characters.

Sample Input 2:
aaabbcddeeeee
Sample Output 2:
a3b2cd2e5

Explanation for Sample Output 2:
In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is occuring single time, 
'd' is repeating 2 times and 'e' is repeating 25times.
'''

s=input()
res=[]
i=0
while i<len(s):
    count=1
    j=i+1
    while j<len(s):
        if s[i]==s[j]:
            count=count+1
            j=j+1
        else:
            break
    if count>1:
        res.append(s[i]+str(count))
    else:
        res.append(s[i])
    i=i+count
for i in range(0,len(res)):
    print(res[i],end="")