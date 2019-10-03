# SaitamaCoder

def getMax(arr):
	return max(arr)

def Main():
	arr = [int(x) for x in input().split()]
	maximum = getMax(arr)
	print(maximum)

if __name__=='__main__':
	Main()
