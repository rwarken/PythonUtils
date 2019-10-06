import os

# Define a folder to iterate through the files recursively
folder_path = 'dir_path'


def replace_ext(folder_path, old_ext, new_ext):
    for path, subdirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(path, file_name)
            new_name = os.path.join(path, file_name.replace(old_ext, new_ext))
            os.rename(file_path, new_name)


old_ext = '.XML'
new_ext = '.xml'

# Define the extensions to change to lowercase
replace_ext(folder_path, old_ext, new_ext)
