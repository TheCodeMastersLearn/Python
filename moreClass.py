# You will get more practice with the class here. 
# This will seem redundant but it is to prove why using class to their full potential is so good. 
# Lets say that you want to create an object that represents people. it could be your boss, or family. Doesnt matter.
# you would probably call it "person" right?
# you now have to give this person methods that represent what they do. So add a makesound() method that returns a string "hello"
# People do things like watch furry videos. 
# but not everyone watches furry videos. 
# juan watches furry videos but james does not. 
# so you can see now we need to either list all the different activities as values inside the person class and set them when we create a person object
# or we can create another class called furry which still has many of the same data as a person since they are still people
# 
# So a furry will probably make the sounds of the animal they furry for (maybe? i actually dont know if they mew or whatever.)
# so now you have to determine the type of sound a furry will make and make the makesound() return "mew"

# do you see the tons of overlap code? furries and people have names so you will have to add those both to both new class
# furries and people have an age so you will have to add that as well
# furries and people both have parents... 
# the list goes on and on and on and on and on furries are remarkably like people. just disgusting and weird 
# 
# this is tons of work and thats just for a furry... what if we wanted to add races or ethnicity.
# then we would have to write even more repeat code for those class... a black person, a white person, an asian, .... 
# it goes on and on and on and on. So basically everytime you want to expand on this you have to write alot more. 
# also lets say you want to change it so all people also have a nickname. 
# Oh boy now we have to go to each of these class and add a nickname field.
# Not only that but lets say you have a simulator that takes on of these people class and then simulates them based on what you filled them out to be like
# for example it makes them mew if they are a furry or say america if they are white. 
# now you have to change a bunch of code there to accept more class is you add more types of people.
# you see how it is a huge problem when we want to create class for similar things? they are so similar but we have to write so much 
# for each of them. 

# this is where inheritance is HUGE and it is easy to understand because it is exactly how it sounds. 
# you can make a class inherit from another class. This will make it so the class that is inheriting gets all the attributes and methods 
# that the parent class has.
# so if person class has "name, age, mother, and father"
# and furry class inherits from the person class. 
# then furry class will also have "name, age, mother, and father" without you needing to write anything
# You can then add new things specific to furries like a watchFurryVideo() method. or animalSound = "woof"
#
# now you created a new class that has everything person has but with the things that a furry has as well. 
# 
# you can also add races that inherit from the person class. and any other person type can inherit from it as well. 
# you can go multiple layers down and do a person class and a man class that inherits from the person class and a furry that inherits from the man class. 
#
# This solves the tons of repeat code and the trouble of expanding the people types in the future. 

# there are some other more advanced things that this helps tons as well but that will be for later. 

# so create a person class that has any attributes or methods you think it should have. 

from cgi import print_arguments


class person:
    
    #######################
    # Constructor: __init__
    #
    # Parameters: 
    # gender: string, height: float, hair_color: string, weight: float, eye_color: string, age: int)
    #
    # comments
    # This is the constructor.
    ######################
    def __init__(self, gender, height, hair_color, weight, eye_color, age):
        self.gender = gender
        self.height = height
        self.hair_color = hair_color
        self.weight = weight
        self.eye_color = eye_color
        self.age = age

    #######################
    # Method Name: get_gender
    # 
    # Return Type: String
    #
    # comments
    # This will get gender from the class.
    ######################
    def get_gender(self):
        return self.gender

    #######################
    # Method Name: get_height
    # 
    # Return Type: String
    #
    # comments
    # This will get height from the class.
    ######################
    def get_height(self):
        return self.height

    #######################
    # Method Name: get_hair_color
    # 
    # Return Type: String
    #
    # comments
    # This will get hair_color from the class.
    ######################
    def get_hair_color(self):
        return self.hair_color

    #######################
    # Method Name: get_weight
    # 
    # Return Type: float
    #
    # comments
    # This will get weight from the class.
    ######################
    def get_weight(self):
        return self.weight

    #######################
    # Method Name: get_eye_color
    # 
    # Return Type: String
    #
    # comments
    # This will get eye_color from the class.
    ######################
    def get_eye_color(self):
        return self.eye_color

    #######################
    # Method Name: get_age
    # 
    # Return Type: int
    #
    # comments
    # This will get age from the class.
    ######################
    def get_age(self):
        return self.age

    #######################
    # Method Name: set_gender
    # 
    # Return Type: String
    #
    # comments
    # This will set gender in the class.
    ######################
    def set_gender(self, gender):
        self.gender = gender

    #######################
    # Method Name: set_height
    # 
    # Return Type: String
    #
    # comments
    # This will set height in the class.
    ######################
    def set_height(self, height):
        self.height = height

    #######################
    # Method Name: set_hair_color
    # 
    # Return Type: String
    #
    # comments
    # This will set hair_color in the class.
    ######################
    def set_hair_color(self, hair_color):
        self.hair_color = hair_color

    #######################
    # Method Name: set_weight
    # 
    # Return Type: float
    #
    # comments
    # This will set weight in the class.
    ######################
    def set_weight(self, weight):
        self.weight = weight

    #######################
    # Method Name: set_eye_color
    # 
    # Return Type: String
    #
    # comments
    # This will set eye_color in the class.
    ######################
    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

    #######################
    # Method Name: set_age
    # 
    # Return Type: int
    #
    # comments
    # This will set age in the class.
    ######################
    def set_age(self, age):
        self.age = age

    #######################
    # Method Name: make_sound
    # 
    # Return Type: String
    #
    # comments
    # This will print "Hi." to the terminal.
    ######################
    def make_sound():
        print ("Hi.")

class businessman(person):
  
    #######################
    # Constructor: __init__
    #
    # Parameters: 
    # gender: string, height: float, hair_color: string, weight: float, eye_color: string, age: int
    # educatiion: string, last_job: string, salary: float, years_of_exp: int
    #
    # comments
    # This is the constructor.
    ######################
    def __init__(self, gender, height, hair_color, weight, eye_color, age, educatiion, last_job, salary, years_of_exp):
        super().__init__(gender, height, hair_color, weight, eye_color, age)
        self.education = educatiion
        self.last_job = last_job
        self.salary = salary
        self.years_of_exp = years_of_exp

    #######################
    # Method Name: get_education
    # 
    # Return Type: String
    #
    # comments
    # This will get education from the class.
    ######################
    def get_education(self):
        return self.education

    #######################
    # Method Name: get_last_job
    # 
    # Return Type: String
    #
    # comments
    # This will get last_job from the class.
    ######################
    def get_last_job(self):
        return self.last_job

    #######################
    # Method Name: get_salary
    # 
    # Return Type: float
    #
    # comments
    # This will get salary from the class.
    ######################
    def get_salary(self):
        return self.salary

    #######################
    # Method Name: get_years_of_exp
    # 
    # Return Type: int
    #
    # comments
    # This will get years_of_exp from the class.
    ######################
    def get_years_of_exp(self):
        return self.years_of_exp

    #######################
    # Method Name: set_education
    # 
    # Return Type: String
    #
    # comments
    # This will set education in the class.
    ######################
    def set_education(self, education):
        self.education = education

    #######################
    # Method Name: set_last_job
    # 
    # Return Type: String
    #
    # comments
    # This will set last_job in the class.
    ######################
    def set_last_job(self, last_job):
        self.last_job = last_job

    #######################
    # Method Name: set_salary
    # 
    # Return Type: float
    #
    # comments
    # This will set salary in the class.
    ######################
    def set_salary(self, salary):
        self.salary = salary

    #######################
    # Method Name: set_years_of_exp
    # 
    # Return Type: int
    #
    # comments
    # This will set years_of_exp in the class.
    ######################
    def set_years_of_exp(self, years_of_exp):
        self.years_of_exp = years_of_exp

    #######################
    # Method Name: professional_speak
    # 
    # Return Type: String
    #
    # comments
    # This will print "Greetings" to the terminal.
    ######################
    def professional_speak():
        print ("Greetings")

philip = businessman("Male", str("5'8\" "), "brown", 210, "brown", 22, "Some college", "Jimmy Johns", 25000, 2)
sarah = person("Female", str("5'4\" "), "brown", 130, "brown", 27)
james = businessman("male", str("5'10\" "), "brown", 200, "brown", 24, "Some college", "Cresco", 56160, str(">1"))

if james.get_weight() > sarah.get_weight():
    print ("James is fatter than Sarah")
else:
    print ("You messed up.")

if james.get_weight() > philip.get_weight():
    print ("James you need to hit the gym.")
else:
    print ("Philip you need to hit the gym.")

if james.get_age() > 20 and philip.get_age() > 20:
    print ("You guys are getting so old.")
else:
    print ("You messed up.")    

# and now create a buisnessman class that inherits from the person class. Give him some things that is specific to buisnessmen:
# like a suit attribute that you can set the color of. 
# a company attribute which states where he works
# etc

# you inherit from class in python by in the class definition adding parenthesees with the parent class in it. 
# EX: class businessman(Person):
#           ......



# read this link, it talks about constructors which is good to know about 
# https://www.programiz.com/python-programming/inheritance#:~:text=Inheritance%20in%20Python.%20Inheritance%20is%20a%20powerful%20feature,inherits%20is%20called%20the%20base%20%28or%20parent%29%20class.
