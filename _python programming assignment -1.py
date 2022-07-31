#!/usr/bin/env python
# coding: utf-8

# Q1. Write a Python program to print "Hello Python"?

# In[2]:


print("Hello Python")


# Q2. Write a Python program to do arithmetical operations addition and division.?

# In[3]:


a=float(input("first number:"))
b=float(input("second number"))
#addition of numbers
print(a+b)
#division of numbers
print(a/b)


# Q3. Write a Python program to find the area of a triangle?

# In[13]:


B=float(input("base of triangle:"))
H=float(input("height of triangle:"))
print("area of triangle:", 0.5*B*H)


# Q4. Write a Python program to swap two variables?

# In[15]:


a= input("first variable a:")
b= input("second variable b:")
# swapping of value
c=a
a=b
b=c
print("a:", a)
print("b:", b)


# Q5. Write a Python program to generate a random number?

# In[23]:


import random
print(random.randint(0,100))

