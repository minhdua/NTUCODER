from collections import Counter 

def Main():
	str = input()
	duplicates = dict(Counter(str))
	print(duplicates)

if __name__ == '__main__':
	Main()

