import os
import shutil

current_script_path = os.path.dirname(__file__)
# Define your source and destination folders
source_folder = os.path.join(current_script_path, "hands from 09_08")
destination_folder = os.path.join(current_script_path, "OSS 83L 4,000GTD")

# Define the specific string you want to search for in file names
specific_string = "OSS #83L - $4,000 GTD"

# Iterate through the files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".txt") and specific_string in filename:
        # Move the file to the destination folder
        shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
