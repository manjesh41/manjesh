from tkinter import *
import sqlite3
root=Tk()

root.title('database')
conn=sqlite3.connect('school_book.db')
root.geometry('420x600')
root.configure(background='black')
#create cursor
#cursor class is an instance using which

c=conn.cursor()
'''
#creat table
c.execute("""CREATE TABLE school_book(first_name text,
last_name text,
address text,
zipcode integer
)""") 
print('Table created successfully')'''
def submit():
    conn=sqlite3.connect('school_book.db')
    c=conn.cursor()
    c.execute('INSERT INTO school_book VALUES(:f_name,:l_name,:address,:zip)',{
        'f_name':f_name.get(),
        "l_name":l_name.get(),
        'address':address.get(),
        'zip':zip.get()
    })
    print('School inserted successfully')
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    zip.delete(0,END)
def record():
    conn=sqlite3.connect('school_book.db')
    c=conn.cursor()
    c.execute('SELECT*,oid FROM school_book')
    record=c.fetchall()
    print(record)
    #loop
    print_record=""
    for record in record:
        print_record+=str(record)+'\n'
    show_recordlabel=Label(root,text=print_record,bg='orange').grid(row=6,column=1)
    conn.commit()
    conn.close()
def delete():
    # Create a databases or connect to one
    conn = sqlite3.connect('school_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from school_book WHERE oid = " + del_entry.get())
    print("deleted sucessfully")

    # query of databases
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    # Loop through the results
    print_record = ''
    for record in records:
        print_record +=  str(record[0]) + ' ' + str(record[1]) + '' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=7, column=0, columnspan=3)

    conn.commit()
    conn.close()



name=Label(root,text='FIRST NAME:',font='lucid 10 bold',bg='blue',fg='white').grid(row=0,column=0,pady=10,padx=10,ipadx=30,ipady=7)
f_name=Entry(root,font='lucid 10 bold')
f_name.grid(row=0,column=1,pady=10,padx=10,ipadx=30,ipady=7)
last1=Label(root,text='LAST NAME:',font='lucid 10 bold',bg='blue',fg='white').grid(row=1,column=0,pady=10,padx=10,ipadx=30,ipady=7)
l_name=Entry(root,font='lucid 10 bold')
l_name.grid(row=1,column=1,pady=10,padx=10,ipadx=30,ipady=7)
add1=Label(root,text='ADDRESS:',font='lucid 10 bold',bg='blue',fg='white').grid(row=2,column=0,pady=10,padx=10,ipadx=30,ipady=7)
address=Entry(root,font='lucid 10 bold')
address.grid(row=2,column=1,pady=10,padx=10,ipadx=30,ipady=7)
zipcode1=Label(root,text='zipcode:',font='lucid 10 bold',bg='blue',fg='white').grid(row=3,column=0,pady=10,padx=10,ipadx=30,ipady=7)
zip=Entry(root,font='lucid 10 bold')
zip.grid(row=3,column=
1,pady=10,padx=10,ipadx=30,ipady=7)
button=Button(root,text='SUBMIT',command=submit,font='lucid 10 bold',bg='red',fg='white').grid(row=4,column=1,pady=10,padx=10,ipadx=30,ipady=7)
show_record=Button(root,text='SHOW RECORD',command=record,font='lucid 10 bold',bg='red',fg='white').grid(row=5,column=1,pady=10,padx=10,ipadx=30,ipady=7)
del_id_label = Label(root, text= "Delete ID")
del_id_label.grid(row=8 ,column=0 )

del_btn = Button(root, text="Delete", command=delete)
del_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=30)
#commit change
conn.commit()
conn.close()
mainloop()
