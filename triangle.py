#program to find hypotenuse and area of a right angle triangle

leg_1 = float(input("Enter the length of first leg of the triangle: "))
leg_2 = float(input("Enter the length of second leg of the triangle: "))
leg_3 = leg_1**2 + leg_2**2
leg_3 = round(leg_3**0.5, 4)
area = round(0.5*leg_1*leg_2, 4)

print(f"For a triangle with legs {leg_1} and {leg_2} the hypotenuse is {leg_3} ")
print(f"For a triangle with legs {leg_1} and {leg_2} the area is {area} ")

