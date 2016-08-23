import tkinter as tk
import sys
    

def display_textarea(num):
    print(num)
    for i in range(len(textAreaList)):
        if(num == textButtonList[i]['text']):
            print(i)
            mywindow.grid_slaves(1, 0)[0].grid_forget()
            current_textarea=textAreaList[i]
            global current_textarea
            print(current_textarea.get("0.0","end"))
            
            textAreaList[i].grid(row=1,column=0,columnspan=100)
            break

def create_newtext():
    t = tk.Text(mywindow,height=50, width=150)
    textAreaList.append(t)

    b = tk.Button(mywindow,text="text"+str(textID), command= lambda : display_textarea(b['text']))
    
    textButtonList.append(b)
    
    textID= textID+1
    global textID
    for i in range(len(textButtonList)):
        textButtonList[i].grid(row=0,column=i,sticky="W")
    #for i in range(len(textButtonList)):
    if(len(textAreaList)>1):
        mywindow.grid_slaves(1, 0)[0].grid_forget()
    textAreaList[len(textAreaList)-1].grid(row=1,column=0,columnspan=100)

    return textAreaList[len(textAreaList)-1]
    

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

    window.config(menu=menubar)

    return window

def openFile():
    filename = tk.filedialog.askopenfilename(initialdir ='C:\\Users\\shanyi\\Desktop\\251-a1-yishan-jasonqu')
    print(filename)
    file=open(filename,'r')
    t=create_newtext()
    t.insert('end',file.read())
    file.close()


def saveFile():
    filename = tk.filedialog.asksaveasfilename(initialdir ='C:\\Users\\shanyi\\Desktop\\251-a1-yishan-jasonqu')
    print(filename)
    file=open(filename,'w')
    file.write(current_textarea.get("0.0","end"))
    file.close()
    
current_textarea= None  
mywindow=init_window(tk)
textAreaList=[]
global textAreaList
textButtonList=[]
global textButtonList
textID=0



mywindow.mainloop()






