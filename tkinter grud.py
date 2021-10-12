from tkinter import*
import tkinter.messagebox
from PIL import ImageTk,Image
from subprocess import call
import pymysql
x=pymysql.connect(host="localhost",user="root",password="Appu@2001",database="employee")
cur=x.cursor()


t=Tk()
t.title('Employe Data')
t.geometry('500x500')

i=Image.open("L:\\employe_tkinter\\bg.jpg")
i=i.resize((800,500))
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
    
    
Button(text='Add Employe',bg="skyblue",command=abcd).place(x=130,y=160)

def updatepage():
    
    t.destroy()
    call(['python','update.py'])

Button(text='UPDATE',bg="#008000",command=updatepage).place(x=160,y=210)


cur.execute('select * from employe')
data=cur.fetchall()
vn=[','.join(map(str,xd))for xd in data]

def viewdata():
    tx=Text(height=10,width=25)
    tx.place(x=260,y=40)
    tx.delete('1.0',END)
    for i in vn:
        tx.insert(INSERT,('%s\n\n'%i))
    
    
    
Button(text='Refresh Data',bg="#008000",command=viewdata).place(x=260,y=210)
x.close()
t.mainloop()      
