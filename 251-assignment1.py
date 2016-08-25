import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import *
import sys
import time
from odf import text, teletype
from odf.opendocument import load
import win32print, win32gui, win32ui, win32con


# When you press the button of the textarea, this function will
# put the corresponding textarea to the top layer to display and
# operate.
def display_textarea(num):
    global textAreaList
    global textButtonList
    global current_textarea

    #find out the corresponding textarea according to the button
    for i in range(len(textAreaList)):
        if(num == textButtonList[i]['text']):
            #put the corresponding textarea to the toplevel of the window
            current_textarea=textAreaList[i]
            
            mywindow.grid_slaves(1, 0)[0].grid_forget()
            textAreaList[i].grid(row=1,column=0,columnspan=100)
            break

# This function is used to respond the press of New-Button
def create_newtext():
    global textAreaList
    global textButtonList
    global current_textarea
    global textID

    #add a new textarea to the window
    t = tk.Text(mywindow,height=50, width=150)
    textAreaList.append(t)
    current_textarea=textAreaList[len(textAreaList)-1]

    #add a new button in the window to select the corresponding textarea
    b = tk.Button(mywindow,text="text"+str(textID), command= lambda : display_textarea(b['text']))
    textButtonList.append(b)
    
    textID= textID+1

    #update the array of button and textarea
    for i in range(len(textButtonList)):
        textButtonList[i].grid(row=0,column=i,sticky="W")

    #put the new textarea on the top layer to display    
    if(len(textAreaList)>1):
        mywindow.grid_slaves(1, 0)[0].grid_forget()
    textAreaList[len(textAreaList)-1].grid(row=1,column=0,columnspan=100)

    return textAreaList[len(textAreaList)-1]
    

#function of finding a specific word in the text
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


#Function for print
def do_print_qu():
    str1=current_textarea.get("0.0","end")
    pname=win32print.GetDefaultPrinter()
    pHandle=win32print.OpenPrinter(pname)
    printinfo=win32print.GetPrinter(pHandle,2)

    pDevModeObj=printinfo["pDevMode"]
    pDevModeObj.Scale=100

    DC=win32gui.CreateDC("WINSPOOL",pname,pDevModeObj)
    hDC= win32ui.CreateDCFromHandle(DC)

    hDC.StartDoc("Python Editor")
    hDC.StartPage()
    hDC.TextOut(20,20,str1)
    hDC.EndPage()
    hDC.EndDoc()

    win32gui.DeleteDC(DC)

#when the software start, this function will run first. it builds the window and put menus on the top of it and also put the first textarea in it
def init_window(tk):
    #build the window
    window = tk.Tk()
    window.title('myEditor');
    window.geometry('1000x600')

    #build the menu
    menubar = tk.Menu(window)

    #file menu
    filemenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=filemenu)

    filemenu.add_command(label='New',command=create_newtext)
    filemenu.add_command(label='Open',command=openFile)
    filemenu.add_command(label='Save',command=saveFile)
    filemenu.add_command(label='Print', command=do_print_qu)
    filemenu.add_separator()
    filemenu.add_command(label='Exit',command=window.destroy)

    #search menu
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

    #help menu
    helpmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Help',menu=helpmenu)
    helpmenu.add_command(label='About',command=popupAbout)
    helpmenu.add_command(label='T&&D',command=getTimeAndDate)
   
    
    window.config(menu=menubar)

    return window

#used to create a new fresh textarea
def openFile():
    filename = tk.filedialog.askopenfilename(initialdir ='C:\\Users\\shanyi\\Desktop\\251-a1-yishan-jasonqu')

    if len(filename)==0:
        print("open file for reading is cancelled.")
        return
    
    filetype=filename.split(".")
    filetype=filetype[len(filetype)-1]
    
    if(filetype=="txt"):  
        try:
            file=open(filename,'r')
            
            t=create_newtext()
            t.insert('end',file.read())
            file.close()
        except IOError as e:
            print(e,filename)
    elif(filetype=="odt"):
        textdoc = load(filename)
        allparas = textdoc.getElementsByType(text.P)

        t=create_newtext()
        for i in range(len(allparas)):
            t.insert('end',teletype.extractText(allparas[i]))
    else:
        tk.messagebox.showinfo( title='Unsupported file type',
                        message='This is unsupported file type, now the supported file type are .txt and .odt')

    
            

#save the content in the textarea into a .txt file    
def saveFile():
    global textAreaList
    global current_textarea
    
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
    
#provide the information of the software and authors
def popupAbout():
    tk.messagebox.showinfo( title='About the Authors of Editor',
                            message='This editor is made by YiShan & JasonQu, if you have any question, please e-mail huifeidepangzi@gmail.com')

#insert the current time and date to the top of current textarea
def getTimeAndDate():
    var = time.strftime('%H:%M %d-%m-%Y',time.localtime(time.time()))
    current_textarea.insert('0.0',var)

#used to record which textarea is current textarea    
current_textarea= None
#the number of textarea
textID=0
#the list of textarea
textAreaList=[]
#the list of button of textarea
textButtonList=[]
#init the window
mywindow=init_window(tk)
#create the first textarea when the window is createdv
create_newtext()

mywindow.mainloop()
