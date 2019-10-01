# SaitamaCoder
def isPalindrome(s):
	rev_s = s[::-1]
	if rev_s == s: return True
	return False
def Main():
	str = input()
	if isPalindrome(str):
		print('YES')
	else : print ('NO')
if __name__=='__main__':
	Main()
