import json
import csv

# Load the JSON data
with open('azure/azure.json', 'r') as json_file:
    data_centers = json.load(json_file)

# Open a CSV file for writing
with open('azure/azure_data_centers.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['region', 'latitude', 'longitude'])
    
    # Iterate over each data center entry in the JSON data
    for dc in data_centers:
        display_name = dc.get('displayName')
        metadata = dc.get('metadata', {})
        latitude = metadata.get('latitude')
        longitude = metadata.get('longitude')
        
        # Write the row to the CSV file
        csv_writer.writerow([display_name, latitude, longitude])
