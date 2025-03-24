import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# the above statement is a unicode character used to print the sides of a dice
# the elements printed using the unicodes are ● ┌ ─ ┐ │ └ ┘

# creating the dice

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

# creating a dictionary of cubes
dice_art = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│ ●       │",
                "│    ●    │",
                "│       ● │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
}
dice = []
total = 0
number_of_dice = int(input("How many dice r u rolling ? :"))
random.randint(0,6)
for die in range(number_of_dice):
    dice.append(random.randint(1,6))

print(dice)

# for die in range(number_of_dice):
#     for line in dice_art.get(dice[die]):  #depends upon the above for loop die keeps incrementing
#         # and setting new values or index for dice array...
#         print(line) #prints the lines of (strings from the above dictionary ... using dice_art (unicodes)
#         pass

# program for printing all the dices horizontally
# procedures for printing , print the first lines of all the dices

for line in range(5): # 5 tells the size of the cube as we used 5 strings in the dictionary
    for die in dice:
        print(dice_art.get(die)[line],end=" ")
        pass
        
    print()
    pass

for die in dice:
    total += die

print(f"\ntotal:{total}")