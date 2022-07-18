# FileRandomizer
## A short programm to randomize the files in a given folder
This program was developed in one night. To shuffle the filenames inside of a folder around. Without altering any of the files other information or contents.

### Usage
- Download the FileRandomizer.py file from this repository.
- Move the File into a folder with the files you want to randomise
- Either double click the file or run it from the console with: 
```
py FileRandomizer.py
```

### Goals
- [✔] Run the software by placing it inside the folder with the files to be renamed and excecute it with no runtime arguments

- [✔] Check if all of the files have the same file format, abbort execution if the files formats do not match

- [❌] After Shuffling create a output.log file that lists the mapping of the randomised files or displays an error log
Replaced this with just having the regular console log output. File creation would interfere with the file format restriction
- [❌] Keep the files contens md5 accurate (Maybe test that after shuffling automatically)
File hashing would need to open the whole file. This can lead to memory issues on bigger files and im lazy. 

### Lessons Learned
- Win+. brings up the emoji selector.
- Random chance can feel like not truly random when using a small set
- camelCase is not for python
- current working directory is referenced with "." as its path
