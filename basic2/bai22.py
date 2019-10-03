# SaitamaCoder

def Factorial(n):
	f = 1
	for x in range(1,n+1):
		f *=x
	return f

def Main():
	n = int(input())
	factor_n = Factorial(n)
	print(factor_n)	

if __name__=='__main__':
	Main()
