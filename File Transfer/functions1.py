import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import main
import os.path, time
import datetime





### Moves Files

def move_files(self):
    folderA = self.labelTxt.get()
    folderB = self.labelTxt1.get()


    #set where the source of the files are
    source = folderA

    #set destination
    destination = folderB
    files = os.listdir(source)



    for i in files:
        today = datetime.datetime.today()
        print (today)
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(source + i))
        print (modified_date)
        duration = today - modified_date
        print (duration)
        if duration.seconds < 24*3600:
        # we are saying move the files representer by 'i' to thier new destination
            shutil.copy(source+i, destination)

### Opens Directories, sets "last modified" text, and 

    
def file_pathA(self):
    mydir = tk.filedialog.askdirectory()
    self.labelTxt.delete(0,END)
    self.labelTxt.insert(0,mydir + '/')
    mycheck = time.ctime(os.path.getmtime(mydir))


    ## Not-used code
    #self.labelModified.config(text = "last modified: {}".format(mycheck))
    #mycheck = os.path.getmtime(mydir)
    #return mycheck
    ##
    


def file_pathB(self):
    mydir = tk.filedialog.askdirectory()
    self.labelTxt1.delete(0,END)
    self.labelTxt1.insert(0,mydir + '/')
    mycheck = time.ctime(os.path.getmtime(mydir))


if __name__ == '__main__':
    pass

