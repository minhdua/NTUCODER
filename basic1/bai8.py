# SaitamaCoder

def Main():
	str = input()
	print('length: ',len(str))
	print('first char: ',str[0])
	print('last char: ',str[-1])
	for i in range(len(str)):
		print('Ki tu thu %d la %s: '%(i,str[i]))

if __name__=='__main__':
	Main()

