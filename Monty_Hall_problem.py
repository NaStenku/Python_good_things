from random import shuffle
doors = {1: "goat", 2: "goat", 3: "car"}
choice = int(input("Choose the door number(1,2 or 3):"))
# def shuffle_new():
#     keys = list(doors.keys())
#     shuffle(keys)
#     Shuffled_doors = dict()
#     for key in keys:
#         Shuffled_doors.update({doors[key]: key})
#     return Shuffled_doors
op = 1
if choice == 1:
    op = 2
else:
    op = 1
print ("Ok. But i want to open one more door for you. Here is door", op , "there is a goat. Do you still want to open the door number", choice, "?")
choice2 = int(input("Choose the door number(1,2 or 3):"))
if doors[choice2] == "car":
    print("Congratulation!")
else:
    print("Sorry, maybe next time")

