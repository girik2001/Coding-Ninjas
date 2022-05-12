'''
Sample Input:
3
1
2
4
4
2
1
3
2
7
6
Sample Output:
2
2
5
Invalid Operation
Explanation of the sample input
The first number given is 3, so that means two more numbers will be given and we'll have to multiply them and show the result. 
The two numbers are 1 and 2. Their product is 2, so 2 is displayed first in the output. 
Similarly, all the numbers are processed in groups of three. 
The first number tells the operation and the next two numbers tell on which numbers the operation is done. 
This applies to numbers from 1 to 5. 
If the input is 6 (like it is at the end), two more numbers will NOT be provided, you simply have to exit the program. 
Also, if the input is any number except 1 to 6 (like 7 which is at the second last), 
then you simply have to print "Invalid Operation"
'''

while True:
    choice=int(input())
    if choice==1:
        a=int(input())
        b=int(input())
        print(a+b)
    elif choice==2:
        a=int(input())
        b=int(input())
        print(a-b)
    elif choice==3:
        a=int(input())
        b=int(input())
        print(a*b)
    elif choice==4:
        a=int(input())
        b=int(input())
        print(a//b)
    elif choice==5:
        a=int(input())
        b=int(input())
        print(a%b)
    elif choice==6:
        break
    else:
        print("Invalid Operation")