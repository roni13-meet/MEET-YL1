def divisors1():
	n = int(raw_input("please put a number"))
	for num in xrange(1,n):
		print num

def divisors2():
	n = int(raw_input("please put a number"))
	for num in xrange(1,n):
		if n % num == 0:	
			print num

def divisors3(n):
	for num in xrange(1,n):
		if n % num == 0:	
			print num

if __name__ == "__main__":
	divisors3(100)
