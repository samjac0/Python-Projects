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

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileTypes(col_fileNameExt) VALUES(?)", (x,))
            print(x)
conn.close()
