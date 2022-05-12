'''
Sample Input 1:
0 
100 
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37

Sample Input 2:
20
119
13
Sample Output 2:
20  -6
33  0 
46  7
59  15
72  22
85  29
98  36
111 43

Explanation For Input 2:
Start calculating the Celsius values for each Fahrenheit Value which starts from 20. 
So starting from 20, we need to compute its corresponding Celsius value which computes to -6. 
We print this information as <Fahrenheit Value> <a single space> <Celsius Value> on each line. 
Now add 13 to Fahrenheit Value at each step until you reach 119 in this case. 
You may or may not exactly land on the end value depending on the steps you are taking.
'''

s=int(input())
e=int(input())
w=int(input())
for i in range(s,e+1,w):
    print(i,int((i-32)*5/9))