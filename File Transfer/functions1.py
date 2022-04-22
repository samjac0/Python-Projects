import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import main





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
        #we are saying move the files representer by 'i' to thier new destination
        shutil.move(source+i, destination)

### Opens Directories

    
def file_pathA(self):
    mydir = tk.filedialog.askdirectory()
    self.labelTxt.delete(0,END)
    self.labelTxt.insert(0,mydir + '/')


def file_pathB(self):
    mydir = tk.filedialog.askdirectory()
    self.labelTxt1.delete(0,END)
    self.labelTxt1.insert(0,mydir + '/')


if __name__ == '__main__':
    pass

