while True:
  print("---Retail Store Menu---")
  print("1. Calculate Discount")
  print("2. Check Inventory ")
  print("3. Calculate Total Bill")
  print("4. Exit")
  
  choice = input("Enter your choice: ")
  if choice == 1:
      amount = float(input("Enter the purchase amount :")) 
      if amount < 1000:
          discount = 0
      elif amount <5000:
          discount = 5
      elif amount <10000:
          discount = 10
      else :
          discount = 15
          print("Your Total Discount :",discount,"%")
  elif choice == "2":
      stock = int(input("Enter the current stock:"))
      reorder = int(input("Enter the reorder level:"))
      if stock == 0:
          print("status : Out of Stock")
      elif stock < reorder :
          print("status : Reorder Required")
      else :
          print("status :Stock Available ")   
  elif choice == "3":
         count = int(input("Enter number of products: "))
         total = 0
         for i in range(count):
             price = float(input(f"Enter price of product {i + 1}: ₹"))
             total += price
             print("Total Bill: ₹", total)
            
  elif choice == "4":
        print("Thank you for using the Retail Store Application.")
        break
  else:
      print("Invalid choice. Please select an option from 1 to 4.")
               