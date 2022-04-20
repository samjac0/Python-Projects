import webbrowser
import tkinter as tk
import webPageGenerator

def createWebsite(self):
    name = open("webGenerator.html", "w")
    name.write("""
    <html>
        <body>
            <h1>
            Stay tuned for our amazing summer sale!
            </h1>
        </body>
    </html> """)
    name.close()

def viewWebsite(self):
    webbrowser.open_new("webGenerator.html")

if __name__ == '__main__':
    main()
