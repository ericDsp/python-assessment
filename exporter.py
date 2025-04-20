# exporter.py
import json
import csv


class DataExporter:
    """Class to export aggregate data in multiple formats."""

    def __init__(self, data):
        """Initialize with dataset."""
        self.data = data
        self.aggregate_data = self._aggregate_data()

    def _aggregate_data(self):
        """Aggregate data for each park."""
        result = {}
        for review in self.data:
            park = review['Branch']
            rating = int(review['Rating'])
            location = review['Reviewer_Location']

            if park not in result:
                result[park] = {
                    'review_count': 0,
                    'positive_reviews': 0,
                    'total_rating': 0,
                    'locations': set()
                }

            result[park]['review_count'] += 1
            result[park]['total_rating'] += rating
            result[park]['locations'].add(location)
            if rating >= 4:
                result[park]['positive_reviews'] += 1

        for park in result:
            result[park]['average_rating'] = (result[park]['total_rating'] /
                                              result[park]['review_count'])
            result[park]['location_count'] = len(result[park]['locations'])
            del result[park]['locations']  # Remove set for export
            del result[park]['total_rating']  # Remove temporary field

        return result

    def export_data(self, format_type):
        """Export data in the specified format."""
        if format_type == 'TXT':
            self._export_to_txt()
        elif format_type == 'CSV':
            self._export_to_csv()
        elif format_type == 'JSON':
            self._export_to_json()
        else:
            print("Invalid format. Please choose TXT, CSV, or JSON.")

    def _export_to_txt(self):
        """Export data to a TXT file."""
        with open('disneyland_export.txt', 'w') as f:
            for park, stats in self.aggregate_data.items():
                f.write(f"Park: {park}\n")
                f.write(f"Number of Reviews: {stats['review_count']}\n")
                f.write(f"Positive Reviews: {stats['positive_reviews']}\n")
                f.write(f"Average Rating: {stats['average_rating']:.2f}\n")
                f.write(f"Number of Countries: {stats['location_count']}\n")
                f.write("-" * 40 + "\n")

    def _export_to_csv(self):
        """Export data to a CSV file."""
        with open('disneyland_export.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Park', 'Review Count', 'Positive Reviews',
                             'Average Rating', 'Number of Countries'])
            for park, stats in self.aggregate_data.items():
                writer.writerow([park, stats['review_count'],
                                 stats['positive_reviews'],
                                 stats['average_rating'],
                                 stats['location_count']])

    def _export_to_json(self):
        """Export data to a JSON file."""
        with open('disneyland_export.json', 'w') as f:
            json.dump(self.aggregate_data, f, indent=4)