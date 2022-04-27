import sqlite3
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('files.db')

with conn: #this checks for a database and 'fileTypes' table. If neither exists, create.
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileTypes( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileNameExt TEXT \
        )")
    conn.commit()
conn.close

conn = sqlite3.connect('files.db')

with conn: #The following adds each filetype into the column
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('Hello.txt'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('myImage.png'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('myMovie.mpg'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('World.txt'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES (?)", \
                ('myPhoto.jpg'))
    conn.commit()
conn.close()

conn = sqlite3.connect('files.db')

with conn: # This selects all files that include .txt annd displays them in a list
    cur = conn.cursor()
    cur.execute("SELECT col_fileNameExt FROM tbl_fileTypes WHERE col_fileNameExt = '.txt'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "Files that match your inquiry = {}.".format(item[0])
    print(msg)
                
