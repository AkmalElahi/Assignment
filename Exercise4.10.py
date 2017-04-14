friends=[]
for i in range(10):
    friends.append(i)
print(friends)
print("First three items of the list are :")
print(friends[:3])
print("three from the middle of the list are :")
mid=int(len(friends)/2)
for j in range(3):
    print(friends[mid])
    mid=mid+1
print("last three items of the list are :")
print(friends[-3:])