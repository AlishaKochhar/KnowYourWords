from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3

conn=sqlite3.connect('Project.db')
c=conn.cursor()

c.execute("CREATE TABLE WordMeaning(Word text,Meaning text)")

c.execute("SELECT * FROM Dictionary")

data=c.fetchall()

for i in range(0,3115) :
    url=urlopen("http://learnersdictionary.com/definition/"+data[i][0])
    soup=BeautifulSoup(url,"html.parser")
    for m in soup.find_all(class_="def_text"):
         c.execute("INSERT INTO WordMeaning VALUES(?,?);",(data[i][0],m.get_text()))
         conn.commit()

        
        
print("Over")
