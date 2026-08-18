# Automated File Sorter

It became time consuming to have to sort through my downloads folder manually trying to find various files so I wrote this Python script.

## The Problem
Download folders rapidly become cluttered. When you have hundreds of files mixed together, finding specific files becomes increasingly difficult.

## The Solution
Run this script to scan the current directory it's placed in, making folders for each file type, and moving the files into them. 

### Key Features
* **Runs Anywhere:** Relying on `__file__` means no hardcoded paths. Put it wherever you need it.
* **Prevents Data Loss:** Duplicate protection is built in. If a file already exists in the target folder, the script ignores it to prevent accidental overwrites.
* **Native Python:** Strictly uses built-in modules (`os`, `shutil`). No pip installs required.

## Usage
1. Place `file_sorter.py` into the target directory.
2. Execute the script via terminal or IDE.
3. The script will automatically skip itself, generate the necessary extension folders, and safely route the appropriate files.
