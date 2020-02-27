# Examples of Arithmetic Operator 
a = 9
b = 4

add = a + b # Addition of numbers
sub = a - b # Subtraction of numbers 
mul = a * b # Multiplication of number 
div1 = a / b # Division(float) of number 
div2 = a // b # Division(floor) of number 
mod = a % b # Modulo of both number 

# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod) 

x = 5
# returns True because 5 is greater than 3 AND 5 is less than 10
print(x > 3 and x < 10)

x = 5
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
print(x > 3 or x < 4)

x = 5
# returns False because not is used to reverse the result
print(not(x > 3 and x < 10))

x = 5
y = 3
# returns True because five is greater, or equal, to 3
print(x >= y)

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2
#the floor division // rounds the result down to the nearest whole number
print(x // y)

x = 5
y = 2
print(x % y) #Modulus


x = ["Collins", "Rodney"]
# returns True because a sequence with the value "Kaniki" is not in the list
print("Kaniki" not in x)

x = ["Joy", "Pierra"]
# returns True because a sequence with the value "Pierra" is in the list
print("Pierra" in x)

x = ["Alfred", "Ezzy"]
y = ["Alfred", "Ezzy"]
z = x
# returns False because z is the same object as x
print(x is not z)
# returns True because x is not the same object as y, even if they have the same content
print(x is not y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print(x != y)

x = ["Kellen", "Ivy"]
# returns True because a sequence with the value "Kellen" is in the list
print("Kellen" in x)

#!/usr/bin/python

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)








