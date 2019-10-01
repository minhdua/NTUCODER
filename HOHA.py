# SaitamaCoder
import math as m
# read n
n = int(input())
# get divisors refer to list
list = list()
for d in range(1,int(m.sqrt(n))+1) :
	if n%d==0 :
		list.append(d)
		if n//d != d: list.append(n//d) 

if sum(list) == 2*n :
	print('YES')
else : print('NO')


