import os

# Define a folder to iterate through the files recursively 
folder_path = 'my_local_path/'


def emptySpaces(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(path, file_name)
            new_name = os.path.join(path, file_name.replace(' ', '_'))
            os.rename(file_path, new_name)

emptySpaces(folder_path)
