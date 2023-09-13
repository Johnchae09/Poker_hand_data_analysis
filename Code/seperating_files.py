# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:45:00 2023

@author: chaeh
"""

import os

current_script_path = os.path.dirname(__file__)
# Define your source and destination folders
source_folder = os.path.join(current_script_path, "OSS 83L 4,000GTD")

# Function to create a new hand file and write hand content to it
def create_new_hand_file(hand_number, hand_content):
    hand_filename = f"hand {hand_number}.txt"
    with open(os.path.join(source_folder, hand_filename), "w") as hand_file:
        hand_file.write(hand_content)

# Initialize variables
hand_number = 509
hand_content = ""

# Iterate through the lines of the source text file
with open(os.path.join(source_folder, "HH20230908 SCHEDULEDID-G30419922T145 TN-OSS #83L - $4,000 GTD GAMETYPE-Hold'em LIMIT-no CUR-REAL OND-F BUYIN-0.txt"), "r") as source_file:
    for line in source_file:
        if line.startswith("Game Hand #"):
            # If a new hand starts, create a new hand file
            if hand_content:
                create_new_hand_file(hand_number, hand_content)
                hand_number += 1
                hand_content = ""
        hand_content += line

# Create a new hand file for the last hand
if hand_content:
    create_new_hand_file(hand_number, hand_content)