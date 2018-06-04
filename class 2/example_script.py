#! /usr/bin/env python

# This script will perform all the calculations we have done in class at once
# It will also highlight some of the things you will learn to do by the end of the class

#this is how you can import packages that hold useful functions -- will be explained further
import math
import timeit

#DEFINE USER FUNCTIONS

#this is a function. When called in the script it will be run
def perform_math(starting_number):
    num = starting_number*9
    
    #this is a while loop and a control statement
    while (num >= 10):
        #creating a string and then splitting it
        mm = list(str(num))
        num = 0
        for num_pos in mm :
            num = num + int(num_pos)
            #End of the "nested" loop
    #end of the first loop
    
    num = num-5
    
    return num

#MAIN SCRIPT

start_time = timeit.default_timer()

#we will first open up a file for reading that is full of numbers
num_file = open("ingredients_file.txt", "r")

#open up a file to write out the results
out_file = open("results_file.txt", "w")

#I have put the contents of the file into what is called an array
numbers = num_file.readlines()

#This is called a loop. This is how we can get every number in the file
for i in range(len(numbers) ):
    
    single_number = int(numbers[i]) #I am going through each number and making sure it is a number
    
    #I am performing the math on that number and setting the result to a new variable
    new_output = perform_math(single_number)
    
    #I am writing out the final output plus a new line character
    out_file.write(str(new_output) + "\n")

#Closing up the files
out_file.close
num_file.close

elapsed = timeit.default_timer() - start_time

print 'The time spent running the script is', elapsed, 'seconds'