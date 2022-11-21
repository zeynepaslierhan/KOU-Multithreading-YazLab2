from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.title("Python Read CSV FILE")
width = 1200
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0) 
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Product", "Issue", "Company"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
tree.heading('Product', text="Product", anchor=W)
tree.heading('Issue', text="Issue", anchor=W)
tree.heading('Company', text="Company", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

    
filepath = "C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv"
    
with open(filepath) as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Product = row['Product']
        Issue = row['Issue']
        Company = row['Company']
        tree.insert("", 0, values=(Product, Issue, Company))

if __name__ == '__main__':
    root.mainloop()