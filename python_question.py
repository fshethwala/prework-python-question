#Question 1
def hello_name(user_name):
    return ("Hello " + user_name + "!")
print(hello_name("USERNAME"))

#Question 2
def first_odds():
    for x in range (1,100):
         if x % 2 == 1:
             print (x)
print (first_odds())

#Question 3
def max_num_in_list(a_list):
    #We have to create a variable for the max number at the beginning of list to start
    maxnumber = a_list[0]
    #loop to check through each number in list
    for g in a_list:
        #conditional if x is greater than value at position 0, x becomes new MaxNumber
        if g > maxnumber:
            maxnumber = g
    return maxnumber
print("Max Number in list is: ", max_num_in_list([8,12,16,64]))

#Question 4
def is_leap_year(a_year):
    #setting initial boolean parameter
    isLeap = False
    #conditional check to determine if input variable is divisible by first condition
    if a_year % 4 == 0 and a_year % 100 != 0:
        isLeap = True
    #conditional check to determine if input variable is divisible by second condition
    elif a_year % 400 == 0:
        isLeap = True
    return isLeap

print (is_leap_year(1980))

#Question 5
def is_consecutive (a_list):
    #sort the given list, and compare it to a created consecutive list using the range function and adding +1 to the STOP because it is exclusive by default
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

print (is_consecutive([1,2,3,4,5]))




    
