'''
Sample Input :
3
9 8 9
Sample Output :
26
'''

n=int(input())
a=list(map(int,input().split()))[:n]
print(sum(a))