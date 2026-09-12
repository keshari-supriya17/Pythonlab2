 
customer_name = input("Enter the customer name : ")
purchase_amount = float(input("Enter the Purchase amount : "))
if purchase_amount < 1000:
    discount_rate = 0
elif purchase_amount < 5000:
    
    discount_rate = 5
elif purchase_amount < 10000:
    discount_rate = 10
else:
    discount_rate = 15         
    discount_amount = purchase_amount * discount_rate / 100
    final_amount = purchase_amount - discount_amount 
    
print("Customer Name:", customer_name)
print("Purchase Amount: ₹", purchase_amount)
print("Discount:", discount_rate, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount: ₹", final_amount)