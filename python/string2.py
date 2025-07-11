driver_name = "Panjatcharam L"

mobile = "9790175171"

masked = mobile[:2] + "******"+mobile[-2:]
print(masked)

song = "Shape of you"
artist = "Ed shreeen"
formatted = f"{song.title()} - {artist.title()}"
print(formatted)

location = "Chennai central"
fixed_location = location.replace("Chennai central","Thambaram")
print(fixed_location)


message = "Your uber booking id is :UB12345, Please keep it safe"
booking_id=message.split(":")[1].split(",")[0]
print(booking_id)


promo_msg="Use zomoto100 to get 100 offer on the first order"
if "zomoto100" in promo_msg:
    print("Offer Applied")

feedback = "The Driver was polite and the ride was smooth"
print("Position is :", feedback.find("polite"))

name = "Panjatcharam Loganathan"
initial = "".join([word[0].upper() for word in name.split()])  #to get the first letter of the names
print(initial)


dirty_input = "        airport"  # name with more spaces
clean_input = dirty_input.strip()
print(clean_input)


word1 = "the tripp was amazing and the car was clean"

word_count = len(word1.split())  # it wiil show the word count  with the split we can use it as a delimitter like and and other words also
print(word_count)

