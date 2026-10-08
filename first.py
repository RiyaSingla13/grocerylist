
print("==============================="*4)

print("`````````Grocery List``````````")

bread = int(input("Enter the quantity of bread: "))
rice = int(input("Enter the quantity of rice: "))
eggs = int(input("Enter the quantity of eggs: "))
chocolate = int(input("Enter the quantity of chocolate: "))
flour = int(input("Enter the quantity of flour: "))

bread_price = 50
rice_price = 100
eggs_price = 10
chocolate_price = 50
flour_price = 150


import math
total_cost = (bread * bread_price) + (rice * rice_price) + (eggs * eggs_price) + (chocolate * chocolate_price) + (flour * flour_price)

print(f"Total cost of groceries: {total_cost}")

print("==============================="*4)

print("`````````Grocery List Bill``````````")

print(f"Quantity of bread: {bread} | Price: {bread_price} | Cost: {bread * bread_price}")
print(f"Quantity of rice: {rice} | Price: {rice_price} | Cost: {rice * rice_price}")
print(f"Quantity of eggs: {eggs} | Price: {eggs_price} | Cost: {eggs * eggs_price}")
print(f"Quantity of chocolate: {chocolate} | Price: {chocolate_price} | Cost: {chocolate * chocolate_price}")
print(f"Quantity of flour: {flour} | Price: {flour_price} | Cost: {flour * flour_price}")

print(f"Total cost of groceries: {total_cost}")

print("==============================="*2)


print("`````````Grocery List Bill with Discount``````````")


if total_cost >6000:
    discount = total_cost * 0.2
    total_cost_after_discount = total_cost - discount
    print(f"Total cost after 20% discount: {total_cost_after_discount}")

elif total_cost > 2500: 
    discount = total_cost * 0.1
    total_cost_after_discount = total_cost - discount
    print(f"Total cost after 10% discount: {total_cost_after_discount}")

elif total_cost > 1000:
    discount = total_cost * 0.05
    total_cost_after_discount = total_cost - discount
    print(f"Total cost after 5% discount: {total_cost_after_discount}")

else:
    print("Shop more than 1000 to get a discount")

print("==============================="*2)

print("`````````Grocery List Bill with Discount and Tax``````````")
print(f"Total cost after discount: {total_cost_after_discount}")
print(f"Tax: {total_cost_after_discount * 0.05}")

print("==============================="*2)

print(f"Total cost after discount and tax: {total_cost_after_discount + (total_cost_after_discount * 0.05)}")

print("==============================="*4)

print("THANKS FOR VISITING OUR STORE")
