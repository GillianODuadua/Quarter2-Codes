
print("Please enter your 5 travel destinations:")
destinations = []

for i in range(5):
    place = input(f"Destination {i + 1}: ")
    destinations.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")

print("\nLet's update your 2nd and 5th destinations.")

new2 = input("Enter a new destination for position 2: ")
destinations[1] = new2

new5 = input("Enter a new destination for position 5: ")
destinations[4] = new5


print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")
