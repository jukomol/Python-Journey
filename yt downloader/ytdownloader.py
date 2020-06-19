from tkinter import *
from tkinter import ttk
import time
import youtube_dl,os


window=Tk()
window.resizable(0,0)
window.title("YT DOWNLOADER")
window['background']='#8c8c8c'

progressbar=ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='determinate')

def step():
    global l1
    progressbar['value']=100
    l1=Label(window, text="Downloaded",width=12)
    l1.grid(row=5,column=1,padx=5,pady=5)
    #progressbar.start(5)
    '''
    for i in range(5):
        progressbar['value'] +=20
        window.update_idletasks()
        time.sleep(1)
            '''

def clearText():
    title_entry.delete(0,'end')
    progressbar.stop()
    l1.destroy()


def ytdownload():
    yd = {}
    path = path_link.get()
    os.chdir(path)
    url = yt_link.get()
    with youtube_dl.YoutubeDL(yd) as y:
        y.download([url])
        step()

Label(window, text="LINK",width=6).grid(row=0,column=0,padx=5,pady=5)
Label(window, text="PATH",width=6).grid(row=1,column=0,padx=5,pady=5)


yt_link=StringVar()
title_entry=Entry(window, textvariable=yt_link)
title_entry.grid(row=0, column=1,padx=5,pady=5,columnspan=3)

path_link=StringVar()
path_entry=Entry(window, textvariable=path_link)
path_entry.grid(row=1, column=1,padx=5,pady=5,columnspan=3)

b1=Button(window,text="Download", width=14,command=ytdownload)
b1.grid(row=3,column=1,pady=5)

b2=Button(window,text="Clear", width=14,command=clearText)
b2.grid(row=3,column=2,pady=5,padx=5)

progressbar.grid(row=4,column=1,pady=5,columnspan=4)

window.mainloop()
