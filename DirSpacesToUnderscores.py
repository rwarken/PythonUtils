import os

# Define a folder to iterate through the files recursively
folder_path = 'E:/Studying/Python Projects/PythonUtils/XML-files/'


def empty_spaces(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for dir_name in subdirs:
            dir_path = os.path.join(path, dir_name)
            new_name = os.path.join(path, dir_name.replace(' ', '_'))
            os.rename(dir_path, new_name)


empty_spaces(folder_path)
