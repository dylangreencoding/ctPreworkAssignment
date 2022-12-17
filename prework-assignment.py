# ********************************************
# QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print('"hello_' + user_name + '!"')

# hello_name("USERNAME")
# USERNAME is the argument passed to the parameter user_name - the input of the function. Here is version 2:


def hello_name2(user_name):
    doomed_list = []
    for letter in user_name:
        doomed_list.append(letter)
    while doomed_list:
        doomed_list.pop()
    user_name = "This function takes an input, then prints something."
    print('"hello_USERNAME!"')


# hello_name2("USERNAME")

# ***********************************************
# QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1, 101, 2):
        print(number)


# first_odds()
# 101 is excluded

def first_odds2():
    for number in range(1, 101):
        if not (number/2).is_integer():
            print(number)


# first_odds2()
# Seems like there is a method for just about everything

def first_odds3():
    for number in range(1, 101):
        if (number / 2) % 1 != 0:
            print(number)


# first_odds3()
# I am still trying to fully understand the difference between modulo (python) and remainder (javascript)

# *************************************************
# QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):

    num_list = []
    for item in a_list:
        if type(item) == int or type(item) == float:
            num_list.append(item)

    for item in num_list:
        if item == num_list[0]:
            largest = item
        elif item > largest:
            largest = item

    return largest


# stuff = ['str', True, [], {}, 1.5, 3, -1, 1000, 71.3, 0, 32, -140, -2, 80]
# print(max_num_in_list(stuff))


def max_num_in_list2(a_list):
    num_list = []
    for item in a_list:
        if type(item) == int or type(item) == float:
            num_list.append(item)

    return max(num_list)


# stuff = ['str', True, [], {}, 1.5, 3, -1, 1000, 71.3, 0, 32, -140, -2, 80]
# print(max_num_in_list2(stuff))


# ***********************************************
# QUESTION 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    #    leap_year = True
    if a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    elif a_year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


# while True:
#    print(is_leap_year(int(input("Enter year: "))))
# Seems to work...

# *********************************************
# QUESTION 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    consecutive = True
    for item in a_list:
        if item == a_list[0]:
            n = item
        elif item == n + 1 or item == n - 1:
            n = item
        else:
            consecutive = False

    return consecutive


# ascending = [-1, 0, 1, 2, 3, 4]
# descending = [1, 0, -1, -2, -3, -4]
# vacillating = [1, 0, -1, 0, 1, 0, -1]
# nonconsecutive = [1, 3, 5, -32, 0]
# print(is_consecutive(ascending))
# print(is_consecutive(descending))
# print(is_consecutive(vacillating))
# print(is_consecutive(nonconsecutive))
# Assuming list is all numbers since already dealt with that in question 3
# A cursory google gave me some conflicting info on whether consecutive numbers have to be ascending or not.
# Removing "or item == n - 1" from line 119 makes the function return True only for ascending consecutive numbers
# Later I will figure out how to get it to return True only for ascending and descending, but not vacillating
# But right now I am sleepy
