
def calculate_discount(price, discount=10):
    amount = price * discount / 100
    return amount

print(calculate_discount(25000))
print(calculate_discount(3900, 150))