dis = int(input("Enter distance traveled (in kilometers):"))
fuel_consumed = int(input("Enter fuel consumed (in liters):"))

def calculate_fuel_efficiency():
    global dis, fuel_consumed
    fuel_efficiency = dis / fuel_consumed
    return fuel_efficiency

print("Fuel efficiency:" , calculate_fuel_efficiency(), "km/l")