import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import functions


class window(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Web Generator")
# Textbox description heading
        self.lblTitle = tk.Label(self.master,text='Use this text box to update your website text:')
        self.lblTitle.grid(row=0,column=0,columnspan=2,padx=(27,0),pady=(10,0),sticky=N+W)
# Textbox 
        self.labelTxt = tk.Entry(self.master,text='')
        self.labelTxt.grid(row = 1,column = 0,rowspan = 3,columnspan = 3,padx = (30,40),pady = (0,10),sticky = N+E+W)
# "Submit changes" button
        self.button1 = Button(self.master, text = "Sumbit changes", width = 25,
                               command=lambda: functions.createWebsite(self))
        self.button1.grid( row = 4, column = 0, columnspan = 1, sticky = W+E+N+S)
# "View" button
        self.button2 = Button(self.master, text = "View", width = 25,
                               command=lambda: functions.viewWebsite(self))
        self.button2.grid( row = 4, column = 1, columnspan = 1, sticky = W+E+N+S)

    #def close_window(self):
        #self.destroy()
def main(): 
    window().mainloop()
if __name__ == '__main__':
    main()

