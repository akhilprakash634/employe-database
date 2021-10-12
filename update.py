from tkinter import*
import tkinter.messagebox
from PIL import ImageTk,Image
from subprocess import call


t=Tk()
t.title('Employe Data')
t.geometry('500x500')

i=Image.open("L:\\employe_tkinter\\bg.jpg")
i=i.resize((500,500))
i=ImageTk.PhotoImage(i)
img=Label(t,image=i)
img.place(x=0,y=0)



Label(text='UPDATE',bg="#008000").place(x=220,y=60)

Label(text='Enter name to update: ',bg="#ffa500").place(x=100,y=110)
use=Entry()
use.place(x=250,y=110)
Label(text='Enter place to update: ',bg="#ffa500").place(x=100,y=150)
upl=Entry()
upl.place(x=250,y=150)
Label(text='Enter age to update: ',bg="#ffa500").place(x=100,y=190)
uag=Entry()
uag.place(x=250,y=190)

def update():
    import pymysql
    x=pymysql.connect(host="localhost",user="root",password="Appu@2001",database="employee")
    cur=x.cursor()
    uptn=use.get()
    uptp=upl.get()
    upta=uag.get()
    
    cur.execute('update employe set place=%s,age=%s where name=%s',(uptp,upta,uptn))
    x.commit()
    x.close()
    t.mainloop()
    
Button(text='Apply',bg="skyblue",command=update).place(x=400,y=190)

Label(text='DELETE',bg="#800080").place(x=220,y=240)
Label(text='Enter Employe to delete: ',bg="#ffa500").place(x=100,y=290)
de=Entry()
de.place(x=250,y=290)

def delete():
    import pymysql
    x=pymysql.connect(host="localhost",user="root",password="Appu@2001",database="employee")
    cur=x.cursor()
    dele=de.get()
    cur.execute('delete from employe where name=%s',dele)
    x.commit()
    x.close()
    t.mainloop()
    
Button(text='Delete',bg="#ff0000",command=delete).place(x=400,y=290)

def home():
    t.destroy()
    call(['python','tkinter grud.py'])
Button(text='Back to Home',bg="#008000",command=home).place(x=220,y=410)




t.mainloop()     
