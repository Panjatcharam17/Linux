delivery_partner="Swiggy"

def hotel():
    item="Pizza"

    def order_now():
        quantity=2
        print(f"Ordering Item {quantity} {item} using {delivery_partner}")
    order_now()
hotel()
