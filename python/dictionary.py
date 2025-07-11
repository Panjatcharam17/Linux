#Dictionary
"""
trip = {
    "trip_id" : "UB12345:",
    "pickup" : "Ozhugur",
    "drop" : ["Kanchipuram", "Walaja", "Chennai"],
    "fare" : 200,
    "driver" : "Ram",
    "Status" : "Completed",
    "trip_id" : "UB123456"
}

print(trip["pickup"])   # it will take it as a key 
print(trip.get("Ozhugur"))

print(trip.keys())
print(trip.values())


for key, value in trip.items():  # to iterate through the dictionary
    print(key, ":", value)
    
trip.update({"car_mode" : "Audi"})  # it will check the key is availabe it will update the value if not availble means it will add key and value
print(trip)

trip.pop("Status")
print(trip)

#duplicate check

for k, v in trip.items():  # here it will take the updated trip_id UB123456 as output it will omit the first id
    print(k, ":",v)

print(trip["drop"][1])  # it will take the particular elements

for location in trip["drop"]:
    print(location)

"""


#Multiple dictionary
"""
#two ways by one using list 
trips = [
    {"trip_id" : "UB01", "pickup" : "chennai", "drop" : "home", "fare" : "500"},
    {"trip_id" : "UB02", "pickup" : "kanchipuram", "drop" : "walaja", "fare" : "200"},
    {"trip_id" : "UB03", "pickup" : "chennai", "drop" : "banglore", "fare" : "600"}
]

for trip in trips:
    print(trip["trip_id"])    
    
"""
#two ways by one using it as dictionary
trips = {
    "UB01": {"trip_id" : "UB01", "pickup" : "chennai", "drop" : "home", "fare" : "500"},
    "UB02": {"trip_id" : "UB02", "pickup" : "kanchipuram", "drop" : "walaja", "fare" : "200"},
    "UB03": {"trip_id" : "UB03", "pickup" : "chennai", "drop" : "banglore", "fare" : "600"}
}

print("UB01 Fare", trips["UB01"]["fare"])

for    trip_id,details in trips.items():
    print(trip_id)
    print(details["pickup"],"-->", details["drop"])