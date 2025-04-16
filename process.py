def display_park_reviews(data):
    park_name = input("Enter the name of the park you wish to see reviews for: ").strip().lower()
    found = False

    print(f"\nReviews for '{park_name.title()}':\n" + "-" * 40)
    for row in data:
        # Assuming the park name is in the first column and review in the second column
        if park_name in row[0].lower():
            found = True
            print(f"- {row[1]}")  # Change index if review is in a different column

    if not found:
        print("No reviews found for that park.")

def sub_menu_a(data):
    while True:
        print("\nSub-Menu A:")
        print("1. View reviews for a specific park")
        print("2. Return to main menu")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_park_reviews(data)
        elif choice == "2":
            break
        else:
            print("Invalid option. Please try again.")
