#Author: Luke Kellett
import os
import shutil
from path import Path


def startmessage():
    print("You are about to delete all files starting in '._' and .DS_Store files on the selected drive")
    print("this also includes the folders '.Trashes', '.Spotlight-V100, and '.fseventsd'.")
    print("Please select your chosen drive with the letter associated with it")
    print("Operations will begin as soon as drive is selected")

def start():
    choice = input("Input a letter to choose a Drive (such as C, D, E ect.): ")
    #Basic check to see if string input is a letter, and is one character in length.
    if choice.isalpha() == True and len(choice) == 1:
        choice = choice.upper()
        walkfiles(choice)
    else:
        print("Error: Incorrect drive letter input.")
        replay()

#responsible for all file deletion activities
def walkfiles(drive):
    text_file = open("deletedfiles.txt", "w", encoding="utf-8")
    fpath = drive + r':\.fseventsd'
    spath = drive + r':\.Spotlight-V100'
    tpath = drive + r':\.Trashes'

    if os.path.exists(fpath):
        shutil.rmtree(fpath)
        text_file.write('.fseventsd Folder Deleted\n')
   
    if os.path.exists(spath):
        shutil.rmtree(spath)
        text_file.write('.Spotlight-V100 Folder Deleted\n')
   
    if os.path.exists(tpath):
        shutil.rmtree(tpath)
        text_file.write('.Trashes Folder Deleted\n')

    p = Path(drive + ':/')
    filenum = 0
    pathlist = []
    for root, dirs, files in os.walk(p):
        for file in files:
            if file is not file.startswith('$') and file.startswith('._') or file.startswith('.DS_Store'):
                filenum =+ 1
                fullpath = os.path.join(root, file)
                pathlist.append(fullpath)
                text_file.write(fullpath + '\n')
                os.remove(fullpath)

    text_file.close()
    if filenum == 0:
        print("No files were found or deleted.")
    else:
        print("Operation successful! " + str(filenum) + " file(s) deleted. A list of deleted files can be found in deletedfiles.txt")

def replay():
    start()
    
    
startmessage()
start()
