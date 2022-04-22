import shutil
import os
import functions1
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

### Tkinter Window

class window(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Backup to server")

    # User Textbox description
        self.lblTitle = tk.Label(self.master,text='User Directory:')
        self.lblTitle.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0),sticky=N+W)

    # User Textbox 
        self.labelTxt = tk.Entry(self.master,width=60,text='')
        self.labelTxt.grid(row = 1,column = 0,rowspan = 1,columnspan = 2,padx = (30,40),pady = (0,10),sticky = N+E+W)

    # "Set User" button
        self.button = Button(self.master, text = "Set User Directory", width = 5,
                               command=lambda: functions1.file_pathA(self))
        self.button.grid( row = 4, column = 0, columnspan = 1, pady=(0,0), padx = (30,40), sticky = W+E+N+S)

        self.labelModified = tk.Label(self.master,text='')
        self.labelModified.grid(row=5,column=0,columnspan=2,padx=(27,0),pady=(0,30),sticky=N+W)


    
    # Server Textbox description 
        self.lblTitle1 = tk.Label(self.master,text='Server Directory:')
        self.lblTitle1.grid(row=6,column=0,columnspan=2,padx=(27,0),pady=(10,0),sticky=N+W)

    # Server Textbox 
        self.labelTxt1 = tk.Entry(self.master,width=60, text='')
        self.labelTxt1.grid(row = 7,column = 0,rowspan = 1,columnspan = 2,padx = (30,40),pady = (0,10),sticky = N+E+W)

    # "Set Server" button
        self.button1 = Button(self.master, text = "Set Server Directory", width = 5,
                               command=lambda: functions1.file_pathB(self))
        self.button1.grid( row = 8, column = 0, columnspan = 1, pady=(0,0), padx = (30,40), sticky = W+E+N+S)

        self.labelModified1 = tk.Label(self.master,text='')
        self.labelModified1.grid(row=9,column=0,columnspan=2,padx=(27,0),pady=(0,30),sticky=N+W)

        

    # "Update" button
        self.btn_update = tk.Button(self.master,width=12,height=2,text='Manual Check',
                                    command=lambda: functions1.move_files(self))
        self.btn_update.grid(row=9,column=0,padx=(30,0),pady=(50,10),sticky=W)
        

def main(): 
    window().mainloop()
if __name__ == '__main__':
    main()
