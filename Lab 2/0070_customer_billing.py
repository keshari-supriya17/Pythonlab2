
customer_name = input("Enter the Customer Name :")
membership_type = input("Enter the Membership type (Regular/Premium/VIP):")
purchase_amount = int(input("Enter the purchages amount :"))

if purchase_amount < 1000:
    discount = 0
elif purchase_amount < 5000:
    discount = 5
elif purchase_amount < 10000:
    discount = 10
else:
    discount = 15

if membership_type.lower() == "premium":
    discount += 5
elif membership_type.lower() == "vip":
    discount += 10
else:
    discount = discount

if discount > 25:
    discount = 25

discount_amount = purchase_amount * discount / 100
final_amount = purchase_amount - discount_amount

print("\n--- CUSTOMER BILL ---")
print("Customer:", customer_name)
print("Membership:", membership_type)
print("Original Amount: ₹", purchase_amount)
print("Final Discount:", discount, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Payable Amount: ₹", final_amount)