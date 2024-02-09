#calculating the area and perimeter of a triangle

side1 = int(input("Enter number 1"))#asking for user input
side2 = int(input("Enter number 2"))
side3 = int(input("Enter number 3"))

Perimeter = (side1 + side2 +side3)#calculating perimeter (a+b+c)
s = Perimeter/2 #finding the s in Heron's formula, which is perimeter halved, or divided by 2
Area = s*(s - side1) * (s-side2) * (s-side3)#calculating area s*(s-a)(s-b)(s-c)

print("The perimeter of the triangle is:", Perimeter) #putting a name to the value perimeter
print("The area of the triangle is:", Area)#putting a name to the value area



##Test if the three sides entered actually form a triangle
#looked up how to check this and the first thing that popped up on the side of the page was this hint below:
#Hint :three numbers can be the sides of a triangle
#if none of the numbers are greater than or equal to the sum of the other two numbers.
#I didn't look for the code as I knew from there, but it did help so I'm crediting it (it's from brainly.in)
Triangle = False


if side1 >= (side2 + side3):#checking if side1 is bigger than the sum of side2 and side3
    Triangle = False#this doesn't really do anything, just there to differentiate. 
    print("These numbers do not form a triangle.")
elif side2 >= (side1 +side3):#checking if side 2 if bigger than the sum of side1 and side3
    Triangle = False
    print("These numbers do not form a triangle.")
elif side3 >= (side2 + side1):#checking if side 3 is bigger than the sum of side2 and side1
            Triangle = False
            print("These numbers do not form a triangle.")
else:#if none of those conditions are fulfilled, this triggers, meaning it can make a triangle
    Triangle = True
    print("These numbers make a proper triangle! Good job!")
