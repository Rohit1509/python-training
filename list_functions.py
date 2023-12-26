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

