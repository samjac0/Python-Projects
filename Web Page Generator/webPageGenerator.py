import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import functions


class window(Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Web Generator")
# Textbox line
        self.labelTxt = tk.Entry(self.master,text='')
        self.Txt.grid(row = 1,column = 0,rowspan = 2,columnspan = 1,padx = (30,40),pady = (0,0),sticky = N+E+W)

# "Submit changes" button
        self.button1 = Button(self, text = "Sumbit changes", width = 25,
                               command=lambda: functions.createWebsite(self))
        self.button1.grid( row = 3, column = 1, columnspan = 1, sticky = W+E+N+S)
# "View" button
        self.button2 = Button(self, text = "View", width = 25,
                               command=lambda: functions.viewWebsite(self))
        self.button2.grid( row = 3, column = 2, columnspan = 1, sticky = W+E+N+S)

    #def close_window(self):
        #self.destroy()
def main(): 
    window().mainloop()
if __name__ == '__main__':
    main()

