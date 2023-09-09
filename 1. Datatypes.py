#numbers examples
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
x = 1.10
y = 1.0
z = -35.59

x = 1.1076543
y = 176453432.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

if 5 > 2:
  print("Hello World!")
  
print("Enter your name:")
x = input()
print("Hello, " + x)


a='Mahesh'
print(type(a))

Casting:
--------------------------
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)


Strings:
-------------------------
a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(len(a))
a = "Hello, World!"
print(a.lower())
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5

word="python"
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])
print(word[0:2])
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print(word[:2])    # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end
print(word[:2] + word[2:])

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

