import math
def is_prime(n):
    if n == 2 : return True
    elif n % 2 == 0 or n == 1:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1,2):
        if n % i == 0:
            return False
    return True

def Main():
	n = int(input())
	if is_prime(n):
		print('YES')
	else: print('NO')


if __name__ == "__main__":
	Main()


