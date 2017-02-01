from tkinter import *
import tkinter
from PIL import Image,ImageTk
import sqlite3

root=Tk()

image=Image.open("Background.JPG")
tkimage=ImageTk.PhotoImage(image)

w = tkimage.width()
h = tkimage.height()
root.geometry("%dx%d+0+0" % (w, h))

MainLabel=Label(root,image=tkimage)
MainLabel.pack(side='top', fill='both', expand='yes')

LabelM1=Label(MainLabel,text="Enter Word :")

val=StringVar()
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()

entry=Entry(MainLabel,textvariable=val)


def click() :
    conn=sqlite3.connect('Project.db')
    c=conn.cursor()

    SimWords=[]
    MeanWords=[]

    InputWord=val.get()
    c.execute("SELECT * FROM Dictionary")
    dataD=c.fetchall()

    c.execute("SELECT * FROM WordMeaning")
    dataWM=c.fetchall()

    flag=0
    i=0    
    j=0
    
    for row in dataD :
        if(row[0] == InputWord) :
            flag=1
            break
        else :
            flag=2

    if(flag==1) :            
        NewFrame1=Toplevel(MainLabel)
        labelNF11=Label(NewFrame1,image=tkimage)
        labelNF11.pack(side='top', fill='both', expand='yes')

    
        MsgExists=Message(labelNF11,textvariable=v1,relief=RAISED)
        v1.set("Word Exists")
        MsgExists.pack()
        for i in dataD :
            if(i[1]==len(InputWord) and i[2]==InputWord[0] and i[3]==InputWord[-1] and i[0]!=InputWord) :
                SimWords.append(i[0])

        k=0

        for j in dataWM :
            if(j[0] == InputWord) :
                k=k+1
                MeanWords.append(str(k))                         
                MeanWords.append(j[1])                                                   
       
    
                           
            
        print("Done")

        MsgSim=Message(labelNF11,textvariable=v2,relief=RAISED)
        v2.set("Similar words : ")
        MsgSim.pack()

        scroll1=Scrollbar(labelNF11)
        scroll1.pack(fill=Y)

        listing1=Listbox(labelNF11,yscrollcommand=scroll1.set,width=50)

        for i in range (0,len(SimWords)):
            listing1.insert(END,SimWords[i])
            
        listing1.pack()
        scroll1.config(command=listing1.yview)
        

        MsgMean=Message(labelNF11,textvariable=v4,relief=RAISED,width=150)
        v4.set("Meanings : ")
        MsgMean.pack()

        scroll2=Scrollbar(labelNF11)
        scroll2.pack(fill=Y)

        listing2=Listbox(labelNF11,yscrollcommand=scroll2.set,width=150)

        for i in range (0,len(MeanWords)):
            listing2.insert(END,MeanWords[i])
            
        listing2.pack()
        scroll2.config(command=listing2.yview)
        

    elif (flag==2) : 
        NewFrame2=Toplevel(MainLabel)
        labelNF21=Label(NewFrame2,image=tkimage)
        labelNF21.pack(side='top', fill='both', expand='yes')

    
        MsgNotExists=Message(labelNF21,textvariable=v6,relief=RAISED)
        v6.set("Word does not exists")
        MsgNotExists.pack()



button=Button(MainLabel,text="OK",command=click)

entry.place(x=625,y=200)

button.place(x=660,y=400)

LabelM1.pack()    

root.mainloop()
