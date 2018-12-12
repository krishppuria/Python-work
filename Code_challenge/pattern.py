while(True):
	try:
		size=int(input("Enter Number"))
		if(size<0):
			print("Invalid Number")
	except ValueError:
		print("Not a number.")
	else:
		break
[print('*'*n) for n in range(size+1)]
[print('*'*n) for n in range(size-1,0,-1)]
print()
