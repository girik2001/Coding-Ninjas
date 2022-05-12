'''
Sample Input 1:
1234
Sample Output 1:
6 4

Sample Input 2:
552245
Sample Output 2:
8 15

Explanation for Input 2:
For the given input, the even digits are 2, 2 and 4 and if we take the sum of these digits 
it will come out to be 8(2 + 2 + 4) and similarly, if we look at the odd digits, 
they are, 5, 5 and 5 which makes a sum of 15(5 + 5 + 5). Hence the answer would be, 8(evenSum) <single space> 15(oddSum)
'''

n=int(input())
sumodd=0
sumeven=0
while n>0:
    last=n%10
    if last%2==0:
        sumeven+=last
    else:
        sumodd+=last
    n//=10
print(sumeven,sumodd)