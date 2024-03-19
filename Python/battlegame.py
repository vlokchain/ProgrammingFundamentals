import sys

wizard = "Wizard"
elf = "Elf"
human = "Human"
dwarf = "Dwarf"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
dwarf_hp = 50

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20
dragon_dmg = 50
dwarf_dmg = 125

while True:
    print("\n1) Wizard\n2) Elf\n3) Human\n4) Dwarf\n\nOr, enter 'exit' to quit the game.")
    choice = input("Select your character: ").lower()

    if choice == "exit":
        print("Thank you for playing!")
        sys.exit()

    elif choice == "1" or "wizard":
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_dmg
        break

    elif choice == "2" or "elf":
        character = elf
        my_hp = elf_hp
        my_dmg = elf_dmg
        break

    elif choice == "3" or "human":
        character = human
        my_hp = human_hp
        my_dmg = human_dmg
        break

    elif choice == "4" or "dwarf":
        character = dwarf
        my_hp = dwarf_hp
        my_dmg = dwarf_dmg
        break

    else:
        print("Unknown character")

print(f"You have chosen the character: {wizard}")
print(f"Health: {my_hp}")
print(f"Damage: {my_dmg}")

while True:
    dragon_hp -= my_dmg
    print(f"The {character} damaged the Dragon! > The Dragon's HP is now {dragon_hp}.")
    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    my_hp -= dragon_dmg
    print(f"The Dragon strikes back at {character}. > The {character}'s HP is now {my_hp}.")

    if my_hp <= 0:
        print(f"The {character} has lost the battle!")
        break

    play_again = input("Game over! Would you like to play again? Enter (Yes/No): ").lower()
    if play_again not in ("yes" or "y"):
        print("Exiting the game. Goodbye!")
        sys.exit()