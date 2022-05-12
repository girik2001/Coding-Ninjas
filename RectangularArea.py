'''
Sample Input:
1
1
3
3
Sample Output:
4

Explanation:
The given coordinates of the diagonal are (x1,y1) = (1,1) and (x2,y2) = (3, 3). 
The area of the rectangle can then easily be calculated as: 
(3 – 1) * ( 3 – 1) = 2 * 2 = 4 
'''

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
print((x2-x1)*(y2-y1))