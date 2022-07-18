import hashlib
import os
import random
import sys
import time

# Create a list of all the files in the folder
fileList = []

for file in os.listdir("."):
    if os.path.isfile(file):
        fileList.append(file)

# Remove the python script file
print(os.path.basename(__file__))
fileList.remove(os.path.basename(__file__))

# Assert all the files have the same file extension
_, checkExt = os.path.splitext(fileList[-1])
print("Ensuring filetype: ", checkExt)

for file in fileList:
    _, ext = os.path.splitext(file)
    print("Found file: ", file)
    assert ext==checkExt, \
        "Error Asserting filenames. Are the files the same type?"

# Generate md5 for all the files
# md5List = []
# for file in fileList:
#     # Loading the whole file like this is not good
#     md5List.append(hashlib.md5(open(file).read().encode('utf-8')))

# Shuffle the filenames
random.seed(str(time.monotonic_ns))
randFileList = random.sample(fileList, k=len(fileList))
randFileList.reverse()


# Rename the files
for orig, rand in zip(fileList, randFileList):
    print("Renaming: ", orig, " -> ", rand)
    os.rename(orig, "temp_" + rand)

# Remove the temp tag from the files after renaming
for file in randFileList:
    os.rename("temp_" + file, file)

# Verify the files still have the same md5
# randMd5List = []
# for file in randFileList:
#     # Same memory issue as previously
#     randMd5List.append(hashlib.md5(open(file).read().encode('utf-8')))

# for a, b in zip(md5List, randMd5List):
#     if a!=b: print("Error", end="")
#     print("A: {0} B: {1}", a, b)