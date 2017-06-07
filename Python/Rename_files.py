import os
def rename_files():
    #1 get name of files from the folder
    file_names = os.listdir(r'/Users/jinzegu/Downloads/prank')
    print file_names
    save_dir = os.getcwd()
    os.chdir(r'/Users/jinzegu/Downloads/prank')
    #2 for each file, rename name
    for name in file_names:
        os.rename(name, name.translate(None, '0123456789'))
        print(name)
    os.chdir(save_dir)

rename_files()
