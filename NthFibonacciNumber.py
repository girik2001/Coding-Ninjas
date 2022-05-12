'''
Sample Input 1:
6
Sample Output 1:
8

Explanation of Sample Input 1:
Now the number is ‘6’ so we have to find the “6th” Fibonacci number
So by using the property of the Fibonacci series i.e 
[ 1, 1, 2, 3, 5, 8]
So the “6th” element is “8” hence we get the output.
'''

n=int(input())
a=1
b=1
c=0
if n==1 or n==2:
    print(1)
else:
    while n-2>0:
        c=a+b
        a=b
        b=c
        n-=1
    print(c)