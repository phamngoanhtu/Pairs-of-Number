##
import sys
##
pairs = 0
ar = []
n = int (input())
for i in range(n):
    ar.append(sys.stdin.readline())
arset = set(ar)
#For more info about why set: https://www.w3schools.com/python/python_sets.asp
for i in arset:
    cnt_ele = ar.count(i)
    if cnt_ele >= 2:
        pairs += ((cnt_ele)*(cnt_ele - 1)/2) #Formula: n*(n-1)/2
print(int(pairs))

