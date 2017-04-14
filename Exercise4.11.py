my_pizza=["fajita","european cheesy","italian"]
friend_pizzas=my_pizza[:]
print(friend_pizzas)
my_pizza.append("Afghani")
friend_pizzas.append("pepperoni")
print("My favourite Pizzas are:")
for pizza in my_pizza:
    print(pizza)
print("\nMy Friend's favourite Pizzas are:")
for pizza in friend_pizzas:
    print(pizza)