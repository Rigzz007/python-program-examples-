from tkinter import *
import mysql.connector
import tkinter.messagebox as msg


def create_conn():
    return mysql.connector.connect(
              host="localhost",
              user="root",
              password="",
              database="python_t"
    )

#print(create_conn())

def insert():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert status","All fields are mendatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert status","Data inserted successfully")
    #print("insert called")
def search():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')

    if e_id.get()=="":
        msg.showinfo("Search status","Id is mandatory for search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showinfo("search status","id not found")
        conn.close()
    #print("search called")
def update():
    print("update called")
def delete():
    print("delete called")


root = Tk()
root.title("my tkinter example")
root.geometry("320x350")
root.resizable(width=False,height=False)  #width and height is not working for this so false is writen

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="GMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)


insert=Button(root,text="INSERT",fg="white",bg="black",font=("Arial",10),command=insert)
insert.place(x=20,y=300)

search=Button(root,text="SEARCH",fg="white",bg="black",font=("Arial",10),command=search)
search.place(x=80,y=300)

update=Button(root,text="UPDATE",fg="white",bg="black",font=("Arial",10),command=update)
update.place(x=148,y=300)

delete=Button(root,text="DELETE",fg="white",bg="black",font=("Arial",10),command=delete)
delete.place(x=214,y=300)

root.mainloop()