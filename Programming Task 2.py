distance = int(input("Enter distance in kilometers:"))
rate_per_km = int(input("Enter rate per kilometer:"))


def calculate_delivery_fee():
    global distance, rate_per_km
    delivery_fee = distance * rate_per_km
    return delivery_fee

total_fee = calculate_delivery_fee()
print("Total delivery fee: ₱", total_fee)


