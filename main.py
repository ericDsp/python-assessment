# main.py
import tui
import process
import visual
import exporter


def main():
    # Display welcome message
    tui.display_welcome()

    # Read CSV data
    data = process.read_csv("Disneyland_reviews.csv")
    tui.confirm_data_loaded(len(data))

    while True:
        # Display main menu and get user choice
        choice = tui.display_main_menu()
        tui.confirm_choice(choice)

        if choice == 'X':
            tui.display_exit()
            break
        elif choice == 'A':
            handle_view_data(data)
        elif choice == 'B':
            handle_visualise_data(data)
        else:
            tui.display_invalid_choice()


def handle_view_data(data):
    """Handle the View Data submenu (Option A)."""
    while True:
        choice = tui.display_view_data_submenu()
        tui.confirm_choice(choice)

        if choice == 'X':
            break
        elif choice == '1':
            park = tui.get_park_input()
            reviews = process.get_reviews_by_park(data, park)
            tui.display_reviews(reviews, park)
        elif choice == '2':
            park = tui.get_park_input()
            location = tui.get_location_input()
            count = process.get_review_count_by_location(data, park, location)
            tui.display_review_count(count, park, location)
        elif choice == '3':
            park = tui.get_park_input()
            year = tui.get_year_input()
            avg_rating = process.get_average_rating_by_year(data, park, year)
            tui.display_average_rating(avg_rating, park, year)
        elif choice == '4':
            park_ratings = process.get_average_rating_by_location(data)
            tui.display_average_rating_by_location(park_ratings)
        else:
            tui.display_invalid_choice()


def handle_visualizations(data):
    """Handle the Visualizations submenu (Option B)."""
    while True:
        choice = tui.display_visualizations_submenu()
        tui.confirm_choice(choice)

        if choice == 'X':
            break
        elif choice == '1':
            counts = process.get_review_counts_by_park(data)
            visual.plot_pie_chart(counts, "Number of Reviews by Park")
        elif choice == '2':
            avg_ratings = process.get_average_rating_by_park(data)
            visual.plot_bar_chart(avg_ratings, "Average Rating by Park", "Park", "Average Rating")
        elif choice == '3':
            park = tui.get_park_input()
            top_locations = process.get_top_locations_by_rating(data, park)
            visual.plot_bar_chart(top_locations, f"Top 10 Locations for {park}", "Location", "Average Rating")
        elif choice == '4':
            park = tui.get_park_input()
            monthly_ratings = process.get_monthly_ratings(data, park)
            visual.plot_bar_chart(monthly_ratings, f"Average Rating by Month for {park}", "Month", "Average Rating")
        else:
            tui.display_invalid_choice()


def handle_export(data):
    """Handle the Export Data feature (Option C)."""
    format_choice = tui.get_export_format()
    exporter_obj = exporter.DataExporter(data)
    exporter_obj.export_data(format_choice)
    tui.confirm_export(format_choice)


if __name__ == "__main__":
    main()