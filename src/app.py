from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import *
import csv
import multithreading as mt
import create_LastData as lstData
        

root = Tk()
root.title("Python Read CSV FILE")
width = 1200
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

def degiskenal():
    
    val_thread = entry1.get()
    val_threshold = entry2.get()
    val_columns = option1.get()
    
    if val_columns == 'Product':
        val_columns = 1
        
    elif val_columns == 'Issue':
        val_columns = 2
        
    else: 
        val_columns =3
        
    mt.searching_with_mutlithreading(int(val_columns),int(val_threshold),int(val_thread))
    
    lstData.lastData()
    filepath = "C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/LastData.csv"
    
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Product = row['Complaint ID 1']
            Issue = row['Complaint ID 2']
            Company = row['threshold']
            tree.insert("", 0, values=(Product, Issue, Company))

frame1 = Frame(root)
frame1.pack(side=TOP, fill=BOTH)


choices = ['Product', 'Issue', 'Company']
variable = StringVar(root)
variable.set('Product')

label0 = tkinter.Label(frame1, text= "Sütun Seçiniz:")
label0.pack(side=LEFT,pady=10,padx=20)

option1= Combobox(frame1, values = choices)
option1.pack(side=LEFT,padx=1,pady=10)



label1 = tkinter.Label(frame1, text="Thread Sayısı:")
label1.pack(side=LEFT,padx=30,pady=10)

entry1 = tkinter.Entry(frame1,)
entry1.pack(side=LEFT,padx=1,pady=10)



label2 = tkinter.Label(frame1, text="Benzerlik Oranı:")
label2.pack(side=LEFT,padx=30,pady=10)

entry2 = tkinter.Entry(frame1,)
entry2.pack(side=LEFT,padx=1,pady=10)



button2=tkinter.Button(frame1,text="ARA",height=2,width=20,background="lightgray",command=degiskenal)
button2.pack(side=LEFT,padx=50,pady=10)



TableMargin = Frame(root, width=700)
TableMargin.pack(side=TOP,pady=50)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Complaint ID 1", "Complaint ID 2", "threshold"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
tree.heading('Complaint ID 1', text="Complaint ID 1", anchor=W)
tree.heading('Complaint ID 2', text="Complaint ID 2", anchor=W)
tree.heading('threshold', text="threshold", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=250)
tree.column('#2', stretch=NO, minwidth=0, width=250)
tree.column('#3', stretch=NO, minwidth=0, width=250)
tree.pack()



try:
    filepath = "C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/LastData.csv"
    
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Product = row['Complaint ID 1']
            Issue = row['Complaint ID 2']
            Company = row['threshold']
            tree.insert("", 0, values=(Product, Issue, Company))
except:
    print("CSV Dosyası Bulunamadı!")

root.mainloop()