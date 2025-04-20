# tui.py
def display_welcome():
    """Display the welcome message."""
    print("--------------------------")
    print("Disneyland Review Analysis")
    print("--------------------------")

def confirm_data_loaded(row_count):
    """Confirm data loading and display row count."""
    print(f"Dataset loaded successfully with {row_count} rows.")

def display_main_menu():
    """Display the main menu and return user choice."""
    print("\nMain Menu:")
    print("A - View Data")
    print("B - Visualise Data")
    print("X - Exit")
    return input("Please enter your choice: ").strip().upper()

def display_view_data_submenu():
    """Display the View Data submenu and return user choice."""
    print("\nView Data Menu:")
    print("1 - View all reviews for a park")
    print("2 - Number of reviews for a park by location")
    print("3 - Average rating for a park in a year")
    print("4 - Average rating per park by reviewer location")
    print("X - Back to Main Menu")
    return input("Please enter your choice: ").strip().upper()

def display_visualizations_submenu():
    """Display the Visualizations submenu and return user choice."""
    print("\nVisualizations Menu:")
    print("1 - Pie chart of reviews by park")
    print("2 - Bar chart of average ratings by park")
    print("3 - Bar chart of top 10 locations by rating for a park")
    print("4 - Bar chart of average rating by month for a park")
    print("X - Back to Main Menu")
    return input("Please enter your choice: ").strip().upper()

def confirm_choice(choice):
    """Confirm the user's menu choice."""
    print(f"You selected: {choice}")

def display_invalid_choice():
    """Display an error for invalid menu choice."""
    print("Invalid choice. Please try again.")

def get_park_input():
    """Get park name from user."""
    print("Available parks: Disneyland_California, Disneyland_HongKong, Disneyland_Paris")
    return input("Enter park name: ").strip()

def get_location_input():
    """Get reviewer location from user."""
    return input("Enter reviewer location: ").strip()

def get_year_input():
    """Get year from user."""
    return input("Enter year (e.g., 2019): ").strip()

def get_export_format():
    """Get export format from user."""
    print("Available formats: TXT, CSV, JSON")
    return input("Enter export format: ").strip().upper()

def display_reviews(reviews, park):
    """Display reviews for a specific park."""
    if reviews:
        print(f"\nReviews for {park}:")
        for review in reviews:
            print(f"Rating: {review['Rating']}, Location: {review['Reviewer_Location']}, Date: {review['Year_Month']}")
    else:
        print(f"No reviews found for {park}.")

def display_review_count(count, park, location):
    """Display the number of reviews for a park by location."""
    print(f"{park} has {count} reviews from {location}.")

def display_average_rating(avg_rating, park, year):
    """Display the average rating for a park in a year."""
    if avg_rating is not None:
        print(f"Average rating for {park} in {year}: {avg_rating:.2f}")
    else:
        print(f"No reviews found for {park} in {year}.")

def display_average_rating_by_location(park_ratings):
    """Display average ratings per park by reviewer location."""
    for park, ratings in park_ratings.items():
        print(f"\nAverage ratings for {park}:")
        for location, avg in ratings.items():
            print(f"  {location}: {avg:.2f}")

def confirm_export(format_type):
    """Confirm data export."""
    print(f"Data exported successfully in {format_type} format.")

def display_exit():
    """Display exit message."""
    print("Thank you for using the Disneyland Review Analysis System. Goodbye!")