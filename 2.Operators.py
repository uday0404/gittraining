x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
x = 5

x += 3

print(x)
x = 5

x -= 3

print(x)
x = 5

x &= 3

print(x)


x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3
x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3
x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3
x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


Conditional Operators:
-------------------------
>
<
==
!=
>=
<=

Logical Operators:
-------------------------
And

T and T = T
T and F = F
F and T = F
F and F = F

Or
T or T = T
T or F = T
F or T = T
F or F =f

Not
not T=F
not F=T

Arithmetic Operators:
-----------------------
+,-,*,%,/

Comparison Operators:
----------------------
==, >=,<=,>,<

Logical Operators:
----------------------
AND, OR, NOT