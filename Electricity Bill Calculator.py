# Function to calculate electricity bill (cumulative tiered system)
def calculate_bill(kwh):
    basic_charge = 50   # fixed basic charge
    surcharge = 0
    total = 0

    # Tiered (cumulative) calculation
    if kwh <= 100:
        total = kwh * 5
    elif kwh <= 200:
        total = (100 * 5) + ((kwh - 100) * 7)
    elif kwh <= 500:
        total = (100 * 5) + (100 * 7) + ((kwh - 200) * 10)
    else:
        # above 500: compute first 500 then remaining at 12 + ₱500 surcharge
        total = (100 * 5) + (100 * 7) + (300 * 10) + ((kwh - 500) * 12)
        surcharge = 500

    total += basic_charge + surcharge
    return total


# --- Main ---
try:
    kwh_used = float(input("Enter the number of kilowatt-hours used: "))
    if kwh_used < 0:
        print("Please enter a non-negative number.")
    else:
        bill = calculate_bill(kwh_used)
        print(f"Total Electricity Bill: ₱{bill:,.2f}")
except ValueError:
    print("Invalid input. Please enter a number.")

