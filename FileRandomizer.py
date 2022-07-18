import hashlib
import os
import random

# Create a list of all the files in the folder
fileList = []

for file in os.listdir("."):
    if os.path.isfile(file):
        print("Found file: ", file)
        fileList.append(file)

# Remove the python script file
fileList.remove(__file__)

# Assert all the files have the same file extension
checkExt = os.path.splitext(fileList[0])

for file in fileList:
    _, ext = os.path.splitext(file)
    assert ext==checkExt, \
        "Error Asserting filenames. Are the files the same type?"

# Generate md5 for all the files
md5List = []
for file in fileList:
    # Loading the whole file like this is not good
    md5List.append(hashlib.md5(open(file).read())) 

# Shuffle the filenames
randFileList = random.sample(fileList)

# This is bad.
# Instead just run the file multiple times
# # Just for good measure
# random.shuffle(ranFileList)
# random.shuffle(ranFileList)
# random.shuffle(ranFileList)
# random.shuffle(ranFileList)

# Rename the files
for orig, rand in zip(fileList, randFileList):
    os.rename(orig, rand)

# Verify the files still have the same md5
randMd5List = []
for file in randFileList:
    # Same memory issue as previously
    randMd5List.append(hashlib.md5(open(file).read()))

for a, b in zip(md5List, randMd5List):
    if a!=b: print("Error", end="")
    print("A: {0} B: {1}", a, b)