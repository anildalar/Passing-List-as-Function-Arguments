

#1. Define the Class

x=10








class MyClass:
    # Note :- There are 3 Members of a class
    # 1. Property
    # Property are variables
    x = 40 # Property
    y = 30
    fullname=""
    address = ''

    # 2. Constructor
    # Constructor is a function
    def __init__(self,addr):
        # The role of constructor is to initiazlize the members
        # object.member
        # self.member
        self.address = addr
        self.fullname = 'ANIL DOLLOR'



    # 3. Method
      
    def anil(self,mystudent):
        print('Hello from anil method')
        print(f' {mystudent} is my python student')
        print(f' My Address is { self.address } ')


#2. Create the object from the Class
# objectName = ClassName()
object = MyClass('Neemuch')

#how we can access the members
# dot . is a member selection operator

#object.member

print(object.fullname)
# Variable substitution / String Interpolation
print(f'The Sum of x and y is {(object.x + object.y)} ')

# Call the anil method of MyClass

object.anil("Swapnil")

# self is the reference of current classs