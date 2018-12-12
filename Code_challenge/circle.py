import math
while(True):
	try:
		radius=int(input("Enter radius of circle: "))
		if (radius<0):
			print("Invalid radius.")
	except ValueError :
		print("Not a number.")
	else:
		break
area=math.pi*(radius**2)
perimeter=2*math.pi*radius
print("The Area of the Circle is: %d\n The perimeter of Circle is: %d"%(area,perimeter))
