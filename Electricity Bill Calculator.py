def calculate_bill(kwh):
    basic_charge = 50
    total = 0
    if kwh <= 100:
        total = kwh * 5
    elif kwh <= 200:
        total = (100 * 5) + ((kwh - 100) * 7)
    elif kwh <= 500:
        total = (100 * 5) + (100 * 7) + ((kwh - 200) * 10)
    else:
        total = (100 * 5) + (100 * 7) + (300 * 10) + ((kwh - 500) * 12) + 500  # ₱500 surcharge
    total += basic_charge
    return total
kwh_used = float(input("Enter the number of kilowatt-hours used: "))
bill = calculate_bill(kwh_used)
print(f"Total Electricity Bill: ₱{bill:,.2f}")



