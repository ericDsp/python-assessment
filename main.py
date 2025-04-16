"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
#Section A#

print("--------------------------\nDisneyLand Review Analyser\n--------------------------")

import csv

# Replace 'your_file.csv' with the path to your actual CSV file
filename = 'data/disneyland_reviews.csv'
data = []
try:
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    print("\nFinished reading the dataset.")
    print(f"Total number of rows: {len(data)}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# Displaying a simple menu
print("\n--- Main Menu ---")
print("[A]. View Data")
print("[B]. Visualise Data")
print("[X]. Exit")

# Taking user input
selection = input("\nPlease enter your choice (A-X): ")

if selection == "A":
    print("\nYou selected: View Data")
    print("\nPlease enter one of the following options:")
    print("[A] View reviews by park")
    print("[B] Number of reviews by park abd reviewer location")
    print("[C] Average score per year by park")
    print("[D] Average score per park by reviewer location")

    selection = input()

elif selection == "A":
    print("\nYou selected: View reviews by park")
    print("Select a specific park")
    print("[1] DisneyLand Paris")
    print("[2] DisneyLand California")
    print("[3] DisneyLand Hong Kong")

    selection = input()


elif selection == "B":
    print("\nYou selected: Visualise Data")
    print("\nEnter one of the following options:")
    print("[A] Most reviewed park")
    print("[B] Average scores")
    print("[C] Park Ranking by nationality")
    print("[D] Most popular month by park")

    selection = input()

elif selection == "X":
    print("You selected: Exit\nGoodbye!")

else:
    print("\nInvalid choice. Please enter the letter which corresponds with your desired menu choice: \n[A]. View Data"
    "\n[B]. Visualise Data"
    "\n[X]. Exit")


