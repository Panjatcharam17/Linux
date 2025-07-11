#using list
favourite_cities = ["ozhugur", "Kanchipuram", "chennai"]

unique_cities=set(favourite_cities)  # set keyword in used to change the list to set
print(unique_cities)


#Set  {} 

uber_cities1 = {"chennai","mumbai", "vellore"}
uber_cities2 = {"banglore", "chennai","ozhugur"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))  # intersection means it will show the common for both the sets

print(uber_cities1.difference(uber_cities2))  # it will show the mumbai and vellore only because chennai common for both

uber_cities1.add("Koomapatti")
print(uber_cities1)

uber_cities1.remove("chennai")
print(uber_cities1)

#print(uber_cities1[1])  # it will show the error

my_set={1,2,3}
my_set.remove(2)
my_set.add(99)

print(my_set)

# to remove it safely

my_set.discard(3)
print(my_set)