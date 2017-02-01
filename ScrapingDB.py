from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3

try :
    conn=sqlite3.connect('Project.db')
    c=conn.cursor()

    c.execute("CREATE TABLE Dictionary(Words text,Length real,First_char text,Last_char)")

          

    url1=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
    n=len(url1)

    url2=[10,8,14,8,6,6,4,5,5,2,1,6,7,3,4,10,1,6,16,8,3,2,6,0,1,1]

    list=[]
    for i in range(0,n) :
        for j in range(1,url2[i]+1) :
            url=urlopen("http://learnersdictionary.com/3000-words/alpha/"+url1[i]
                    +"/"+str(j))
            soup=BeautifulSoup(url,"html.parser")
        #print("http://learnersdictionary.com/3000-words/alpha/"+url1[i]+"/"+str(j))
        

            bc=soup.find(class_="a_words").get_text().strip()
            list.append(bc.split())

    x=len(list)
    print(x)


    for i in range(0,x) :
        for words in list[i][:] :
            if words.startswith('(') or words.endswith(')') :
                list[i].remove(words)

    list_new=[]


    for i in range(0,x) :
        for words in list[i][:] :
            if words not in list_new :
                list_new.append(words)

    y=len(list_new)    


    for i in range(0,y) :
        #for words in list_new[:] :
            #print(words,len(words),words[0],words[-1])
        c.execute("INSERT INTO Dictionary VALUES(?,?,?,?);",(list_new[i],len(list_new[i]),list_new[i][0],list_new[i][-1]))
        conn.commit()

   
    c.execute("SELECT * FROM Dictionary")
    data=c.fetchall()

    for row in data :
        print(row)
    print("Done")

   

except sqlite3.Error :
    if c:
        conn.rollback()
        
            






