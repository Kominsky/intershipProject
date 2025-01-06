import os
import shutil

def organinize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename) #Print the file names to see if the loop is working


#testing the function
organinize_files("/Users/jakobkominsky/Desktop/test_directory/test_files")
