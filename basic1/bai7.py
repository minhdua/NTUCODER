# SaitamaCoder
import math as m
def Main():
	a,b,c = [int (i) for i in input().split()]

	delta = b*b - 4*a*c

	if delta < 0 : print("PTVN")
	elif delta == 0:
		x = -b/(2*a)
		print("x = %f"%(x))
	else:
		x1 = (-b + m.sqrt(delta))/(2*a)
		x2 = (-b - m.sqrt(delta))/(2*a)
		print("x1 = %f, x2 = %f"%(x1,x2))

if __name__ == '__main__':
	Main()

