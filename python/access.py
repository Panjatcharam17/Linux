class Parent:
    def __init__(self):
        self.public_var = " I am Public"
        self._protected_var = " I am Protected"
        self.__private_var = "I am Private"
        
    def access_from_same_class(self):
        print("Inside parent class: ")
        print("Public : ", self.public_var)
        print("Protected : ", self._protected_var)
        print("Private : ", self.__private_var)
        

class Child(Parent):
    def access_from_sub_class(self):
        print("Inside child class (Subclass) : ")
        print("Public : ", self.public_var)
        print("Protected : ", self._protected_var)
        try:
            print("Private : ", self._Parent__private_var)
        except AttributeError:
            print("Private : 🔴 Cannot access ( AttributeError)")
            


class Stranger:
    def access_from_other_class(self, obj):
        print("\n Inside the Stranger class (Unrelated): ")
        print("Public : ", obj.public_var)
        print("Protected: ", obj._protected_var)  #Not recommended
        try:
            print("Private : ", obj.__private_var)
        except AttributeError:
            print("Private : 🔴 Cannot access ( AttributeError)")
            
        

#Objeect

p = Parent()
c =Child()
s=Stranger()
print("\n Access from SAME class : ")
p.access_from_same_class()

print("\n Access from SUB class : ")
c.access_from_sub_class()

print("\n Access from STRANGER class : ")
s.access_from_other_class(p)