import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import *
import sys
import time
import win32ui



def display_textarea(num):
    global textAreaList
    global textButtonList
    for i in range(len(textAreaList)):
        if(num == textButtonList[i]['text']):
            print(i)
            mywindow.grid_slaves(1, 0)[0].grid_forget()

            global current_textarea
            current_textarea=textAreaList[i]
            
            print(current_textarea.get("0.0","end"))
            
            textAreaList[i].grid(row=1,column=0,columnspan=100)
            break

def create_newtext():
    global textAreaList
    global textButtonList
    global current_textarea
    global textID
    
    t = tk.Text(mywindow,height=50, width=150)
    textAreaList.append(t)
    current_textarea=textAreaList[len(textAreaList)-1]
      
    b = tk.Button(mywindow,text="text"+str(textID), command= lambda : display_textarea(b['text']))
    textButtonList.append(b)
    
    textID= textID+1
        
    for i in range(len(textButtonList)):
        textButtonList[i].grid(row=0,column=i,sticky="W")
    
    if(len(textAreaList)>1):
        mywindow.grid_slaves(1, 0)[0].grid_forget()
    textAreaList[len(textAreaList)-1].grid(row=1,column=0,columnspan=100)


    return textAreaList[len(textAreaList)-1]
    


def do_search_by_qu():
    global current_textarea
    current_textarea.tag_remove('search','1.0','end')
    target =askstring("SimpleEditor",'Search String?',initialvalue='Find a word')
    if target:
        countVar=tk.StringVar()
        pos = current_textarea.search(target,'1.0', stopindex='end', count=countVar,nocase=True)
        if pos:
            sWOrd = '{}+{}c'.format(pos, len(target))
            current_textarea.tag_configure("search", background='green')
            current_textarea.tag_add("search",pos,sWOrd)



def do_nothing():
    return 0

def init_window(tk):
    window = tk.Tk()
    window.title('myEditor');
    window.geometry('1000x600')

    menubar = tk.Menu(window)

    filemenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=filemenu)

    filemenu.add_command(label='New',command=create_newtext)
    filemenu.add_command(label='Open',command=openFile)
    filemenu.add_command(label='Save',command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit',command=window.destroy)

    searchmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Search',menu=searchmenu)
    searchmenu.add_command(label="Cut",\
                           accelerator="Ctrl+x",\
                           command = lambda: \
                                     current_textarea.event_generate('<<Cut>>'))
    searchmenu.add_command(label="Copy",\
                           accelerator="Ctrl+c",\
                           command = lambda: \
                                     current_textarea.event_generate('<<Copy>>'))
    searchmenu.add_command(label="Paste",\
                           accelerator="Ctrl+v",\
                           command = lambda: \
                                     current_textarea.event_generate('<<Paste>>'))
    searchmenu.add_command(label='Search',command=do_search_by_qu)
    
    helpmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Help',menu=helpmenu)
    helpmenu.add_command(label='About',command=popupAbout)
    helpmenu.add_command(label='T&&D',command=getTimeAndDate)
   
    
    window.config(menu=menubar)

    return window

def openFile():
    filename = tk.filedialog.askopenfilename(initialdir ='C:\\Users\\shanyi\\Desktop\\251-a1-yishan-jasonqu')
    
    if len(filename)==0:
        print("open file for reading is cancelled.")
        return
    try:
        file=open(filename,'r')
        print("filename = ",file)
        t=create_newtext()
        t.insert('end',file.read())
        file.close()
    except IOError as e:
        print(e,filename)
    


def saveFile():
    global textAreaList
    
    filename = tk.filedialog.asksaveasfilename(initialdir ='C:\\Users\\shanyi\\Desktop\\251-a1-yishan-jasonqu')
    if len(filename)==0:
        print("open file for writing is cancelled.")
        return
    
    try:
        file=open(filename,'w')
        file.write(current_textarea.get("0.0","end"))
        file.close()
    except IOError as e:
        print(e)
    

def popupAbout():
    tk.messagebox.showinfo( title='About the Authors of Editor',
                            message='This editor is made by YiShan & JasonQu, if you have any question, please e-mail huifeidepangzi@gmail.com')

def getTimeAndDate():
    global textAreaList
   
    var = time.strftime('%H:%M %d-%m-%Y',time.localtime(time.time()))
    current_textarea.insert('0.0',var)
    
current_textarea= None
textID=0
mywindow=init_window(tk)
textAreaList=[]
textButtonList=[]
create_newtext()




mywindow.mainloop()

