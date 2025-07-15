"""
class Student:  # class startswith class keyword
    def say_hello(self):   #we need to set self must
        print("Hi, I'm a student!")

s1 = Student()    #s1 it is a object
s1.say_hello()     #s1.say_hello(s1)

""" 
#constructor
"""
class Student:
    def __init__(self , name, grade):  # if we do not use __init__ (constructor)means it will show the error
        self.name = name
        self.grade = grade
        
    def display(self):
         print(f"{self.name} is in grade {self.grade}")
         
#multiple object
s1 = Student("Panja", 10)
s2 = Student("Perumal", 20)
s3 = Student("Panji", 30)

s1.display() # Panja is in grade 1
s2.display()
s3.display()      

"""
#constructor example 2

class Employee:
    def __init__(self, name, aadhar):  #it will give the data to all the class
        self.name=name        #stored once
        self.aadhar=aadhar    #stored once
        
    def enter_office(self):
        print(f"{self.name } enters using Aadhar {self.aadhar}.")
        
    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with aadhar {self.aadhar}.")
        
emp1=Employee("Panja","1234-5678-9012")
emp1.enter_office()
emp1.open_bank_account()
