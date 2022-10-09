# You need to use pi (3.14) r^2 to calcualte a cirlce area 


pi = 3.14
result = 0
radius = -1

# get the user input using input() :::::: reference -> https://www.pythonforbeginners.com/basics/how-to-take-user-input-in-python#:~:text=We%20can%20use%20the%20input%28%29%20method%20to%20take,value%20entered%20by%20the%20user%20as%20a%20string.

radius = input("Enter radius number")

# do calculations and set the result variable to it

result = (pi * int(radius) ** 2)

# print results back to the user

print (result)
