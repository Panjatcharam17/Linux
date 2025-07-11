items = []

while True:
    item = input("Add items to your cart (Type 'done to finish) : ")
    if item.lower() == "done" :
        break
        
    items.append(item)
    
print("Items in cart : ", items)