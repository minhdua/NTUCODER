# SaitamaCoder

def Main():
	arr1 = [int(x) for x in input().split()]
	arr2 = [int(x) for x in input().split()]
	arr3 = arr1 + arr2
	arr4 = arr1 + arr2
	arr3 = sorted(arr3)
	arr4 = sorted(arr4,reverse = True)
	print("Merge two Increment List: ",arr3)
	print("Merge two Decrement List: ",arr4)
if __name__=='__main__':
	Main()
