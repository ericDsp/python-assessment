# process.py
import csv
from collections import defaultdict
from datetime import datetime


def read_csv(file_path):
    """Read the CSV file and return a list of dictionaries."""
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


def get_reviews_by_park(data, park):
    """Return all reviews for a specific park."""
    return [review for review in data if review['Branch'] == park]


def get_review_count_by_location(data, park, location):
    """Return the number of reviews for a park from a specific location."""
    return sum(1 for review in data if review['Branch'] == park and review['Reviewer_Location'] == location)


def get_average_rating_by_year(data, park, year):
    """Return the average rating for a park in a specific year."""
    ratings = [int(review['Rating']) for review in data
               if review['Branch'] == park and review['Year_Month'].startswith(year)]
    return sum(ratings) / len(ratings) if ratings else None


def get_average_rating_by_location(data):
    """Return average rating per park by reviewer location."""
    park_ratings = defaultdict(lambda: defaultdict(list))
    for review in data:
        park = review['Branch']
        location = review['Reviewer_Location']
        rating = int(review['Rating'])
        park_ratings[park][location].append(rating)

    result = {}
    for park, locations in park_ratings.items():
        result[park] = {loc: sum(ratings) / len(ratings) for loc, ratings in locations.items()}
    return result


def get_review_counts_by_park(data):
    """Return the number of reviews for each park."""
    counts = defaultdict(int)
    for review in data:
        counts[review['Branch']] += 1
    return dict(counts)


def get_average_rating_by_park(data):
    """Return the average rating for each park."""
    park_ratings = defaultdict(list)
    for review in data:
        park_ratings[review['Branch']].append(int(review['Rating']))

    return {park: sum(ratings) / len(ratings) for park, ratings in park_ratings.items()}


def get_top_locations_by_rating(data, park, limit=10):
    """Return top locations by average rating for a park."""
    location_ratings = defaultdict(list)
    for review in data:
        if review['Branch'] == park:
            location_ratings[review['Reviewer_Location']].append(int(review['Rating']))

    avg_ratings = {loc: sum(ratings) / len(ratings) for loc, ratings in location_ratings.items()}
    sorted_locations = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)[:limit]
    return dict(sorted_locations)


def get_monthly_ratings(data, park):
    """Return average rating by month for a park."""
    month_ratings = defaultdict(list)
    for review in data:
        if review['Branch'] == park and review['Year_Month'] != 'missing':
            try:
                month = datetime.strptime(review['Year_Month'], '%Y-%m').strftime('%B')
                month_ratings[month].append(int(review['Rating']))
            except ValueError:
                continue

    # Order months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    result = {month: sum(ratings) / len(ratings) for month, ratings in month_ratings.items()
              if ratings}
    return {month: result.get(month, 0) for month in months_order if month in result}