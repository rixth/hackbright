import os
import os.path
import shutil

# This is used to determine whether the string starts with something
# print astring.startswith("Hello")

"""
create 26 directories in the current directory, one for each letter of the alphabet, './a/'
loop through all files in original_files directory
organize files into the directory that their name starts with

"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

base = "/Users/trix/workspace/hackbright/wk1_day3/Week_1_Project"
out_dir = base + "/out/"

for letter in letters:
    for filename in os.listdir(base + "/original_files/files"):
        if filename.startswith(letter):
            if os.path.exists(out_dir + letter) == False:
                os.mkdir(out_dir + letter)
            shutil.move(base + "/original_files/files/" + filename, out_dir + letter + "/" + filename)
