#question 1: area of circle calculation
pii = 3.142
r = float(input("enter raduis of the circle: \n"))
area = pii*(r**2)
print(f"area of cicle with radius {r} is {area}\n\n")

#question 2: area of triangle
L = float(input("enter a length: "))
w = float(input("enter a width: \n"))
area_rec = L*w
print(f"the area if the triangle is {area_rec}\n\n")

#question 3: area of square
s = float(input("enter the lengh if its side: \n"))
area_sq = s**2
print(f"the area of the square is {area_sq}\n\n")

#question 4: cinditional in areas
shape = input("choose a shape from the list {circle, square, rectangle}: \n")
if shape == "circle":
	r = float(input("enter raduis of the circle: \n"))
	area = pii*(r**2)
	print(f"area of cicle with radius {r} is {area}\n\n")

elif shape == "rectangle":
	L = float(input("enter a length: "))
	w = float(input("enter a width: "))
	
	area_rec = L*w
	print(f"the area if the triangle is {area_rec}\n\n")

elif shape == "square":
	s = float(input("enter the lengh if its side: \n"))
	area_sq = s**2
	print(f"the area of the square is {area_sq}\n\n")
	
else:
	print("enter one of the shapes listed in the brackets...!")	