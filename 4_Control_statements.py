## This is a Sequential statement
 
a=20
b=10
c=a-b
print("Subtraction is : ",c)

The selection statement allows a program to test several conditions and execute instructions based on which condition is true.

Some Decision Control Statements are:
Simple if
if-else
nested if
if-elif-else

Simple if: If statements are control flow statements that help us to run a particular code, but only when a certain condition is met or satisfied. A simple if only has one condition to check.

Simple IF:
--------------------
n = 10
if n % 2 == 0:
   print("n is an even number")
   
   

If Else:
------------------------------
The if-else statement evaluates the condition and will execute the body of if if the test condition is True, but if the condition is False, then the body of else is executed.

n = 5
if n % 2 == 0:
   print("n is even")
else:
   print("n is odd")
   
 
mark = 100
if not (mark == 100):
  print("mark is not 100")
else:
  print("mark is 100")
   
Nested if:
------------------------------------
Nested if statements are an if statement inside another if statement.

a = 5
b = 10
c = 15
if a > b:
   if a > c:
      print("a value is big")
   else:
       print("c value is big")
elif b > c:
    print("b value is big")
else:
     print("c is big")
	 
Elif:
---------------------------
The if-elif-else statement is used to conditionally execute a statement or a block of statements.

x = 15
y = 12
if x == y:
   print("Both are Equal")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")
	
Combinding Multiple Operators:
-------------------------------------
mark = 72
if mark > 80:
  print ("You got A Grade !!")
elif mark >= 60 and mark < 80:
  print ("You got B Grade !!")
elif mark >= 50 and mark < 60:
  print ("You got C Grade !!")
else:
  print("You failed!!")
  
  
For Loop:
----------------------------------
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
     print(lst[i], end = " ")
 
for j in range(0,10):
    print(j, end = " ")
    

    
print("\nExample 1\n")
for i in [1,2,3] :
    print(i)

print("\nExample 2\n")
for name in ["Tom", "Dick", "Harry"] :
    print(name)

print("\nExample 3\n")
for name in ["Tom", 42, 3.142] :
    print(name)

print("\nExample 4\n")
for i in range(3) :
    print(i)

print("\nExample 5\n")
for i in range(1,4) :
    print(i)

print("\nExample 6\n")
for i in range(2, 11, 2) :
    print(i)

print("\nExample 7\n")
for i in "ABCDE" :
    print(i)

print("\nExample 8\n")
longString = "The quick brown fox jumped over the lazy sleeping dog"
for word in longString.split() :
    print(word)
   
While:
-------------------------------------------   
m = 5
i = 0
while i < m:
     print(i, end = " ")
     i = i + 1
print("End")


# while loop
n = 10
cur_sum = 0
# sum of n  numbers
i = 1
while  i <= n :
    cur_sum = cur_sum + i
    i = i + 1
print("The sum of the numbers from 1 to", n, "is ", cur_sum)


Break, Continue
-------------------------------
In Python, the break statement provides you with the opportunity to exit out of a loop when an external condition is triggered. You’ll put the break statement within the block of code under your loop statement

The continue statement gives you the option to skip over the part of a loop where an external condition is triggered, but to go on to complete the rest of the loop.






number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

-------

my_list = ['Siya', 'Tiya', 'Adams', 'Daksh', 'Riya', 'Guru'] 

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Adams':
        print('Found the name Adams')
        break
        print('After break statement')

print('Loop is Terminated')

------

number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')


-----
my_list = ['Siya', 'Tiya', 'Adams', 'Daksh', 'Riya', 'Guru'] 
i = 0

while True:
    print(my_list[i])
    if (my_list[i] == 'Adams'):
        print('Found the name Adams')
        break
        print('After break statement')
    i += 1

print('After while-loop exit')