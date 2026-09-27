"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Florence Z. Sibal]
Date: [09/27/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

- I built a simple Python script that organizes files into different folders based on their file extensions. It makes sorting files easier by automatically putting similar files together.

============================================
KEY VOCABULARY
============================================
- os module: The os module lets Python work with files, folders, and file paths on the computer.
- shutil module: The shutil module helps Python move, copy, and manage files.
- file path: A file path tells Python where a file or folder is located.
- directory: A directory is another name for a folder where files are stored.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        if extension in [".jpg", ".png", ".jpeg"]:
            folder = "Images"
        elif extension in [".pdf", ".docx", ".txt"]:
            folder = "Documents"
        else:
            folder = "Others"

        folder_path = os.path.join(source_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

        shutil.move(file_path, os.path.join(folder_path, file))

print("Files have been sorted successfully!")

# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
 - One mistake I had was making sure the file path was correct before running the script. I learned that checking the folder location first can prevent errors and make the script work properly.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
- This is similar to real automation because a computer can do repetitive tasks for us instead of doing everything manually. For example, a similar script could organize school files like assignments, attendance records, or grade sheets automatically.
"""
