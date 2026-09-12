first_number= int(input("Enter the First Number :"))
Arithmetic_operator = (input("Enter the Arithmetic Operator (+,-,*,/,) :"))
second_number = int(input("Enter the Second Number :"))

if Arithmetic_operator == '+':
      print("Addition : ",first_number + second_number)
elif  Arithmetic_operator == '-':
     print("Substraction : ",first_number - second_number) 
elif  Arithmetic_operator == '*':
     print("Multiplication : ",first_number * second_number)
elif  Arithmetic_operator == '/':
       print("Division : ",first_number / second_number)