#!/usr/bin/python3
import sys

def main():
	
	if  len(sys.argv) != 2:
		print("Usage: nqueens N")
		sys.exit(1)
	try:
		n = int(sys.argv[1])
		if n < 4:
			raise Exception("N must be at least 4")
		else:
			print("lets goo..")
		
	except ValueError:
		raise("N must be a number")
		sys.exit(1)
	except Exception as err:
		raise(err)
		sys.exit(1)

			
main()

