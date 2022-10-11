# in this one you will practice string manipulation. 
# string manipulation is when you manipulate a string :D 
# this could be to combine strings into one string : "james" and " marshall" into "james marshall"
    # this is called concatination. You can use the + opperator to combine strings. 
    # fullname = "james" + " marshall"
    # 

# it could also replace part of the string with other strings: "james is the cool" -> "james is the coolest"
    # this is called replacing you can use the variable.replace() function to replace parts of a string
    # fullname = "james is the cool"
    # replaced = fullname.replace("cool", "coolest")

# you can also split strings -> "james philip" -> "james", "philip"
    # this is called splitting, you can use the variable.split() function to split strings. 
    # fullname =  "james philip" 
    # splitnames = fullname.split(" ")


# now ask the user for their full name and their age.

username = input("Enter fullname and age. For Example: Juan Carpinteyro 27 ")

# ask them for a comma seperated list of three of their family members firstnames and their ages (like this : philip 22, james 24, sarah 100)

family_information = input("Enter a list 3 of Family members and their ages separted by commas like: Juan 4, Michael 2, Christina 1 ")

# print out "welcome " + username + "."

print ("Welcome " + username + ".")

# print out the family information split by the ","

print (family_information)

# print out the family information split by the " "

print (family_information.replace(",", " "))

# tell the user what their full name would be if they changed their last name to "salmon"

username2 = username.split(" ")
username2.pop(1)
username2.insert(1, "Salmon")
print (username2[0] + " " + username2[1] + " " + username2[2])

# strip away all the "," in the family informaiton and print it out.

print (family_information.replace(",", " "))
