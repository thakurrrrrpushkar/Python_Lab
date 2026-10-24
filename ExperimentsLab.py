#E1
age = int(input("Enter your age: "))
name = input("Enter your name: ")
print("Welcome to python,",name,"!")
print("You are",age,"years old!")
print()

#E2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You aren't eligible to vote.")
print()

#E3
x = int(input("Enter a number to find its factorial: "))
factorial = 1
for j in range(1, x+1):
    factorial *= j
print("The factorial is:",factorial)
print()

#E4
l = []
while True:
    n = int(input("Enter a number: "))
    l.append(n)
    ch = input("Do you want to continue? (Y/N): ")
    if ch in 'Nn':
        break
print(sorted(l))
print()

#E5
string = input("Enter a string to reverse it: ")
string[::-1]
print()

#E6
import math
def AreaCircle(rad):
    ar = math.pi * rad * rad
    return ar
r = int(input("Enter the radius of the circle: "))
a = AreaCircle(r)
print("The area of the circle is: ", a)
print()

#E7
class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
C1 = Car("Aston Martini","DB12 Volante", 2023,"Silver")
C2 = Car("Morris Garages", "Windsor", 2024, "Black")
print(C1.make)
print(C1.model)
print(C1.year)
print(C1.colour)
print(C2.make)
print(C2.model)
print(C2.year)
print(C2.colour)


#E8
