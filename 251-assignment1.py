import tkinter as tk

window = tk.Tk()
window.title('myEditor');

window.geometry('1000x600')

l = tk.Label(window, bg='yellow',width=20,text='')
l.pack()
counter=0

def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter+=1

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

searchmenu.add_command(label='Cut',command=do_job)
searchmenu.add_command(label='Copy',command=do_job)
searchmenu.add_command(label='Paste',command=do_job)

viewmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='View',menu=viewmenu)

helpmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)

t = tk.Text(window,height=100, width=100)
t.pack()
# t.selection_get()


window.config(menu=menubar)

window.mainloop()

tk.se
