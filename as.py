
from tkinter import *

from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Message Box')

#Databases
# Create a databases or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()


# Create table

c.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      city text,
      state text,
      zipcode integer
) """)


# Create submit button for databases
def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO address_book VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })

    conn.commit()

    conn.close()

    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    # Loop through the results
    print_record=''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1])+ ' ' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)


    conn.commit()
    conn.close()

def delete():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + del_entry.get())
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
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Create edit function to update a record
def edit():

    global editor

    editor = Tk()
    editor.title('Update Data')
    editor.geometry('300x480')

    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = del_entry.get()

    # query of the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

    records = c.fetchall()

    #Creating global variable for all text boxes
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor



    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=3, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1)



    # Create textbox labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State")
    state_label.grid(row=3, column=0)

    zipcode_label = Label(editor, text="Zip Code")
    zipcode_label.grid(row=4, column=0)

    # loop through the results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0, record[5])






    # Create a update button
    edit_btn = Button(editor, text=" SAVE ", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)



# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=3, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1)

del_entry = Entry(root, width=30)
del_entry.grid(row=8,column=1)

# Create textbox labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=3, column=0)


zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=4, column=0)

del_id_label = Label(root, text= "Delete ID")
del_id_label.grid(row=8 ,column=0 )

# Create submit button

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create query button

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create delete id button

del_btn = Button(root, text="Delete", command=delete)
del_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create update button to update data

update_btn = Button(root, text="Update", command=edit)
update_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# commit change
conn.commit()

# close connection
conn.close()





mainloop()