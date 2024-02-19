print(type("hello")) #prints the type of the variable

x=1
print(type(x))

def hello():
    print("hello")

print(type(hello)) #to print the class of the function hello

y = "hello"
#print (x+y) #this is wrong since addition not defined between the class string and integer

string = "hello"
print(string.upper()) #upper is the method acting on the object which is "string"

class Dog: #creating your own class

    def __init__(self,name,age):
        self.name = name #name is the attribute of the class dog
        self.age = age
        print (name)
        print(self.age)
    
    def get_name (self):
        return self.name
    
    def set_age (self, age): #modifying the attribute
        self.age = age
    
    def get_age(self):
        return self.age

    def bark(self):         #defining methods
        print("bark")
    
    def add_one(self, x):
        return(x+1)
    
    

#d = Dog() #instantiating the object of class Dog
#print(type(d))
#d.bark()
#print(d.add_one(5))

d = Dog ("Tim", 17)
d.set_age(23)
print(d.name)
print(d.get_name())
print(d.get_age())


d1 = Dog("Bill", 20)
print(d1.name)
print(d1.get_name())
print(d1.get_age())


#interaction between multiple classes =>

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    

class Course: 

    def __init__(self, name, max_students): #add students in the course => but how will we have students stored in a course object
        self.name = name
        self.max_students = max_students
        self.students = [] #made an empty list 

    def add_student(self , student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_avg_grade(self):
        sum = 0 
        for student in self.students:
            sum = sum + student.get_grade()

        return sum/len(self.students)

    
s1 = Student("Hafsa" ,22, 65)
s2 = Student ("Ali", 23, 56)
s3 = Student ("Sara", 76, 95)

course = Course("Math" , 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.students)
print(course.students[1].name)
print(course.get_avg_grade())


#Inheritance Concept

class Inherit_class:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and {self.age} years")
    
    def speak(self):
        print("I really dont know")


class Cat(Inherit_class):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and {self.age} years and my color is {self.color}")


class Dog(Inherit_class):

    def speak(self):
        print("Bark")

i = Inherit_class("Tim" ,19)
i.show()
i.speak()

c = Cat("Bill" ,34, "brown")
c.show()
c.speak()    #will not print what is defined in the parent class but will print what is defined in the cat class itself

d = Dog("Doggy" ,78)
d.show()
d.speak()


#Class Attributes => attributes that are specific to the class not to an instance or object of that class 

class Person:

    no_of_people = 0 #not specific to the instance of the Person class. Will stay same for each object created

    def __init__(self, name):
        self.name = name
        Person.no_of_people += 1 #to keep track of how many instances we have created of the Person class
        Person.add_people()

    @classmethod #decorator method to specify that this method is the class method
    def no_of_people_(cls):
        return cls.no_of_people
    
    @classmethod
    def add_people(cls):
        cls.no_of_people += 1


p1 = Person("Ahmed")
print(Person.no_of_people)
p2 = Person("Jill")
print(Person.no_of_people)

print(p1.no_of_people)
print(Person.no_of_people) #since no_of_people is not secific to the instance of the class

Person.no_of_people = 8
print(p2.no_of_people)

print(Person.no_of_people_())

#Static Methods

class Math:

    @staticmethod 
    def add5(x):
        return x+5

#Now no need to create the instance of the class Math inorder to call the add5 method

print(Math.add5(5))







    

