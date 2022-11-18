# create a tuple using ()
from ast import Num
from parser import tuple2st
from turtle import position


Num = (10, 20, 30, 40)
print(Num)

# string tuple
str = ('Jessa', 'Emma', 'Kelly')
print(str)

# hetrogeneous tuple
num_str = ('jessa', 30, 40, 50)
print(num_str)

# create tuple using tuple() constructor
t1 = tuple(('Jessa', 30, 40, 50, [23, 78]))
print(t1)

# creating a single tuple
t1 = ("hello")
print(type(t1))

# with comma
t2 = ("hello",)
print(type(t2))

# Packing and unpacking
# A tuple can also be created without using a tuple() constructor or enclosing the items inside the parentheses. It is called the variable “Packing.”

t2 = 1, 2, "hello"
print(t2)

# Unpacking tuple into variables
# Similarly, we can unpack the items by just assigning the tuple items to the same number of variables. This process is called “Unpacking.”
i, j, k = t2
print(i, j, k)

# length of a tuple 
t3 = ('p', 'y', 't', 'h', 'o', 'n')
print(len(t3))

# Iterating a tuple
t = tuple((1, 2, 3, "hello", [4, 8, 16]))

# iterate a tuple
for item in t:
    print(item)

# Accessing items of a tuple
t4 = ('t', 'e', 'a', 'm')
for i in range(4):
    print(t4[i])
   # print(t4[5])


# Negative Indexing
t5 = ('M', 'a', 'y', 'u', 'r', 'i')
print(t5[-3])

# iterating a tuple using negative indexing
for i in range(-6, 0):
   print(t5[i], end=",")

# slicing a tuple
t6 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# slice a tuple with start and end index number
print('\n',t6[1:5])

# slice a tuple without start index
print(t6[:5])

# slice a tuple wihout end index
print(t6[6:])

# slice a tuple using negative indexing
print(t6[-5:-1])

# finding an item in a tuple
t7 = (10, 20, 30, 40)

# get index of item 30
position = t7.index(20)
print(position)

# find within a range
position = t7.index(30, 1, 3)
print(position)

# checking if an item exists
t8 = (10, 20, 30, 40, 50, 60, 70, 80)
# checking whether item 50 exists in tuple

print(50 in t8)

print(500 in t8)

# Adding and changing item in a tuple
t9 = (0, 1, 2, 3, 4, 5)
# t9[1] = 10

# converting tuple into a list
list1 = list(t9)
# add item to list list1 
list1.append(6)
print(list1)

# converting list back into a tuple
t9 = tuple(list1)
print(t9)

# Modify nested items of a tuple
tuple1 = (10, 20, [25, 75, 85])
# before update
print(tuple1)

# modify last item's first value
tuple1[2][0] = 250

# after update
print(tuple1)

# Removing items from a tuple
# using del keyword

# sampletup1 =(0,1,2,3,4,5,6,7,8,9,10)
# del sampletup1

# print(sampletup1)

# By converting into a list
tuple1 = (0, 1, 2, 3, 4, 5)

# converting tuple into a list
sample_list = list(tuple1)
# reomve 2nd item
sample_list.remove(2)

# converting list back into a tuple
tuple1 = tuple(sample_list)
print(tuple1)  
