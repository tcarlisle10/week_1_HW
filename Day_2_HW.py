# place = input("Choose a place: forest or cave? ")

# if place == "forest": # add another "="
#     action == input("climb a tree or cross a river?") # add another "="
#     if action == "climb a tree": # add another "="
#         print("You found a bird's nest!")
#     elif action == "cross a river":  #Change else to elif and add another "="
#         print("You found a boat!")
# elif place == "cave":  # add another "="
#     print("You find a hidden treasure!")

#----------------------------------------------------------------#

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":  
        print("You found a boat!")
elif place == "cave": 
    action = input("You enter the cave! Do you want to light a torch or proceed in darkness?")
    if action == "Light the torch":
        print("You can now see! There are skeletons all around!!! OH NO!")
        action = input("Do you want to draw your sword and continue or turn around and get the heck out of there?")
        if action == "draw sword":
            print("Good thing you did a horde of skeletons come and attack you!")
            action = input("You swing with all your might and fight all the skeletons and defeat them! Do you wish to continue or loot the skeletons?")
            if action == "continue":
                print("Congratulations! You have found the treasure!")
            elif action == "loot":
                print("UH OH! You have set off a trap and have perished from multiple arrows piercing you")
                print("GAME OVER!")
        elif action == "turn around":
            print("Good thing you did! you hear terrifying noises behind you!")
            print("You escape the cave and go outside... too bad the town now knows you are a weenie! HA HA")
    elif action == "proceed in darkness":
        print("What was that? It felt like a bone!")
        action = input("Continue in the darkness? Light your torch? or Draw your sword?") 
        if action == "continue":
            print("Welp! Your head got cut off by a skeleton warrior")
            print("GAME OVER!")
        elif action == "light your torch":
            print("Uh Oh! You are surrounded by skeleton warriors")
            action = input("Do you want to fight or flee?")
            if action == "fight":
                print("You draw your sword!")
                print("you defeat the skeleton warriors! continue down the path or loot the skeletons?")            #
                action = input("continue down path or loot skeletons?")
                if action == "continue":
                    print("You have found the treasure!")
                elif action == "loot":
                    print("Oops! you have set off a trap and have died!")
                    print("GAME OVER!")
            elif action == "flee":
                print("You narrowly escape!")
        elif action == "draw sword":
            pass        # print("You hear skeleton warriors around you! TOO LATE!!! They attack and kill you!")
                        # print("GAME OVER!")
    else:
        print("invalid input, choose something else")


#------------------------------------------------------------------------------------------------------------------------#

attendees = int(input("Enter number of attendees: ")) # add int() 
venue = "large hall" if attendees >= 100 else "conference room"  # change to else added '>=' cause what if 100 is max capacity for conference room? thats a fire hazard... you also dont need '>=' you can just have '>' 
print(venue)

#----------------------------------------------------------------#

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"  # change to else
print(venue)

food = input('Would you like our vegetarian food?')
if food == "yes":
    print("Veggie Delight Caterers")
else:
    print("Gourment Meals Caterers")
