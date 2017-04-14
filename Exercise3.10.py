list_of_friends=[]
friends=input("Enter no of friends you want to insert in list" )
ch=-1
choise=-1
print("Enter your friends names :")
for i in range(int(friends)):
    list_of_friends.append(input())
while choise!=0:
 print("select your choise")
 print("press 1 to print your friend list")
 print("press 2 to check length your friend list")
 print("press 3 to print your friend list in sorted order ")
 print("press 4 to print your friend list in reverse sorted order")
 print("press 5 to insert name in your list  your friend list")
 print("press 6 to delete any name from list")
 print("press 0 to Exit")
 choise=int(input())
 if choise==1:
     print("Your Friend list is:")
     print(list_of_friends)

 elif choise==2:
     print("your list contain "+str(len(list_of_friends))+ "  friends")
 elif choise==3:
     print("sorted list of your friends :")
     print(sorted(list_of_friends))
 elif choise==4:
     print("your friend list in reversed sorted order")
     print(sorted(list_of_friends,reverse=True))
 elif choise==5:
     position=0
     print("Enter position where you want to insert name")
     position=input()
     print("Enter name you want to insert")
     name=input()
     if position==1:
         list_of_friends.insert(0,name)
         print("your new list  :")
         print(list_of_friends)
     elif position>=len(list_of_friends):
         list_of_friends.append(name)
     else:
         list_of_friends.insert(position,name)
 elif choise==6:
     print("Enter namr you ant to delete")
     name=input()
     list_of_friends.pop(name)
     print("your new list  :")
     print(list_of_friends)
 else:
     print("Invalid Selection")
     exit()

