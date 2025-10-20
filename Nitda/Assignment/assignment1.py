'''Please write a simple python program that creates a Band Name Generator. The program should do the following:
Print out a welcome message
Prompts the user to enter the name of of his hometown
Prompt the user to enter the name of his favorite pet
Prompt the user to enter his lucky number
Concatenate the user's hometown and pet name and lucky number.
To concatenate, the hometown should be first, then a space, then the pet name, followed by the number i.e., there should be no space between the pet name and the lucky number 
convert all characters in the result to title case
print the result in the form "Your band name is <BAND NAME>"
A sample output is as follows:

Enter your hometown: Colorado
Enter your favorite pet's name: Jim
Enter your lucky number: 7
Your band name  Colorado Jim7, rock and roll 🔥🎸🚀'''

# Band Name Generator

# Welcome message
print("Welcome to the Band Name Generator!")

# Get user input
hometown = input("Enter your hometown: ")
pet_name = input("Enter your favorite pet's name: ")
lucky_number = input("Enter your lucky number: ")

# Concatenate the values
band_name = f"{hometown} {pet_name}{lucky_number}"

# Convert to title case
band_name_title_case = band_name.title()

# Display the result
print(f"Your band name {band_name_title_case}, rock and roll")
