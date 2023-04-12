# Pands-problem-sheet - Weekly Solutions

## Introduction
This repository contains the solutions for the weekly problem sheets as part of 52167 Programming and Scripting 2023 at ATU Galway.  
Author: Rebecca Feeley  
Student ID: G00425652

## Requirements  


### Task 1 Solution & References  
>Commit and push a file to the problem sheet called helloworld.py which should contain a python program that >displays Hello World! when it is run.  

This is a simple beginner program which displays "Hello World!" when it is run.
  
### Task 2 Solution & References   
>Write a program called bank.py which prompts the user and read in two money amounts (in cent); adds the two >amounts and prints out the answer in a format with a euro 
>sign and decimal point between the euro and cent of the amount.

User is asked to input two values in cents. The values inputted are converted to integers so they are not interpreted as strings.  
The two user inputs are then added together. To get the result in a euro format, the result of this is divided by 100 and uses the sum format.  
Also, the result is converted to a floating point number so that the result can display a decimal point, as per the task requirement.  

***References:***      
https://stackoverflow.com/questions/320929/currency-formatting-in-python  
https://www.w3schools.com/python/ref_string_format.asp    
  
### Task 3 Solution & References  
>Write a python program called accounts.py that reads in a 10 character account number and outputs the account ?>number with only the last 4 digits showing (and the first 6 digits replaced with Xs).  

Asks user to input a bank a/c 10 digits long. This input is converted to a string.   
The program catches if the person enters less than 10 digits and using a while loop, continues to prompt the user until they input an a/c number that is 10 digits long.  
This program uses the rjust built-in string method in Python. This rights aligns the string, and using the specified chartacter 'X', replaces the first 6 digits with 'X'  
so that the output is the same length as the a/c number inputted, with only the last 4 digits showing.  

***References:***   
https://www.w3schools.com/python/ref_string_rjust.asp   
https://stackoverflow.com/questions/59342854/how-to-mask-input-and-display-the-last-4-digit-using-python    
https://www.codingem.com/python-how-to-ask-for-user-input/

### Task 4 Solution & References   
>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive >values of the following calculation.  
>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it >is odd, multiply it by three and add one. Have the program end if the current value is one.  

This program asks the user to input a positive number and converts it to an integer value. A while loop is used to keep repeating the loop as long as the value in number does not equal 1.
I created my own collatz function in which an if and elif statement is used to help determine whether the number inputted is even or odd.  
The if statement uses the modulus operation to check if the integer inputted is even as if the remainder equals 0, the number must be even.   
If the number is even, the indented statement runs and the number is divided by 2.  
The elif statement uses the modulus operation to check if the integer inputted is odd as if the remainder equals 1, the number must be odd.
If the number is odd, the indented statement runs and the number is multiplied by 3 and 1 is added to it.  
The while loop is used to iterate over every number until 1. When the number eventually reaches 1, the while loop will evaluate as false and will end the while loop. The result is appended to the collatz_number list.    
This set of calculations is called the Collatz Conjecture.   

***References:***   
https://www.w3schools.com/python/python_while_loops.asp  
https://www.educative.io/answers/how-to-implement-the-collatz-sequence-in-c-and-python  
https://www.pythonpool.com/collatz-sequence-python/  
https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators

### Task 5 Solution & References  
>Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)    

There are two main solutions I considered for this task. The first solution was getting the current datetime and then getting current datetime as an integer value.  
Using an if statement, if the integer value is over 5, then it is the weekend. Otherwise it is a weekday.  
However, as the weekly tasks conincided with the lab on lists and tuples, I used a different solution to demonstrate these in action.  
I used the strftime function from the imported datetime module to convert the date and time objects to a string representation and assigned it to the day_name variable.
The '%A' formatting is neccessary to ensure the output is the full weekday name.   
As tuples are ordered and unchangeable, so too are the day of the week, so tuples are appropriate to use here.  
Then, an if statement is used to determine if the day_name is in the weekday tuple. If it is, it prints out that it is a weekday.  
An else statement is used to display that it is the weekend.  

***References:***   
https://pynative.com/python-get-the-day-of-week/  
https://www.delftstack.com/howto/python/python-datetime-day-of-week/  
https://www.w3schools.com/python/python_datetime.asp  


### Task 6 Solution & References     
>Write a program that takes a positive floating-point number as input and outputs an approximation of its square >root.  
>You should create a function called <tt>sqrt</tt> that does this and should not use the built in functions x ** .5 >or math.sqrt(x).  

To complete this task, I used Newton's method for approximating the square root of a number. The user must input a positive number which is assigned the variable 'number'.    
For Netown's method, you must carry out the calculation root = 0.5 * (X + (N / X)), where N is the number for which the square root is being sought and X is the current guess of the root. Initially X is set to N. 
I defined a sqrt function with one argument i.e user inputted number. Newton's method requires a guess of the square root but this guess cannot be hardcoded.  
So, I made assigned the value of half the inputted number as the variable 'guess_sqrt'. Also, the improved guess of the square root using Newton's Method is assigned to the variable netwon_sqrt  
I used a while loop that will continue to iterate until the current guess (guess_sqrt) and improved guess (newton_sqrt) are equal.  
Within this loop, current guess (guess_sqrt) is updated to be equal to the improved guess (newton_sqrt).
Newton's Method is used to calculate an improved guess of the square root and the final guess of the square root of the inputted number is returned.
The square root of the inputted number is then displayed.  

***References:***  
https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm  
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/  

### Task 7 Solution & References  
>Write a program that reads in a text file and outputs the number of e's it contains. The program should take the >filename from an argument on the command line.  

This program reads in a text file whihc is called by the user from an arguement on the command line, not in the program itself.
Please note that the text file must be in the same directory as the program in order so that it may be called upon.   
I am making the assumption that the text file in which the letter to be counted is in, already exists in the same directory as es.py  
I am not specifying the filename as it will be passed as an argument to the function from the command line instead of being specified in the program itself.   
The sys module is imported for using argv function (sys.argv() is an array for command line arguments in python) so that the filename can be taken from the command line as an argument.    
I created my own function called count_es, which takes in one arguement i.e the filename. Within this function, the file is opened in read mode only, and the content of the file is assigned a variable.    
As per the task requirement, I used the count built in function to count the occurancces of lowercase 'e' only.  
I used the count function instead of a while loop, as the count function is generally considered more efficient for large text files.    
   
***References:***   
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/  
https://www.tutorialspoint.com/python/python_command_line_arguments.htm  
https://stackoverflow.com/questions/18647707/count-letters-in-a-text-file  

### Task 8 Solution & References  
>Write a program called plottask.py that displays: a histogram of a normal distribution of a 1000 values with a >mean of 5 & standard deviation of 2, and a plot of the function h(x)=x3 in the range [0, 10], on one set of axes.  

This program requires the numpy and matplotlib.pyplot modules to be imported.
Firstly, I created a histogram using randomly generated numbers. However, I set the seed to 1 so the   
random numbers generated will be the same each time, in order to make debuggin easier.  
The values in the brackets following the historgram set the mean, standard deviation and number of values.  
Here, an array of 1000 random numbers is created, with a mean of 5 and a standard deviation of 2.  
In addition, the function h(x)=x^3 is plotted on the same plot as the historgram, in the range 1 to 10 inclusive,  
with the y point being the cube of the x point.  
I also used various matplotlib functions such as title() and grid() to set the title, grid, style, colour, font and size. I also created a legend so the user can easily idenify the histogram and the function.  

***References:***
https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
https://www.geeksforgeeks.org/matplotlib-pyplot-xlim-in-python/
https://matplotlib.org/stable/tutorials/introductory/pyplot.html
https://www.w3schools.com/python/matplotlib_histograms.asp
https://www.w3schools.com/python/matplotlib_labels.asp