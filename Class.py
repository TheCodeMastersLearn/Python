# A class is a way to create your own datatypes ( int, string, list, ...)
# This is the cornerstone of OOP (object oriented programming)
# you can think of creating one as creating a blueprint for your datatype 
# class can contain two categories
#       - Data in the form of datatypes (ints, strings, ...)
#       - Sub programs called methods. 
#           - these subprograms are basically bits of code that you can use. 
# This is where alot of programming principals shine. 
# one example is when a programming language has great orthogonality 
#       - othogonality is that thing where two 'things' are completely different from each other but can be combined to make a huge 
#           variety of things. 
#       - in math the x-axis and y-axis are orthogonal and they can create any point in the x and y plane
# another programming principle is maintainability
#       - Class shine when you look at massive programs and they are being used in multiple parts of that program. 
#       - an example of a class being used in multiple parts of a program is the window you are currently using. 
#           - this window is the same class as the window you pull up when you open your browser for Furry images. 
#           - it is also the same class that is used to open up your file explorer
#       - As you can imagine when the first window class was created it probably did not have all the features it has now. 
#       - over time as it got used for more purposes developers expanded on it
#           - if the windows class was made with maintnance in mind it made the future developers jobs alot easier
# there are more but you get the idea.
#
# now those two categories are extreamly powerful. 
# I will use psuedocode on a class and you can look online how to actually create a class for python. 
# 
# class family:
#   brothers = []
#   sisters = []
#   you = ""
#   
#   def __init__(self, brothers, sisters, you):
#       self.brothers = brothers
#       self.sisters = sisters
#       self.you = you
#
#   def printFamily(self):
#       for brother in brothers:
#           print(brother)
#       for sister in sisters:
#           print(sister)
#       print(you)
#
# this is a simple class that allows you to store family names and print them out calling the class member printFamily()
# so in order to use this class you need to initialize it. 
# there are two special methods in class, they are the constructor and destructor. 
#   The constructor you can see here __init__class(self, parameters)
#   all methods take self since it is the object referencing it's self. 
#   you usually create a constructor to send preliminary data to the object once it is created. 

# remember a class is a blueprint on how to create an object. It has not been created yet in our program until we use the blueprint to create it. 
# so in our program we will type the following:
# brothers = ["philip", "man", "big salmon"]
# sisters = ["sarah", "little salmon", "no"]
# you = "juan"
# jamesFamily = family(brothers, sisters, you)
# jamesFamily.printFamily()
# 
# now you will see that this will print out all the family. 
# create a class that adds, subtracts, and divides. 
# HINT: you dont need both of these chategories, you dont need datatypes if all you need are methods. 




# class
class math:
    def add(self, num1, num2):
        if self.validate_numbers(num1, num2) == False:
            return -1
        sum = num1 + num2 
        return sum
    def subtract(self, num1, num2):
        if self.validate_numbers(num1, num2) == False:
            return -1
        difference = num1 - num2 
        return difference
    def divide(self, num1, num2):
        if self.validate_numbers(num1, num2) == False:
            return -1
        quotient = num1 / num2 
        return quotient  
    def multiply(self, num1, num2):
        if self.validate_numbers(num1, num2) == False:
            return -1
        product = num1 * num2 
        return product       
    def validate_numbers(self, num1, num2):
        if (type(num1) == float or type(num1) == int) and (type(num2) == float or type(num2) == int):
            return True
        else:
            return False
calculator = math()
print ("Welcome to JuanTonSuey's most excellent calculator. I can Add, Subtract, Multiply and Divide. \
 Be sure to enter your question correctly for Example: Multiply 2 and 3; Divide 22 by 2; Subtract 10 by 1; Add 2 and 4")
question = input("Ask me to do Math. ")
question = question.lower()
question = question.split(" ")
if question[0] == "multiply":
    x1 = (calculator.multiply(float(question[1]),float(question[3])))
    if x1 % 2 == 0:
        print ("The Product is " + str(x1) + ". The answer is even.")
    else:
        print ("The Product is " + str(x1) + ". The answer is odd.")
elif question[0] == "divide":
    x1 = (calculator.divide(float(question[1]),float(question[3])))
    if x1 % 2 == 0:
        print ("The Quotient is " + str(x1) + ". The answer is even.")
    else:
        print ("The Quotient is " + str(x1) + ". The answer is odd.")
elif question[0] == "add":
    x1 = (calculator.add(float(question[1]),float(question[3])))
    if x1 % 2 == 0:
        print ("The Sum is " + str(x1) + ". The answer is even.")
    else:
        print ("The Sum is " + str(x1) + ". The answer is odd.")
elif question[0] == "subtract":
    x1 = (calculator.subtract(float(question[1]),float(question[3])))
    if x1 % 2 == 0:
        print ("The Difference is " + str(x1) + ". The answer is even.")
    else:
        print ("The Difference is " + str(x1) + ". The answer is odd.")                
else:
    print ("Did you spell everything correct?")

# init (constructor)

# add(self, num1, num2)

# minus(self, num1, num2)

# divide(self, num1, num2)