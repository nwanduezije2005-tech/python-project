# SmartPlate Project
# Ezije Nwandu
# Purpose: Automate plate tracking and billing
# for conveyor belt sushi restaurants

print("===================================")
print("      Welcome to SmartPlate!")
print("===================================")

total = 0
plate_count = 0

while True:

    item = input("\nEnter sushi plate name (or type 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input("Enter plate price: $"))

    total += price
    plate_count += 1

    print(f"{item} added successfully!")
    print(f"Current Total: ${total:.2f}")

# Tax calculation
tax = total * 0.08
final_total = total + tax

# Receipt
print("\n===================================")
print("         SMARTPLATE RECEIPT")
print("===================================")

print(f"Total Plates: {plate_count}")
print(f"Subtotal: ${total:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")

print("\nThank you for using SmartPlate!")
print("Have a great day!")
