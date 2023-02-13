import json
import os

# Create output folder if it doesn't exist
if not os.path.exists("output"):
    os.makedirs("output")

# Load data from journal.json
with open("journal.json") as f:
    data = json.load(f)

# Create a dictionary to store filenames based on the entry's identifier
filenames = {}

# Loop through each journal entry
for entry in data["entries"]:
    # Get the entry's content and parent (if it exists)
    content = entry.get("content", "")
    parent = entry.get("parent", None)

    # Get the entry's date and format it as YYYY-MM-DD
    date = entry["dateCreated"][:10]
    filename = f"{date}.md"

    # Store the filename based on the entry's identifier
    filenames[entry["identifier"]] = filename

    # If the entry has a parent, insert a wikilink at the beginning of the content
    if parent:
        parent_filename = filenames[parent]
        content = f"[[{parent_filename[:-3]}]]\n{content}"
    
    # Check if the entry has images
    images = entry.get("images", [])

    # If the entry has images, insert links to each image at the bottom of the content
    if images:
        content = f"{content}\n\n"
        for image in images:
            content = f"{content}![[{image}.jpg]]\n"

    # Get the date portion from the filename
    date_portion = date[-5:]
    
    # Write the entry's content to the corresponding .md file
    with open(f"output/{filename}", "w") as f:
        f.write(f"```dataview\ntable file.mtime as LastEdit\nfrom \"\"\nwhere contains(file.name, \"-{date_portion}\") and !contains(file.name, \"{date[:4]}\")\n```\n{content}")
