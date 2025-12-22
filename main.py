# Pokemon Gen 6


# Asking the user for their name.

user_name = input("What would you like your name to be? ")
print("")

# Random generator used lator on in the code

from random import choice as ch

# Preview/Introduction

print(f"Welcome to the Kalos Region {user_name}!")
print("")
print("My name is Augustine Sycamore,")
print("but you can call me Professor Sycamore!")
print("")
print(f"{user_name} This is a world filled with Pokemon, which are both your allies and your bestfriends.")

print("First, I would like you to choose a Pokemon from these 3 in front of you.")
print("   ")

# Choices

Pokeball1 = 1  # Water Pokemon Froakie
Pokeball2 = 2  # Fire Pokemon Fennekin
Pokeball3 = 3  # Grass Pokemon Chespin

print("Pokeball 1 , Pokeball 2 , Pokeball 3. Pick (1-3): ")
print("")

flag = True

while True:

    pokemon = int(input("Which Pokemon would you like to choose? "))
    print("")

    if pokemon == 1:
        print("Froakie, The Water pokemon, A Bubble Frog Pokemon.")
        print("It uses its webbed feet to swim with surprising")
        print("speed.")
        print("Its signature move is Bubble Beam")
        choice = input("Would you like to choose Froakie? (Yes/No): ").lower()
        if choice == "yes":
            print("Froakie is now yours!")
            break
        elif choice == "no":
            print("")
            print("Please pick a Pokemon.")
        else:
            flag = False
            if flag:
                print("Wrong Input.")
    elif pokemon == 2:
        print("Fennekin, the fire type Pokemon.can be temperamental,")
        print("but it tries to do its best for its Trainer")
        print("Searing heat blows from its ears")
        print("This Pokémon loves to snack on twigs.")
        choice = input("Would you like to choose Fennekin? (Yes/No): ").lower()
        if choice == "yes":
            print("Fennekin is now yours!")
            break
        elif choice == "no":
            print("")
            print("Please pick a Pokemon.")
        else:
            flag = False
            if flag:
                print("Wrong Input.")
    elif pokemon == 3:
        print("Chespin, the grass type Pokemon.")
        print("Chespin is known for its hard shell covering its head and back,")
        print("and its generally optimistic nature despite a tendency towards curiosity,")
        print("which sometimes leads to trouble.")
        choice = input("Would you like to choose Chespin? (Yes/No): ").lower()
        if choice == "yes":
            print("Chespin is now yours!")
            break
        elif choice == "no":
            print("")
            print("Please pick a Pokemon.")
        else:
            flag = False
            if flag:
                print("Wrong Input.")


# Receiving off the Pokedex


class Pokemon:
    def __init__(self, entry, name, types, description, level, region, nature, shiny, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.level = level
        self.region = region
        self.nature = nature
        self.shiny = shiny
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ', ' + self.name + '!')

    def display_details(self):
        print('Entry Number: ' + str(self.entry))
        print('Name: ' + self.name)

        if len(self.types) == 1:
            print('Type: ' + self.types[0])
        else:
            print('Type: ' + self.types[0] + '/' + self.types[1])

        print('Lv. ' + str(self.level))
        print('Region: ' + self.region)
        print('Description: ' + self.description)
        print("Nature: " + self.nature)

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + ' hasn\'t been caught yet.')

        if self.shiny:
            print(self.name + ' is shiny!')
        else:
            print(self.name + ' is not shiny.')


froakie = Pokemon(656, "Froakie", ["Water"],
                  "Froakie, The Water pokemon, A Bubble Frog Pokemon. It uses its webbed feet to swim with surprising speed. It's signature move is bubble beam.",
                  5, "Kalos", "Timid", True, True)
fennekin = Pokemon(653, "Fennekin", ["Fire"],
                   "Fennekin, the fire type Pokemon.can be temperamental, but it tries to do its best for its Trainer. Searing heat blows from its ears, this pokemon loves to snack on twigs.",
                   5, "Kalos", "Harsh", True, True)
chespin = Pokemon(650, "Fennekin", ["Grass"],
                  "Chespin, the grass type Pokemon.Chespin is known for its hard shell covering its head and back,nd its generally optimistic nature despite a tendency towards curiosity,which sometimes leads to trouble.",
                  5, "Kalos", "Playful", True, True)

print("")

print("Along with your Pokemon I would like to give you this")
print("Pokedex.")
print("Its a device that lets you learn about pokemeon,")
print("and records data about pokemon who we have yet to")
print("encounter.")

# Pokemon Database, asking the user if they want a detailed description of their pokemon.

pokedex = input("Would you like to use the Pokedex on your pokemon? Yes/No: ").lower()
print("")

if pokedex == "yes" and pokemon == 1:
    froakie.display_details()
elif pokedex == "yes" and pokemon == 2:
    fennekin.display_details()
elif pokedex == "yes" and pokemon == 3:
    chespin.display_details()
else:
    print("Alright!")

print("")

# The first trainer battle. Dialogue**

print("Here are some pokeballs, these will help you in catching pokemon.")
print("")
print("As you are about to leave the lab, you bump into your bestfriend.")
print(f"{user_name}, I didn't think you would be here this early!")
print("Trying to get the jump on me huh?")
print("")
print("Well that won't happen, wait 2 minutes while I get my pokmeon!")
print(".....")
print(f"Alright!! I got my first pokemon, how about a battle now {user_name}")

# Trainer battle commence

froakie = ["Pound", "Growl", "Bubble Beam"]
fennekin = ["Tail Whip", "Ember", "Howl"]
chespin = ["Rollout", "Pin Missile", "Bullet Seed"]

damage = [1, 3, 5, 9]

# Pokemon decision on which pokemon is thrown according to the users pick.

if pokemon == 1:
    print("Jake threw out Fennekin! Lv. 5 , Health = 20")
    print("You threw out Froakie! Lv. 5 , Health = 19")
elif pokemon == 2:
    print("Jake threw out Chespin! Lv . 5 , Health = 18")
    print("You threw out Fennekin! Lv . 5 , Heath = 20")
elif pokemon == 3:
    print("Jake threw out Froakie! Lv . 5 , Health = 19")
    print("You threw out Chespin! Lv . 5 , Health = 18")

print("")

health_1 = 20  # If it were Pokemon 1 Jake Fennekin
health_2 = 19  # Pokemon Froakie Starter User
health_5 = 20  # Pokemon Fennekin Starter User
health_6 = 18  # Pokemon Chespin Starter User
health_3 = 18  # If it were Pokemon 2 Jake Chespin
health_4 = 19  # If it were Pokemon 3 Jake Froakie

exp = 0

level_froakie = 5
level_fennekin = 5
level_chespin = 5

# Battle commence

while True:

    if pokemon == 1:  # The water type pokemon Froakie!
        print("Pound , Growl , Bubble Beam")
        move_asker = int(input("Select a move: 1-3 "))  # Ask the user for input on what move to use.
        print("")
        if move_asker == 1:
            print("Froakie used Pound!")
            damage_done = ch(damage)
            print(f"Froakie has done {damage_done} damage!")
            health_1 = health_1 - damage_done  # If the move = 1, damage and health are calculated and printed.
            if health_1 > 0:
                print(f"Fennekin has {health_1} health left!")
            random_move_jake = ch(fennekin)
            print(f"Fennekin used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Howl":
                print("Fennekins attack power rose!")
                damage_done = 0
            elif random_move_jake == "Tail Whip":
                print("Froakies defense fell!")
                damage_done = 0
            print(f"Fennekin has done {damage_done} damage!")
            health_2 = health_2 - damage_done
            if health_2 > 0:
                print(f"Froakie has {health_2} health left!")
            if health_1 <= 0:
                print("Froakie has won!!")
                print("Froakie has been awared 56 exp.")
                exp = exp + 56
                print("Froakie is now level 6!")
                level_froakie = level_froakie + 1
                break
            elif health_2 <= 0:
                print("Fennekin has won!!")
                break
        elif move_asker == 2:  # If the move = 2, damage and health are calculated and printed.
            print("Froakie used Growl!")
            print("Fennekins attack fell!")
            random_move_jake = ch(fennekin)
            print(f"Fennekin used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Howl":  # Non damage moves like howl or tailwhip do no damage
                print("Fennekins attack power rose!")
                damage_done = 0
            elif random_move_jake == "Tail Whip":
                print("Froakies defense fell!")
                damage_done = 0
            if health_1 > 0:
                print(f"Fennekin has {health_1} health left!")
            health_2 = health_2 - damage_done
            if health_2 > 0:
                print(f"Froakie has {health_2} left!")
            if health_1 <= 0:
                print("Froakie has won!!")
                print("Froakie has been awared 56 exp.")
                exp = exp + 56  # Exp is awarded after trainer has been defeated.
                print("Froakie is now level 6!")
                level_froakie = level_froakie + 1
                break
            elif health_2 <= 0:
                print("Fennekin has won!!")
                break
        elif move_asker == 3:  # If the move = 3, damage and health are calculated and printed.
            print("Froakie used Bubble Beam!")
            damage_done = ch(damage)
            print(f"Froakie has done {damage_done} damage!")
            health_1 = health_1 - damage_done
            if health_1 > 0:
                print(f"Fennekin has {health_1} health left!")
            random_move_jake = ch(fennekin)
            print(f"Fennekin used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Howl":
                print("Fennekins attack power rose!")
                damage_done = 0
            elif random_move_jake == "Tail Whip":
                print("Froakies defense fell!")
                damage_done = 0
            print(f"Fennekin has done {damage_done} damage!")
            health_2 = health_2 - damage_done
            if health_2 > 0:
                print(f"Froakie has {health_2} health left!")
            if health_1 <= 0:
                print("Froakie has won!!")
                print("Froakie has been awared 56 exp.")
                exp = exp + 56
                print("Froakie is now level 6!")
                level_froakie = level_froakie + 1
                break
            elif health_2 <= 0:
                print("Fennekin has won!!")
                break
    if pokemon == 2:  # The fire type pokemon Fennekin!
        print("Tail Whip, Ember , Howl")
        move_asker = int(input("Select a move: 1-3 "))  # Ask the user for input on what move to use.
        print("")
        if move_asker == 1:
            print("Fennekin used Tail Whip!")
            if move_asker == "Tail Whip":
                print("Chespins defense fell!")
                damage_done = 0
                print(f"Fennekin has done {damage_done} damage!")
                health_3 = health_3 - damage_done
            if health_3 > 0:
                print(f"Chespin has {health_3} health left!")
            random_move_jake = ch(chespin)
            print(f"Chespin used {random_move_jake}")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_5 = health_5 - damage_done
            if health_5 > 0:
                print(f"Fennekin has {health_5} health left!")
            if health_3 <= 0:
                print("Fennekin has won!!")
                print("Fennekin has been awared 56 exp.")
                exp = exp + 56
                print("Fennekin is now level 6!")
                level_fennekin = level_fennekin + 1
                break
            elif health_5 <= 0:
                print("Chespin has won!!")
                break
        elif move_asker == 2:
            print("Fennekin used Ember!")
            damage_done = ch(damage)
            print(f"Fennekin has done {damage_done} damage!")
            health_3 = health_3 - damage_done
            if health_3 > 0:
                print(f"Chespin has {health_3} health left!")
            random_move_jake = ch(chespin)
            print(f"Chespin used {random_move_jake}")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_5 = health_5 - damage_done
            if health_5 > 0:
                print(f"Fennekin has {health_5} health left!")
            if health_3 <= 0:
                print("Fennekin has won!!")
                print("Fennekin has been awared 56 exp.")
                exp = exp + 56  # Exp is awarded after trainer has been defeated.
                print("Fennekin is now level 6!")
                level_fennekin = level_fennekin + 1
                break
            elif health_5 <= 0:
                print("Chespin has won!!")
                break
        elif move_asker == 3:  # If the move = 3, damage and health are calculated and printed.
            print("Fennekin used Howl")
            if move_asker == "Howl":
                print("Fennekins attack rose!")
                damage_done = 0
            print(f"Fennekin has done {damage_done} damage!")
            health_3 = health_3 - damage_done
            if health_3 > 0:
                print(f"Chespin has {health_3} health left!")
            random_move_jake = ch(chespin)
            print(f"Chespin used {random_move_jake}")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_5 = health_5 - damage_done
            if health_5 > 0:
                print(f"Fennekin has {health_5} health left!")
            if health_3 <= 0:
                print("Fennekin has won!!")
                print("Fennekin has been awared 56 exp.")
                exp = exp + 56
                print("Fennekin is now level 6!")
                level_fennekin = level_fennekin + 1
                break
            elif health_5 <= 0:
                print("Chespin has won!!")
                break
    if pokemon == 3:  # The grass type pokemon Chespin!
        print("Rollout, Pin Missle , Bullet Seed")
        move_asker = int(input("Select a move: 1-3 "))  # Ask the user for input on what move to use.
        print("")
        if move_asker == 1:
            print("Chespin used Rollout!")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_4 = health_4 - damage_done
            if health_4 > 0:
                print(f"Froakie has {health_4} health left!")
            random_move_jake = ch(froakie)
            print(f"Froakie used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Growl":
                print("Chespins defense fell!")
                damage_done = 0
            print(f"Chespin has done {damage_done} damage!")
            health_6 = health_6 - damage_done
            if health_6 > 0:
                print(f"Chespin has {health_6} health left!")
            if health_4 <= 0:
                print("Chespin has won!!")
                print("Chespin has been awared 56 exp.")
                exp = exp + 56
                print("Chespin is now level 6!")
                level_chespin = level_chespin + 1
                break
            elif health_6 <= 0:
                print("Froakie has won!!")
                break
        elif move_asker == 2:
            print("Chespin used Pin Missile!")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_4 = health_4 - damage_done
            if health_4 > 0:
                print(f"Froakie has {health_4} health left!")
            random_move_jake = ch(froakie)
            print(f"Froakie used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Growl":
                print("Chespins defense fell!")
                damage_done = 0
            print(f"Froakie has done {damage_done} damage!")
            health_6 = health_6 - damage_done
            if health_6 > 0:
                print(f"Chespin has {health_6} health left!")
            if health_4 <= 0:
                print("Chespin has won!!")
                print("Chespin has been awared 56 exp.")
                exp = exp + 56  # Exp is awarded after trainer has been defeated.
                print("Chespin is now level 6!")
                level_fennekin = level_fennekin + 1
                break
            elif health_6 <= 0:
                print("Froakie has won!!")
                break
        elif move_asker == 3:  # If the move = 3, damage and health are calculated and printed.
            print("Chespin used Bullet Seed")
            damage_done = ch(damage)
            print(f"Chespin has done {damage_done} damage!")
            health_4 = health_4 - damage_done
            if health_4 > 0:
                print(f"Froakie has {health_4} health left!")
            random_move_jake = ch(froakie)
            print(f"Froakie used {random_move_jake}")
            damage_done = ch(damage)
            if random_move_jake == "Growl":
                print("Chespins defense fell!")
                damage_done = 0
            print(f"Froakie has done {damage_done} damage!")
            health_6 = health_6 - damage_done
            if health_6 > 0:
                print(f"Fennekin has {health_5} health left!")
            if health_4 <= 0:
                print("Chespin has won!!")
                print("Chespin has been awared 56 exp.")
                exp = exp + 56
                print("Chespin is now level 6!")
                level_fennekin = level_fennekin + 1
                break
            elif health_6 <= 0:
                print("Froakie has won!!")
                break

# Dialogue after the battle!

print("")

print(f"That was a great battle {user_name}!")
print("I should head out now, theres a whole world of pokemon out there!")
print("Make sure to stop by your house so you can get some supplies!")
print("Jake runs off as you look at your pokemon, both feeling excited for your journey.")
print("Professor Sycamore walks in..")
print("")
print(f"{user_name}, please have these as well.")
print("𝘗𝘳𝘰𝘧𝘦𝘴𝘴𝘰𝘳 𝘩𝘢𝘯𝘥𝘴 𝘺𝘰𝘶 𝘢 𝘧𝘦𝘸 𝘱𝘰𝘬𝘦𝘣𝘢𝘭𝘭𝘴 𝘢𝘯𝘥 𝘩𝘦𝘢𝘭𝘪𝘯𝘨 𝘱𝘰𝘵𝘪𝘰𝘯!")
print("These pokeballs will help you catch pokemon and grow your team!")
print("Kalos is a big region and I wish you the best of luck!")
print("I suggest you travel on route 3, which will lead you straight to the first gym.")
print("A small hint.. the first gym is an electric type!")

# To be continued!