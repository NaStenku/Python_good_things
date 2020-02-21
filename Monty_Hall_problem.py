import random
choice = int(input("Choose the door number(1,2 or 3):"))
doors = [1,2,3]
car = random.randint (1,3)
open_door = list(filter(lambda x: x != car and x != choice, doors))[0]
close_door = list(filter(lambda x: x != choice and x != open_door, doors))[0]
print ("Ok. But I want to open one door for you. Now I will open the door number", open_door, "and we will see what's there. Oh! Goat here! Do you still want to open the door number", choice, "?")
choice2 = int(input("Choose the door number: %s or %s ?" % (choice, close_door)))
print("Congratulation!" if choice2 == car else  "Maybe next time")


