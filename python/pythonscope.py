# L -> E -> G -> B


#Local

def order():
    food="Chicken Rice"
    print("Your order is :",food)
order()

#print(food)

#Enclosure

def card():
    discount=10

    def checkout():
        print("Applying discount : ",discount)
    checkout()
card()

#Global

user_id="panja17"

def homepage():
    print("Welcome : ",user_id)

def profile():
    print("Welcome to the profile page : " , user_id)
homepage()
profile()

#Builtin

print(__file__)
