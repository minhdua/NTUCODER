# SaitamaCoder

def Main():
	n = int(input())
	s = sum([i for i in range(1,n+1)])
	s1 = sum([2*i-1 for i in range(1,n+1)])
	s2 = sum([i*2 for i in range(1,n+1)])
	s3 = sum([i*i for i in range(1,n+1)])
	s4 = sum([float(1/(2**i)) for i in range(0,n+1)])
	print('s = ',s)
	print('s1 = ',s1)
	print('s2 = ',s2)
	print('s3 = ',s3)
	print('s4 = ',s4)
if __name__ == '__main__':
	Main()

