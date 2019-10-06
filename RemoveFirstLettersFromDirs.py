import os

# Define a folder to iterate through the files recursively
folder_path = 'dir_path'


def replace_first_letters(folder_path, text, text_size):
    for path, subdirs, files in os.walk(folder_path):
        for dir_name in subdirs:
            if dir_name[:text_size] == text:
                dir_path = os.path.join(path, dir_name)
                new_name = os.path.join(path, dir_name.replace(dir_name[:text_size], ''))
                os.rename(dir_path, new_name)


text = 'TU '
text_size = 3

replace_first_letters(folder_path, text, text_size)
