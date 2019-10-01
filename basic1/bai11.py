# SaitamaCoder
def add_tags(a,b):
	opentag = a.join(('<','>'))
	closetag = a.join(('</','>'))
	return opentag + b + closetag
def Main():
	tag,name = input().split()
	result = add_tags(tag,name)
	print(result)

if __name__=='__main__':
	Main()
