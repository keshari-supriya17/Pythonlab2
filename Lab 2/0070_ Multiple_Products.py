Number_of_products = int(input("Enter number of products: "))

Total = 0

for i in range(Number_of_products):
    price = float(input(f"Enter price of product {i + 1}: ₹"))
    Total = Total + price

if Total < 1000:
    discount_rate = 0
elif Total < 5000:
    discount_rate = 5
elif Total < 10000:
    discount_rate = 10
else:
    discount_rate = 15

discount_amount = Total * discount_rate / 100
final_amount = Total - discount_amount

print(" BILL SUMMARY ---")
print("Total Amount: ₹", Total)
print("Discount:", discount_rate, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount: ₹", final_amount)