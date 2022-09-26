# Q1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def type_num(num):
    if num == 0:
        print(num, "is zero")
    elif num > 0:
        print(num, "is positive number")
    else:
        print(num, "is a negative number")
try:
    num = float(input("enter your number: "))
    type_num(num)
except:
    print("please enter a number")




# Q2. Write a Python Program to Check if a Number is Odd or Even?
def even_odd(n):
    if n % 2 == 0:
        print(n, "is an even number")
    if n % 2 != 0:
        print(n, "is an odd number")

try:
    n= int(input("enter number: "))
    even_odd(n)
except:
    print("please enter a integer")

# Q3.3. Write a Python Program to Check Leap Year?

def leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print(year, "is a leap year")
        else:
            if year % 400 == 0:
                print(year, " is a leap year")
            else:
                print(year, "is not a leap year")
    else:
        print(year, "is not a leap year")
try:
    year=int(input("enter year: "))
    leap(year)
except:
    print("enter a valid data")


# Q4. Write a Python Program to Check Prime Number?
try:
    num = int(input("enter number: "))
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
    if prime:
        print("number is prime")
    else:
        print("number is not prime")

except Exception as e:
    print(e)

# Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
n=10000
for i in range(n+1):

    prime = True
    for j in range(2,i):
        if (i % j) == 0:
            prime = False
            break
    if prime:
        print(i)

