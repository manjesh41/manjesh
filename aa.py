from tkinter import *
root=Tk()
def edit():

    global editor

    editor = Tk()
    editor.title('Update Data')
    editor.iconbitmap('E:/images/global.ico')
    editor.geometry('300x480')

    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    # query of the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

    records = c.fetchall()
    # print(records)
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


root.mainloop()
