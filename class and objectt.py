from tkinter import *
import sqlite3
root=Tk()

root.title('database')
conn=sqlite3.connect('school_book.db')
root.geometry('420x600')
root.configure(background='black')

class Elder:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.Pack()

        self.myButton=Button(master,text='CLICK ME', command=self.clicker)

    def clicker(self):
        print('BUTTON CLICKED')
e=Elder(root)
root.mainloop()