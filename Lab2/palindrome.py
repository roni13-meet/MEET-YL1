def pali():
	n = raw_input("Please write something")	
	if n == n[::-1]:
		return True
	else:
		return False

if __name__ == "__main__":
	print pali()
