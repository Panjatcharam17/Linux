# Create lists for different apps

playlist = ["Beliver", "Till i collapse", "Kun fuya kun" , "Tere bina"]  # Spotify

favourite_foods = ["chicken rice", "idly", "poori", "doosa"]              # Zomato

recent_locations = ["home", "Office","Walaja"]                              # Uber

print("Spotify Playlist : " , playlist)
print("Zomato foods : ", favourite_foods)
print("Uber Locations : " ,recent_locations)



#List Methods

#Append   is used to append at the last of the list

playlist.append("Aval ")
print("After append : ", playlist)


#insert

playlist.insert(1,"Your Eyes")
print("After insert : ", playlist)

# Remove

playlist.remove("Your Eyes")
print("After Removing : ", playlist)

#Pop
#it will remove the last element in the list

playlist.pop()
print("After POP: ", playlist)


#reverse

playlist.reverse()
print("After reverse : ", playlist)

#count 


# It will count the number of times the word occurs

print("count : ", playlist.count("Beliver"))


#..............................................................................................................................................................................#


#List slicing


print("Top 2 songs : ",playlist[0:2])  # it will take 0 and 1 only (2 element    only it will take)

print("Last 2 songs : ", playlist[-2:])  # it will show the last two element

#List Iteration:


for food in favourite_foods:
    print("All foods  : ", food)
for song in playlist:
    print(song+" - By Gowtham")
    
    
# check if

if "doosa" in favourite_foods:
    print("yes")
    
    
#Change the list element

favourite_foods[1]="Idiyappam"
print("Updated favourite_foods : ",favourite_foods)

mixed = ["Panjatcharam" , 23 ,180]

for a in mixed:
    print(a)
    
# to get the index locations

for i, locations in enumerate(recent_locations):
    print(f"locations {1} : {locations}")
        
        
