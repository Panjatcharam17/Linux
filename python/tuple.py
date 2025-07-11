trip_summary = ("Ozhugur", "Walaja", "Kanchipuram","sunguvarchatram")
print(trip_summary)

print(trip_summary[1])

for item in trip_summary:
    print(item)
    
print(len(trip_summary))

print(trip_summary.count("Walaja"))

print(trip_summary.index("Walaja"))


trip_summary[1] = "Chennai"
print(trip_summary)  # it will show the error that tuple is immutable