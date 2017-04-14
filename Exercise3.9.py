# Exercise 3.4
Guests=[]
print("Enter guests names you want to invite")
for i in range(4):
    Guests.append(input())
for j in range(4):
    print("Hello  "+ Guests[j]+"   !you are invited for dinner ")
print(str(len(Guests))+" guests are invited for dinner") #printing length of list
# Exercise 3.5
print("\n"+Guests[2]+" is not comming for dinner today")
Guests[2]=input("so I have to invite someone else\n")
for k in range(4):
    print("Hello  " + Guests[k]+"   !you are invited for dinner ")
print(str(len(Guests))+" guests are invited for dinner") # printing length of list
# Exercise 3.6
print("\nI just found a bigger dinner table so I can invite 3 more friends")
Guests.insert(0,input("Enter name to insert first\n"))
Guests.insert(3,input("Enter name to insert in middle\n"))
Guests.append(input("Enter name to insert in last of list\n"))
for l in range(len(Guests)):
    print("Hello  " + Guests[l]+"   !you are invited for dinner ")
print(str(len(Guests))+" guests are invited for dinner")#printing length of list
# Exercise 3.7
print("\nnow I have to shring my Guests list")
while len(Guests)!=2:
    print("sorry "+Guests.pop()+"  I can't Invite you for dinner today")
print(Guests)
print(str(len(Guests))+" guests are invited for dinner") #printing length of list
del(Guests[0])
del(Guests[0])
print("Empty list")
print(Guests)
print(str(len(Guests))+" guests are invited for dinner") #printing length of list
