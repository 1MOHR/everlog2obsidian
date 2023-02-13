# everlog2obsidian
A script to convert an Everlog.json to individual .md files for use in Obsidian.

## This script will:
1. Read the .json file exported from everlog
2. Extract each entry and create a seperate .md file for it (unless they happened on the same day, in that case they just get combined)
3. Links images to the bottom of each .md file if the entry has them
4. Adds an "on this day" feature to the top of each .md file (you much have dataview enabled in Obsidian for this to work)

## Usage:
1. Download it
2. Put everlog2obsidian into the same folder as your .json file
3. Rename the .json file to journal.json
4. Run everlog2obsidian
5. Take the .md files from the "output" folder and put them wherever your daily note folder is in obsidian
6. Take the images from the everlog export and put them wherever you have obsidian set up to put attachments
