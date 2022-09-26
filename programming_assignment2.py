# Q1. Write a Python program to convert kilometers to miles?
def kmTom(n):
    meter = n * 1000
    print("value of",n, "kilometers in meters is", meter, "meters")
num = int(input("value in kilometers: "))
kmTom(num)

# Q2. Write a Python program to convert Celsius to Fahrenheit?
def forenite(value):
    f= ((value*9/5)+32)
    print("Value of", value,"celsius is",f,"forenite")
a = int(input("insert the value in celsius: "))
forenite(a)

# Q3. Write a Python program to display calendar?
import calendar
year = int(input("enter year:"))
month = int(input("enter month number(1-12):"))
print(calendar.month(year,month))

#Q4. Write a Python program to solve quadratic equation?
import math
def roots(a,b,c):
    d = (b*b-4*a*c)
    sqrt_d = math.sqrt(d)
    if d==0:
        print("both roots are same & real and roots are - ")
        print(-b/(2*a))
    if d>0:
        print("both roots are distinct & real and roots are-")
        print((-b+sqrt_d)/(2*a))
        print((-b-sqrt_d) / (2 * a))
    if d<0:
        print(" both roots are complex and roots are-")
        print((-b / (2 * a)), "+i",sqrt_d)
        print((-b / (2 * a)) , "-i",sqrt_d)
a = int(input("enter coefficient of x^2 : "))
b = int(input("enter coefficient of x : "))
c = int(input("enter constant term : "))
roots(a,b,c)
# Q5. Write a Python program to swap two variables without temp variable?
def swap(a,b):
    a, b = b, a
    print("value of a is now:", a)
    print("value of b is now:", b)

a = input("enter first value a: ")
b = input("enter second value b: ")
swap(a,b)