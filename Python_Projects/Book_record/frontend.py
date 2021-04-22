"""
A python program that stores my library books information
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend


window=Tk()
window.resizable(0,0)
window.title("JU's Library")
#window.configure(bg ='#b2beb')
window['background']='#8c8c8c'

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END,selected_tuple[1])

        author_entry.delete(0,END)
        author_entry.insert(END,selected_tuple[2])

        year_entry.delete(0,END)
        year_entry.insert(END,selected_tuple[3])

        isbn_entry.delete(0,END)
        isbn_entry.insert(END,selected_tuple[4])
    except IndexError:
        pass



def search_command():
    list1.delete(0,END)
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    list1.delete(0,END)
    list1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())

Label(window, text="Title",width=6).grid(row=0,column=0,padx=5,pady=5)
Label(window, text="Author",width=6).grid(row=1,column=0,padx=5,pady=5)
Label(window, text="Year",width=6).grid(row=0,column=2,padx=5,pady=5)
Label(window, text="ISBN",width=6).grid(row=1,column=2,padx=5,pady=5)

title_value=StringVar()
title_entry=Entry(window, textvariable=title_value)
title_entry.grid(row=0, column=1,padx=5,pady=5)

author_value=StringVar()
author_entry=Entry(window, textvariable=author_value)
author_entry.grid(row=1, column=1,padx=5,pady=5)

year_value=StringVar()
year_entry=Entry(window, textvariable=year_value)
year_entry.grid(row=0, column=3,padx=5,pady=5)

isbn_value=StringVar()
isbn_entry=Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=1, column=3,padx=5,pady=5)

list1=Listbox(window, height=10, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2,padx=5,pady=5)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All", width=14,command=view_command)
b1.grid(row=2,column=3,pady=5)

b2=Button(window,text="Search Entry", width=14,command=search_command)
b2.grid(row=3,column=3,pady=5)

b3=Button(window,text="Add Entry", width=14, command=add_command)
b3.grid(row=4,column=3,pady=5)

b4=Button(window,text="Update Selected", width=14,command=update_command)
b4.grid(row=5,column=3,pady=5)

b5=Button(window,text="Delete Selected", width=14,command=delete_command)
b5.grid(row=6,column=3,pady=5)

b6=Button(window,text="Close", width=14,command=window.destroy)
b6.grid(row=7,column=3,pady=5)
window.mainloop()
