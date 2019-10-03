# SaitamaCoder

def Main():
	arr = [int(x) for x in input().split()]
	arr_inc = sorted(arr)
	arr_dec = sorted(arr,reverse = True)
	print("Increment : ",arr_inc)
	print("Decrement : ",arr_dec)

if __name__=='__main__':
	Main()
