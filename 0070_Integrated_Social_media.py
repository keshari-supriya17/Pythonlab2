user = {
    "name"  : "SupriyaKeshari",
     "ID" : 487,
    "age" : 21,
    "interest" : ["Music" , "Dance" , "Volleyball" , "Sleeping"],
    "FriendList" : ["Tanvi" , "Vaibhavi", "Tanisha", "Sneha"]
} 
friend = ["Supriya","Tanvi","Sneha","Tanisha"]
friend.append ( "Swati")
friend.remove  ("Sneha")
friend.sort()

profile = ["Supriya" , 21 , "Varanasi"]
 
user = ["supriya","shubham","shubhii","tanvi"]
print("shubham" in user) 
user.sort()

activities = ["Post","like","Comment","Follow","Subscribe"]
 
my_list = [2,23,12,35,10,20,30,5,3,12]
print(my_list)
my_list.append("Supriya Keshari")
print("After adding name in list:",my_list)
my_list.pop(2)
print("After removing 3rd element in the list:",my_list)
my_list[0] , my_list[-1] = my_list[-1] , my_list[0]
print("After swapping the first element to the last element:",my_list)
total_element = len(my_list) 
print("Total number of the list",my_list)

print(activities[0])
print(activities[1:4])
print(user)    
print(profile[0])
print(profile[1])
print(friend)
print(user)