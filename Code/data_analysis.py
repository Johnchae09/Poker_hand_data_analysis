# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:44:30 2023

@author: chaeh
"""

import os

# Define the directory path containing your text files
directory_path = "OSS 83L 4,000GTD"

searchVpip = ["JohnChae0929 calls", "JohnChae0929 raises "]

searchBBDef = ["JohnChae0929 posts the big blind" , "JohnChae0929 calls"]

PostBB = "JohnChae0929 posts the big blind"
vpipCount = 0;
handCount = 0
BBDefFreq = 0
BBFreq = 0

# Function to search for the strings in a file
def search_in_file(file_path, search_strings):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            found_strings = []
            for search_string in search_strings:
                if search_string in content:
                    found_strings.append(search_string)
            return found_strings
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return []

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  # Check if the file is a text file
        handCount += 1
        file_path = os.path.join(directory_path, filename)
        foundVpip = search_in_file(file_path, searchVpip)
        foundBBDef = search_in_file(file_path, searchBBDef)
        foundBB = search_in_file(file_path, PostBB)
        if foundVpip:
            vpipCount +=1
        if foundBBDef:
            BBDefFreq +=1
        if foundBB:
            BBFreq += 1
            

Vpip = vpipCount / handCount
BBDef = BBDefFreq / BBFreq
