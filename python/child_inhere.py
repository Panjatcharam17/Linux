from dad import dad


class son(dad):
    
    def factory(self):
        print("white colour paint for the factory")
        
    def house(self):
        print("Green colour paint for the house")  # we can change the dad class value 
            
s = son()
s.factory()
s.house()