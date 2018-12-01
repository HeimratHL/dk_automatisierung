'''
Created on 01.12.2018

@author: Anton

@note: Imports pictures from portable drives to '/assets'
'''
from shutil import copy2
from _overlapped import NULL
import os, sys


sourcepath = os.path.join('E:\\')
destpath = os.path.join('D:\\', 'Desktop', 'pyfolder', 'activeSite', 'assets')
allowed_fileextensions = ['.mp4', '.tff', '.png','.gif']
    
#checks a list of filenames and returns a list without bad filetypes
def checkFiles(names):
    checked = []
    allowed_extset = set(allowed_fileextensions)
    error = False
    
    for i in names:
        #splits the filename into name -> NULL and extension -> ext
        NULL, ext = os.path.splitext(os.path.join(sourcepath, i))
        
        #checks if the extension of file 'i' is in the list of allowed fileextensions and writes the filename into 'checked' if it is
        if ext in allowed_extset:
            checked.append(i)

        else:
            error = True
            
    #Prints out error if input had bad fieltypes.
    if error == True:
        print("Some files havn't been copyied due to a bad fileextension.")
        print("You can change the allowed fileextensions in 'PictureImporter.py' -> 'allowed_fileextensions")
        print("Currently allowed are:")
        print(allowed_fileextensions)

    return checked

#compares the two directorys and adds the intersects to found[]
def compareFiles(src, dst):
    #creates filelist in source and destination
    sourcefiles = set(os.listdir(path=src))
    destfiles = set(os.listdir(path=dst))
    
    #return intersections in the filelists
    setIntersect = sourcefiles.intersection(destfiles)
    return setIntersect

#handles duplicates and can 
def duplicates():
    #checks whether there is a same file in both directorys
    intersects = compareFiles(sourcepath, destpath)
    if(len(intersects) > 0):
        print("We have found " + str(len(intersects)) + " fileduplicates.")
        
        #asks for the users wishes and executes a rename or not
        # !!!!!has to be handled by ui in the future!!!!!
        for i in intersects:
            print("Dupclicate: " + str(i))
            print("Would you like to overwrite the existing file or rename the new one?")
            wtd = input("overwrite/rename?")
            
            if(wtd == "rename"):
                rename(i)


#renames a file if a user prompted to rename a duplicate file
def rename(oldname):
    newname = input("New Name?")
    
    #checks if a file with this name already exists and either calls the method again or renames the file
    if os.path.isfile(os.path.join(destpath, newname)): #duplicate == False:
        print("Name already exists!")
        rename(oldname)
    else:
        os.rename(os.path.join(sourcepath, oldname), os.path.join(sourcepath, newname))
        print("renamed: " + oldname + " -> " + newname)

# MAIN
#checks for and handles found duplicates
duplicates()

#creates a list of the files to copy. This list wont include files with unfitting html formats (i.e. Recycle.bin or anything.jpeg)
copydir = checkFiles(os.listdir(path=sourcepath))

#copies the files from the list above to 'destpath' as defined in the header of this file
for i in copydir:
    try:
        copy2(os.path.join(sourcepath, i), destpath)
        print(i + " copyied.")
    except:
        print("Unexpected error:", sys.exc_info()[0])