# SaitamaCoder

def Multi_array(arr):
	sumx = 1
	for i in arr:
		sumx *=i
	return sumx

def Main():
	arr = [int(x) for x in input().split()]
	mul = Multi_array(arr)
	print(mul)

if __name__=='__main__':
	Main()
