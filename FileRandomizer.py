import os
import random
import time

# Create a list of all the files in the folder
filelist = []

for file in os.listdir("."):
    if os.path.isfile(file):
        filelist.append(file)

# Remove the python script file
print(os.path.basename(__file__))
filelist.remove(os.path.basename(__file__))

# Assert all the files have the same file extension
_, checkext = os.path.splitext(filelist[-1])
print("Ensuring filetype: ", checkext)

for file in filelist:
    _, ext = os.path.splitext(file)
    print("Found file: ", file)
    assert ext==checkext, \
        "Error Asserting filenames. Are the files the same type?"

# Shuffle the filenames
random.seed(str(time.monotonic_ns))
randfilelist = random.sample(filelist, k=len(filelist))
randfilelist.reverse()

# Rename the files
for orig, rand in zip(filelist, randfilelist):
    print("Renaming: ", orig, " -> ", rand)
    os.rename(orig, "temp_" + rand)

# Remove the temp tag from the files after renaming
for file in randfilelist:
    os.rename("temp_" + file, file)