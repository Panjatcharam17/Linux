from abc import ABC, abstractmethod

#Architect define the plan

class FeaturePlan(ABC):
    @abstractmethod   
    def login(self):
        pass
        
        
    @abstractmethod
    def logout(self):
        pass
    
    def checkout(self):  #it is not a abstract mehtod  we can use non abstract method 
        pass
        
#Developer implementation
        
class Webapp(FeaturePlan):
    
    def login(self):
        print("Webapp login done ")
        """
    def logout(self):
        print("Webapp logout done")
       """
     
#Team lead checks functionality
app=Webapp()
app.login()
app.logout()