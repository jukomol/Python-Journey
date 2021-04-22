from tkinter import *
from backend import Database

database=Database("books.db")

class Window(object):

    def __init__(self,window):

        self.window = window

        Label(window, text="Title",width=6).grid(row=0,column=0,padx=5,pady=5)
        Label(window, text="Author",width=6).grid(row=1,column=0,padx=5,pady=5)
        Label(window, text="Year",width=6).grid(row=0,column=2,padx=5,pady=5)
        Label(window, text="ISBN",width=6).grid(row=1,column=2,padx=5,pady=5)

        self.title_value=StringVar()
        self.title_entry=Entry(window, textvariable=self.title_value)
        self.title_entry.grid(row=0, column=1,padx=5,pady=5)

        self.author_value=StringVar()
        self.author_entry=Entry(window, textvariable=self.author_value)
        self.author_entry.grid(row=1, column=1,padx=5,pady=5)

        self.year_value=StringVar()
        self.year_entry=Entry(window, textvariable=self.year_value)
        self.year_entry.grid(row=0, column=3,padx=5,pady=5)

        self.isbn_value=StringVar()
        self.isbn_entry=Entry(window, textvariable=self.isbn_value)
        self.isbn_entry.grid(row=1, column=3,padx=5,pady=5)

        self.list1=Listbox(window, height=10, width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2,padx=5,pady=5)

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1=Button(window,text="View all", width=14,command=self.view_command)
        b1.grid(row=2,column=3,pady=5)

        b2=Button(window,text="Search Entry", width=14,command=self.search_command)
        b2.grid(row=3,column=3,pady=5)

        b3=Button(window,text="Add Entry", width=14, command=self.add_command)
        b3.grid(row=4,column=3,pady=5)

        b4=Button(window,text="Update Selected", width=14,command=self.update_command)
        b4.grid(row=5,column=3,pady=5)

        b5=Button(window,text="Delete Selected", width=14,command=self.delete_command)
        b5.grid(row=6,column=3,pady=5)

        b6=Button(window,text="Close", width=14,command=window.destroy)
        b6.grid(row=7,column=3,pady=5)


    def get_selected_row(self,event):
        try:
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.title_entry.delete(0,END)
            self.title_entry.insert(END,self.selected_tuple[1])

            self.author_entry.delete(0,END)
            self.author_entry.insert(END,self.selected_tuple[2])

            self.year_entry.delete(0,END)
            self.year_entry.insert(END,self.selected_tuple[3])

            self.isbn_entry.delete(0,END)
            self.isbn_entry.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())


window=Tk()
window.resizable(0,0)
window.title("JU's Library")
window['background']='#8c8c8c'
Window(window)
window.mainloop()
