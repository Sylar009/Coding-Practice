print("Hello World! I Don't Give a Bug") 


#================================================================
# Comments in Python
# sample comment  
# This is Python Comment 
name = "sanyam lawania"
print(name) 


#================================================================
# Python Variable
# An integer assignment 
age = 45
  
# A floating point 
salary = 1456.8
  
# A string 
name = "John"
  
print(age) 
print(salary) 
print(name) 

#================================================================
# Python Data Types

x = "Hello World" # string 
x = 50  # integer 
x = 60.5  # float 
x = 3j  # complex 
x = ["geeks", "for", "geeks"]  # list  
x = ("geeks", "for", "geeks")  # tuple 
x = {"name": "Suraj", "age": 24} # dict 
x = {"geeks", "for", "geeks"} # set 
x = True  # bool 
x = b"Geeks" # binary 

#================================================================
# Python Input/Output


# Python program show input and Output 
val = input("Enter your value: ")  
print(val)

#================================================================
# Python Operators

a = 9
b = 4
add = a + b  
  
sub = a - b  
  
mul = a * b  
  
mod = a % b  
  
p = a ** b  
print(add)  
print(sub)  
print(mul)  
print(mod)  
print(p)  

#================================================================
# Logical Operators



a = True
b = False
print(a and b)  
print(a or b)  
print(not a)  

#================================================================
# Bitwise Operators



a = 10
b = 4
print(a & b)  
print(a | b)  
print(~a)  
print(a ^ b)  
print(a >> 2)  
print(a << 2) 

#================================================================
# Assignment Operators


a = 10
b = a  
print(b)  
b += a  
print(b)  
b -= a  
print(b)  
b *= a  
print(b)  
b <<= a  
print(b) 

#================================================================
# Python If Else



i = 20
if (i < 15):  
    print("i is smaller than 15")  
    print("i'm in if Block")  
else:  
    print("i is greater than 15")  
    print("i'm in else Block")  
print("i'm not in if and not in else Block")  


# Example 2: Python if-elif-else ladder


i = 20
if (i == 10):  
    print("i is 10")  
elif (i == 15):  
    print("i is 15")  
elif (i == 20):  
    print("i is 20")  
else:  
    print("i is not present")  

# Python For Loop


for i in range(0, 10, 2):  
    print(i)  

# Python While Loop

# Python program to illustrate while loop  
count = 0
while (count < 3):  
    count = count + 1
    print("Hello Geek") 

# Python Functions
# A simple Python function to check 
# whether x is even or odd 
def evenOdd(x): 
    if (x % 2 == 0): 
        print("even") 
    else: 
        print("odd") 
  
  
# Driver code to call the function 
evenOdd(2) 
evenOdd(3) 