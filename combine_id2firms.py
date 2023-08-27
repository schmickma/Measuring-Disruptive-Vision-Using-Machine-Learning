import os
import csv

# Set folder path and csv file path
folder_path = 'C:/Users/...'
csv_file_path = 'C:/Users/...'

# Create a list to hold the file names
file_names = []

# Loop through the files in the folder and extract the file names
for file in os.listdir(folder_path):
    if file.endswith('.txt'):
        # Split the file name into parts using the delimiter '_'
        file_parts = file.split('_')
        # Add the parts to the list of file names
        file_names.append(file_parts)

# Write the list of file names to the csv file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Column 1', 'Column 2', 'Column 3'])
    for name_parts in file_names:
        writer.writerow(name_parts)
