import math
while(True):
	try:
		num=float(input("Enter a Number: "))
		if (num<0):
			print("Invalid Number.")
	except ValueError :
		print("Not a number.")
	else:
		break

print(math.factorial(num))
