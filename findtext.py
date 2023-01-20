import easygui
import os
# open a directory dialog
path = easygui.diropenbox(
    title='Select a base directory to scan for text'
)
# check if pressed cancel
if path == None: exit()
# get which type of file they're scanning for
file_extension = input('what type of file do you want to search for (e.g. \'.txt\'): ')
# get what text they are looking for
search_text = input('what text are you looking for: ')
# check if left empty
if file_extension == "":
    print('searching for any filetype')
occurences = 0
# scan through all directories from base
for root, dirs, files in os.walk(path):
    # scan through all files in directory
    for file in files:
        # check if file ends with given extension
        if not str(file).endswith(file_extension):
            continue
        try:
            with open(f'{root}\\{file}', 'r+') as f:
                try:
                    # iterate through all lines in file
                    for i, line in enumerate(f.readlines()):
                        # check if text is on line
                        if search_text in line:
                            print(f'{root}\\{file}:{i+1}')
                            occurences += 1
                except: pass
        except: pass
print(f'found {occurences} occurences.')