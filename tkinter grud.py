from tkinter import*

import tkinter.messagebox
from PIL import ImageTk,Image



t=Tk()
t.title('Employe Data')
t.geometry('500x500')

i=Image.open("L:\\employe_tkinter\\bg.jpg")
i=i.resize((500,500))
i=ImageTk.PhotoImage(i)
img=Label(t,image=i)
img.place(x=0,y=0)



Label(text='Name: ',bg="#ffa500").place(x=30,y=40)
nm=Entry()
nm.place(x=90,y=40)

Label(text='Place: ',bg="#ffa500").place(x=30,y=80)
pl=Entry()
pl.place(x=90,y=80)

Label(text='Age: ',bg="#ffa500").place(x=30,y=120)
ag=Entry()
ag.place(x=90,y=120)


def abcd():
    import pymysql
    x=pymysql.connect(host="localhost",user="root",password="Appu@2001",database="employee")
    cur=x.cursor()
    n=nm.get()
    p=pl.get()
    a=ag.get()
    
    cur.execute('insert into employe values(%s,%s,%s)',(n,p,a))
    x.commit()
    x.close()
    tkinter.messagebox.showinfo('Added','Employe Added suchesfully')
    
    
Button(text='Add Employe',bg="skyblue",command=abcd).place(x=320,y=80)



Label(text='UPDATE',bg="#008000").place(x=220,y=160)

Label(text='Enter name to update: ',bg="#ffa500").place(x=100,y=190)
use=Entry()
use.place(x=250,y=190)
Label(text='Enter place to update: ',bg="#ffa500").place(x=100,y=230)
upl=Entry()
upl.place(x=250,y=230)
Label(text='Enter age to update: ',bg="#ffa500").place(x=100,y=270)
uag=Entry()
uag.place(x=250,y=270)

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
    
Button(text='Apply',bg="skyblue",command=update).place(x=400,y=230)

Label(text='DELETE',bg="#800080").place(x=220,y=300)
Label(text='Enter Employe to delete: ',bg="#ffa500").place(x=100,y=340)
de=Entry()
de.place(x=250,y=340)

def delete():
    import pymysql
    x=pymysql.connect(host="localhost",user="root",password="Appu@2001",database="employee")
    cur=x.cursor()
    dele=de.get()
    cur.execute('delete from employe where name=%s',dele)
    x.commit()
    x.close()
    t.mainloop()
    
Button(text='Delete',bg="#ff0000",command=delete).place(x=400,y=340)

t.mainloop()      
