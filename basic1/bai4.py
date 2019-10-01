import math
def getDienTich(r):
	return 2*math.pi*r
def getChuVi(r):
	return math.pi*r*r

def Main():
	bk = int(input())
	print (getDienTich(bk))
	print (getChuVi(bk))

if __name__ == '__main__':
	Main()
