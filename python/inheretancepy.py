#Inheretance 
"""
class dad:   
    
    def house(self):  #parent
        print("I am from dad class ")
     
class son(dad) :   #child
    
    def factory(self):
        print("I am from factory class")
        
    
s = son()  # by using son class we can access the dad class that is inhertance
s.house()
s.factory()
"""
"""
#example

class app1 :  # parent
    def v1(self):
        print("Orders")

class   app1_1(app1):   #child
    def v2(self):
        print("refund")
        
    def v1(self):           # To override the parent class data
        print("Cart")      # order  will not show cart only show becuase we called the same function v1 and changed it
            
a = app1_1()
a.v1()
a.v2()   
"""

#Inheretance example 2

