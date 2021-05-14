# You enter a dark room and should choose one of two doors, identified by 1 and 2

# Door 1 contains a giant bear eating a cheese cake, Show this to the user and two options:
    # 1. Take the cake --> The bear eats your face off, Good Job!
    # 2. Scream at the bear --> The bear eats your legs off, Good Job!
    # <hidden> If the user chooses another option --> Well doing, {option} is probably better. Bear runs away!

# Door 2 --> You stare into the endless abyss at Cthulhu's retina. Show three options with the message "What is your insanity"
    # 1. Blueberries
    # 2. Yellow Jacket clothespins
    # 3. Understanding revolvers yelling melodies

    # if choose option 1 or 2 --> Your body survives powered by a mind of jello
    # if choose option 3 --> Good Job!
    # if choose another option --> print "The insanity rots of your eyes into a pool of muck, Good Job!"

# If another door number is chose --> print "You stumble around and fall on a knife and die. Good Job!"

print("You enter a dark room and should choose one of two doors:\nDoor 1\nDoor 2")
door_number = input("Choose a number: ")

# while door_number not in ["1", "2"]:
#     print("Not valid")
#     door_number = input("Choose a number: ")

if door_number != "1" and door_number != "2":
    print("You stumble around and fall on a knife and die. Good Job!")
elif door_number == "1":
    print("This room contains a giant bear eating a cheese cake")
    print("1. Take the cake\n2. Scream at the bear")
    door_1_option = input("Choose a number: ")
    if door_1_option == "1":
        print("The bear eats your face off, Good Job!")
    elif door_1_option == "2":
        print("The bear eats your legs off, Good Job!")
    else:
        print(f"Well doing, {door_1_option} is probably better. Bear runs away!")
elif door_number == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("What is your insanity:\n1. Blueberries\n2. Yellow Jacket clothespins\n3. Understanding revolvers yelling melodies")
    door_2_option = input("Choose a number: ")
    if door_2_option == "1" or door_2_option == "2":
        print("Your body survives powered by a mind of jello")
    elif door_2_option == "3":
        print("Good Job!")
    else:
        print("The insanity rots of your eyes into a pool of muck, Good Job!")
