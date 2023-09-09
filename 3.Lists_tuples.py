List - is a collection which is ordered and changeable. Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary - is a collection which is ordered** and changeable. No duplicate members.

Lists:
-----------------
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .

List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("Original list ", List)
 
List[3] = 77
print("Example to show mutablity ", List)


sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures[-3])
sea_creatures[1] = 'octopus'
sea_creatures[-3] = 'blobfish'
print(sea_creatures)
print(sea_creatures[1:4])
print(sea_creatures[:3])

List = [True, "mahesh", 4, 4, 3, 3, 3, 6, 5]
print("Original list ", List)


Tuple:
----------------
Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.


tuple1 = (0, 1, 2, 3)
print(tuple1)
print(type(tuple1))
print(len(tuple1))
#tuple1[0] = 4
print(tuple1[1])

thistuple = ("apple", "banana", "cherry", "apple", "cherry") #allows duplicates
print(thistuple) 


tuple1 = ("abc", 34, True, 40, "male")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)


Set:
-----------------
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

--
# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
List = [1, 2, 3, 2]
my_set = set(List)
print(type(my_set))
print(my_set)


--
# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
my_set.remove(1)
print(my_set)

List = [1, 2, 3, 2]
print(List[1])
my_set = set(List)
print(type(my_set))
print(my_set[1])