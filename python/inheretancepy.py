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

#Inheretance example 2(Multi level inhertance)
"""
class dad:
    def house(self):
        print("Dad has a house")
        
class son1(dad):
    def factory(self):
        print("Son1 has a factory")
        
class son2(dad):
    def market(self):
        print("Son2 has a market")
        
g=son1()  # son1 has  house and factory only he cannot access the market
g.house()
g.factory()

v=son2()  #son2 has house and market only he cannot acces the factory
v.house()
v.market()
"""

#Multiple inhertance

class dad:
    def house(self):
        print("Dad has a house")
class mom:
    def shop(self):
        print("flower shop")
        
class son(dad, mom):   #multiple inhertance now we can access the house and shop
    def factory(self):
        print("Son1 has a factory")
        
s=son()
s.factory()
s.house()
s.shop()

"""
Multiple inhertance
A
B 
C(A,B)

Multi level inhertance

A
B(A)
C(B)
"""
