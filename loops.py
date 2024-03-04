# Loops in python are used when we want to perform certain action repeatedly.
# There are mainly two types of loops i.e. 'for' loop and 'if-else', 'if-elif-else'.

########################################################## 'for' loop ############################################################

# The way how 'for' loop works is it iterates through each element in the list and preforms action as specified 

# 'for' loop syntax is as follows:
# for <variable_name> in <list_name>:
#     <action to be performed on each element in the list>

## Example 1: Print all the elements in the list

shopping_cart = [5, 10, 15] # define a list

for each_element in shopping_cart:
    print(each_element)
# Working: 'for' loop will iterate through each element one by one in the list and print each element. i.e.
# first iteration: first element of the list i.e. '5' will be stored in 'each_element' variable, it will be printed
# second iteration: second element of the list i.e. '10' will be stored in 'each_element' variable, it will be printed
# and so on....

# Example 2: Find sum of all values in shopping_cart list:

sum = 0 # initialize value of sum varibale to 0
for each_element_price in shopping_cart:
    sum = each_element_price + sum
print(sum)

# Working: first iteration: first value of list i.e. '5' will be stored in 'each_element_price' variable. Action i.e. addition will
# be performed i.e. 5 + 0 = 5. The new value of 'sum' is 5
# second iteration: second value of list i.e. '10' will be stored in 'each_element_price' variable. Action i.e. addition will
# be performed i.e. 10 + 5 = 15. The new value of 'sum' is 15
# and so on......
# 5 + 0 = 5
# 5 + 10 = 15
# 15 + 15 = 30
# Final value of 'sum' i.e. '30' will be printed.

####################################################### 'if-else' statement #########################################################

# 'if-else' statement is used when the action needs to be performed under certain conditions. The syntax is as follows:
# if condition:
#     action1
# else:
#     action2

# Note: 'else' block is an optional block. If no else block is specified, it means do nothing.

# Example 1: If number is less than 10 print the number, if number is greater than 10 print it's index

for each_element_price in shopping_cart: # iterate through the list
    if each_element_price < 10: # conditional statement to check if a number of less or greater than 10
        print(f'Each element price less than 10 is {each_element_price}') # Print number if it's less than 10
    else: # default condition if all the above conditions are false
        print(f'Each element position for price greater than 10 is {shopping_cart.index(each_element_price)}') # Print index of the number that is greater than 10
 
####################################################### 'if-elif-else' statement ######################################################

# 'elif' condition is used when we want to specify more than one conditions in 'if-else' block

# Example 1: Print 'single digit number is <number>', 'double digit number is <number>' or else print 'Three digit'  

l1 = [1, 2, 12, 100]

for each_element in l1:
    if each_element < 10:
        print(f'single digit number is {each_element}')
    elif each_element >=10 and each_element < 100:
        print(f'double digit number if {each_element}')
    else:
        print(f'Three digit number is {each_element}')