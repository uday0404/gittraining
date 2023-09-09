    # outer loop to handle number of rows
    # n in this case
    for i in range(0, 5):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
--------------------------------------------
# initialising starting number
num = 1
 
    # outer loop to handle number of rows
for i in range(0, 5):
     
        # re assigning num
    num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
    for j in range(0, i+1):
         
                # printing number
        print(num, end=" ")
         
            # incrementing number at each column
        num = num + 1
     
        # ending line after each row
    print("\r")
   
----------------------------------
num = 5

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
-----------------------------------------
num = 13

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
-----------------------------------------------------
num = 153
sum = 0

while num!=0:
    digit = int(num%10)
    sum += digit
    num = num/10

print(sum)

-------------------------------------------------
num = 125
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
	
----------------------------------------
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1