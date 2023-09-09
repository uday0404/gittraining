Python Slice
------------------------------------------------------
The slice() function returns a slice object that is used to slice any sequence (string, tuple, list, range, or bytes).

slice() can take three parameters:

start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.

py_list = ['P', 'y', 't', 'h', 'o', 'n']
py_tuple = ('P', 'y', 't', 'h', 'o', 'n')

# contains indices 0, 1 and 2
slice_object = slice(3)
print(py_list[slice_object]) # ['P', 'y', 't']

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object]) # ('y', 'h') 

-----

text = 'Python Programing'

# get slice object to slice Python
sliced_text = slice(6)
print(text[sliced_text])

# Output: Python

text = 'Python Programing'

# get slice object to slice Python
sliced_text = slice(6)
print(text[sliced_text])

print(text[slice(1,6)])
print(text[slice(1)])

----
# List slicing
L = [1, 2, 3, 4, 5]
s1 = slice(3)
s2 = slice(1, 5, 2)
 
print("List slicing")
print(L[s1])
print(L[s2])

----
# Tuple slicing
T = (1, 2, 3, 4, 5)
s1 = slice(3)
s2 = slice(1, 5, 2)
 
print("Tuple slicing")
print(T[s1])
print(T[s2])

----
# list -ve index slicing
l = ['a', 'b', 'c', 'd', 'e', 'f']
print("list slicing1:", l[slice(2)])
print("list slicing1:", l[slice(-2)])
print("list slicing1:", l[slice(1,3)])
print("list slicing1:", l[slice(0,5,2)])
print("list slicing1:", l[slice(-5,5,2)])
print("list slicing:", l[slice(-2, -6, -1)])
 
# string -ve index slicing
s = "geeks"
slice_obj = slice(-1)
print("string slicing:", s[slice_obj])
 
# tuple -ve index slicing
t = (1, 3, 5, 7, 9)
slice_obj = slice(-1, -3, -1)
print("tuple slicing:", t[slice_obj])

l = {'a', 'b', 'c', 'd', 'e', 'f'}
print("list slicing1:", l[slice(2)]) #slice not allowed on set.