# Weekly Task 07
# es.py
# Program that counts the occurance of the letter 'e' in a text file
# Author: Rebecca Feeley

import sys
# This sys module is imported for using argv function (a sub-module of os)

# I am making the assumption that the file to be counted already exists in the same directory as es.py
# I am not specifying the filename as it will be passed as an argument to the function from the command line
# instead of being written in the program

def count_es(filename): # function to return the count of the frequency of 'e'
    with open (filename) as f: #file is opened in read mode
        text = f.read()  # the content of the file is assigned as a variable
    return text.count('e') # this only counts occurances of lowercase 'e'; uppercase 'E' requires a second function
    # I used the count() function of python here instead of a for loop.
    # while a for loop would also work, the built-in count() function is more efficent

# here I created a second function to count all of the uppercase 'E's separately, as it is considered a different character
def count_Es(filename): # the content of this function is almost the same as count_es, except for it is counting 'E's.
    with open (filename) as f:
        text = f.read()
    return text.count('E')


filename = sys.argv[1] # takes in name of file from command line argument entered
#argv is for showing all the arguments passed to the script. 
# The first item i.e 0 is the name of the script itself, i.e es.py in this case
# So, argv[1] will get the second item, i.e mobydick.txt so that I can calculate the occurance of the letter 'e'
print("The number of occurances of the lowercase letter 'e' is: " + str(count_es(filename)))
# print a message for user; result is converted to a string as it cannot concatenate as an integer with a string
print ("The number of occurances of the uppercase letter 'E' is: " + str(count_Es(filename)))
# print a message for the user; result is converted to a string as you can only concatenate str to str (i.e add)
print ("The overall occurances of both the lowercase 'e' and uppercase 'E' is: ", int(count_es(filename)) + int(count_Es(filename)))
# here the results of the function are kept as integers as addition is being performed on them. If converted to strings, it would not  
# be accurate; no addition would occur but the strings would be joined together instead of mathematically added.

