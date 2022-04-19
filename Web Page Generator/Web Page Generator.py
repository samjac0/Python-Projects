import webbrowser
import tkinter

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

#open and read the file after the appending:
f = open("webGenerator.html", "r")
print(f.read())

webbrowser.open_new("webGenerator.html")
