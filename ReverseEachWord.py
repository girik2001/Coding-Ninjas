'''
Sample Input 1:
Welcome to Coding Ninjas
Sample Output 1:
emocleW ot gnidoC sajniN

Sample Input 2:
Always indent your code
Sample Output 2:
syawlA tnedni ruoy edoc
'''

def reverseEachWord(string) :
    string=string.split()
    for i in range(len(string)):
        string[i]=string[i][::-1]
    return " ".join(string)

s=input().strip()
print(reverseEachWord(s))