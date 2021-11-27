
#. Lets define a List  []

fruits = ['Apple','Orange',"Grapes","PineApple"]


print(fruits)

#1. Function defination


def printFruitsName(fn): # fn is a formal arguments

    for x in fn: # you can iterate over a List
        print('I like '+x)

#2. Function Calling
printFruitsName(fruits) # Actual Arguements
