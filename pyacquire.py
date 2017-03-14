import os
import sys
import fnmatch
import re

# Get directory to recursively search from argument list
directory = sys.argv[1]
# Get file type to search
fileType = sys.argv[2]
# Get string to search for
searchItem = sys.argv[3]

# Setup matches list to hold all files with specified string
matches = []

# Search all files with specified type in directory, check if the given string is contained within them
# and then add to matches list
for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, '*.' + fileType):
        item = open(os.path.join(root, filename), 'r')
        line = item.read()
        if re.search(searchItem, line) != None:
            matches.append(os.path.join(root, filename))


for match in matches:
    print match