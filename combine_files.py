import os

# Define the folder path where the text documents are located
folder_path = 'C:/Users/.../'

# Define the name of the new combined text file
new_file_name = 'document.txt'

# Create a new empty text file with the given name
with open(new_file_name, 'w', encoding='utf-8') as new_file:
    # Get a list of all the file names in the folder
    file_names = os.listdir(folder_path)
    # Loop through each file name in the list
    for file_name in file_names:
        # Open the text file in read mode
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8', errors='replace') as text_file:
            # Read the contents of the text file
            text = text_file.read().replace('\n', ' ')
            # Write the contents of the text file to the new file
            new_file.write(text + '\n')
