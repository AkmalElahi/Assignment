my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for foods in my_foods:
    print(foods)
print("\nMy friend's favorite foods are:")
for ffoods in friend_foods:
    print(ffoods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for foood in friend_foods:
    print(foood)