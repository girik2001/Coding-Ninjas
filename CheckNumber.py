'''
Sample Input 1 :
10
Sample Output 1 :
Positive

Sample Input 2 :
-10
Sample Output 2 :
Negative
'''

n=int(input())
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")