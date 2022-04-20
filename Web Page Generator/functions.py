import webbrowser
from tkinter import *
import tkinter as tk
import webPageGenerator

def createWebsite(self):
    var_subbmittedText = self.labelTxt.get()
    name = open("webGenerator.html", "w")
    name.write("""
    <html>
        <body>
            <h1>
            {}
            </h1>
        </body>
    </html> """.format(var_subbmittedText))
    name.close()

#This lauches a window on button click
def viewWebsite(self):
    webbrowser.open_new("webGenerator.html")




if __name__ == '__main__':
    pass

