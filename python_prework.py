# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of code has been defined as below.
# def hello_name(user_name):

from calendar import leapdays
from multiprocessing import reduction
from xmlrpc.client import Boolean, boolean


def hello_name(user_name):
    print("Hello, " + user_name + "!")
hello_name("Damon")



# Question 2: Write a python function, first_odds that print the odd numbers from 1-100 and returns nothing
def first_odds(num):
    while num < 100:
        print(num)
        if first_odds == 100:
            return None
        num +=2 
first_odds(1)

# Question 3: Please write a python function, max_num_in_list to return the max number given. 
# The first line of code has been defined as below.
# def max_num_in_list(a_list):
def max_num_in_list(a_list):
    return max(a_list)

maximum = max_num_in_list(a_list=[1,34,12,45,15,])
print(maximum)



# Question 4: Write a funtion to return if the given year is a leap year.
# A leep year is divisible by 4, but not divisible by 100, unless it is also divisible by 400
# The return should be boolean type (true/false)
def is_leap_year(a_year):
    boolean = False
    if a_year % 4 == 0:
        if a_year % 10 != 0 or a_year % 400 == 0:
            boolean = True
        else:
            boolean = False
    return boolean
print(is_leap_year(1600))
print(is_leap_year(1942))

# Question 5: Write a function to check to see if all numbers in list are consecutive numbers.
# for example [2,3,4,5,6,7] are consecutive
# but [1,2,4,5] are not consecutive
# return should be boolean type

def is_consecutive(a_list):
    for numbers in a_list:
        if numbers +1 == a_list[+1]:
            return True
        else:
            return False
numbers = is_consecutive(a_list=[1,2,3,4,5,6])
print(numbers)

numbers = is_consecutive(a_list=[1,6,3,5,4,])
print(numbers)