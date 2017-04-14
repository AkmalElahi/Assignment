buffet=("BBQ","Pizza","Ice Creame","Fries","Soft drinks")
print("Buffet:")
for item in buffet:
    print(item)
#buffet[0]="biryani" this line of code won't execute as tuple can't be modified
print("\nchnaged buffet:")
buffet=("BBQ","Biryani","Ice Creame","beef Role","Soft drinks")
for food in buffet:
    print(food)
