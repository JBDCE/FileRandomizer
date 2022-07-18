import os
import random
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