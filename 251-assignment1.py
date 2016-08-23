import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import *
# This is my test1.
# from tkinter import messagebox as tkMessagebox

# tkMessagebox.as
# from tkinter import simpledialog as tkSimpleDialog
# from  tkSimpleDialog import askstring

# import ScrolledText

window = tk.Tk()
window.title('myEditor');

window.geometry('1000x600')

l = tk.Label(window, bg='yellow',width=20,text='')
l.pack()

t = tk.Text(window,height=100, width=100)
t.pack()

counter=0

def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter+=1

def do_search_by_qu():
    t.tag_remove('search','1.0','end')
    target =askstring("SimpleEditor",'Search String?',initialvalue='Find a word')
    if target:
        countVar=tk.StringVar()
        pos = t.search(target,'1.0', stopindex='end', count=countVar,nocase=True)
        if pos:
            # print ("pos is :",pos)
            sWOrd = '{}+{}c'.format(pos, len(target))
            t.tag_configure("search", background='green')
            # t.tag_add("search",pos,sWOrd)
            t.tag_add("search",pos,sWOrd)

# def do_j_insert():
#     t.insert('current', "hello,    word" )

# def ClearTags(event):
#
#     t.tag_remove('green','1.0','end')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)

filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

searchmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Search',menu=searchmenu)

# searchmenu.add_command(label='Cut',command=do_job)
searchmenu.add_command(label="Cut",\
                       accelerator="Ctrl+x",\
                       command = lambda: \
                                 t.event_generate('<<Cut>>'))
# searchmenu.add_command(label='Copy',command=do_job)
searchmenu.add_command(label="Copy",\
                       accelerator="Ctrl+c",\
                       command = lambda: \
                                 t.event_generate('<<Copy>>'))
# searchmenu.add_command(label='Paste',command=do_j_insert)
searchmenu.add_command(label="Paste",\
                       accelerator="Ctrl+v",\
                       command = lambda: \
                                 t.event_generate('<<Paste>>'))
searchmenu.add_command(label='Search',command=do_search_by_qu)

viewmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='View',menu=viewmenu)

helpmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)



# searchmenu.add_command(label='Paste',command=do_j_insert())

# t.selection_get()


window.config(menu=menubar)

# t.bind("<Button-1>",ClearTags)

window.mainloop()

