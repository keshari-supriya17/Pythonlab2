Product_name = input("Enter the Product Name  :")
Current_stock = int(input("Enter the Current Stock :"))
Reorder_level = int(input("Enter the  Recorder Level :"))
if Current_stock == 0:
    status = "Out of Stock"
elif   Current_stock <   Reorder_level :
    status = "Reorder Required"
else :
     status = "Stock Available"
     
     print("Inventory Status----")
     print("Product name",Product_name)
print("Current stock",Current_stock)
print("Reorder level",Reorder_level)
print("status",status)
    