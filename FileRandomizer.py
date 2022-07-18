import os
from tabnanny import check


# TODO Add Content

# Create a list of all the files in the folder
fileList = []

for file in os.listdir("/"):
    if os.path.isfile(file):
        print("Found file: ", file)
        fileList.append(file)


# Assert all the files have the same file extension
checkExt = os.path.splitext(fileList[0])

for file in fileList:
    _, ext = os.path.splitext(file)
    assert ext==checkExt, "Error Asserting filenames. Are the files the same type?"

# Generate md5 for all the files

# Shuffle the filenames

# Verify the files still have the same md5