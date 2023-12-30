# Python provides some in-built functions for list that can be used in the code.

######################################### 1. 'index' function ###################################################

# 'index' function is used to retrieve the index of an element in list
# synatx for using 'index' function is as follows:
# <list_name>.index(<element of the list whose index is to be found>)

# Example 1: print index of all the numbers in the list

l = [6,7,4,5]
for each_element in l: # loop through the list one by one
    print(l.index(each_element)) # print index of each element
    
######################################### 2. 'len' function #####################################################

# 'len' function is used to get total number of elements in the list
# syntax is: len(<list_name>)

l1 = [1,2,3,4]
print(len(l1))

######################################### 3. 'count' function #####################################################

# 'count' function is used to get total number of occourences of a specific element in the list
# syntax: <list_name>.count('<element whose number of occurences is to be found>')

l2 = [1,1,2,3]
print(l2.count(1))

######################################### 4. 'append' function #####################################################

# append function is used to add elements to list
# syntax: <list_name>.append(<element to be added to the list>)

l3 = [1,1,2,3]
l3.append(4)
print(l3)

######################################### 5. 'range' ###############################################################

# 'range' function is ised to get sequence of numbers
# syntax: range(<start_number>, <end_number>). <start_number> is an optional field. By default <start_numer> is 0.
# range(<start_number>, <end_number>) will print values starting (<start_number>, ...., <end_number-1>)

range(4) # is same as # print(range(0, 4))
# this will print values 0, 1, 2, 3.

range(5)
# this will print values 0, 1, 2, 3, 4

range(1, 5)
# this will print values from 1 to 4 i.e. 1,2,3,4

range(0,7,2)
# this will print numners in difference of 2 starting with 0 until 6 i.e. 0,2,

# To print elements from range function

for number in range(0,7,2):
    print(number)

######################################### 6. accessing element of the list ###############################################################

# To access elements of a list we generally use range function
# Syntax: <name_of_the_list>[<index_number_at_which element is to be accessed]

l3 = [48, 59, 39, 15]
#print(l3[0]) # This will print element at index 0 i.e. '48'
print(l3[1])

# Example: Print values at index 0, 1, 2
l3 = [48, 59, 39, 15]

for element in range(3): # This will create a list [0, 1, 2] for looping
    print(l3[element])
   
    