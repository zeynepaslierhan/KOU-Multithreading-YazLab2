import mutlithreading as th
from pathlib import Path
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter
import csv


customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 1200
    HEIGHT = 800

    def __init__(self):
        super().__init__()

        self.title("Mutlithreading")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame_right.rowconfigure(10, weight=14)
        self.frame_right.columnconfigure((0, 1), weight=0,)
        self.frame_right.columnconfigure(2, weight=0)

        #self.frame_info = customtkinter.CTkFrame(master=self.frame_right,)
        #self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=6, pady=20, padx=20, sticky="nsew")
        
        
        
        

        # ============ frame_info ============

        # configure grid layout (1x1)
        #self.frame_info.rowconfigure(0, weight=1)
        #self.frame_info.columnconfigure(0, weight=1)

        #self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
         #                                          text="CTkLabel: Lorem ipsum dolor sit,\n" +
          #                                              "amet consetetur sadipscing elitr,\n" +
           #                                             "sed diam nonumy eirmod tempor" ,
            #                                       height=100,
             #                                      corner_radius=6,  # <- custom corner radius
              #                                     fg_color=("white", "gray38"),  # <- custom tuple-color
               #                                    justify=tkinter.LEFT,
                #                                   )
        #self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        
        filepath = "C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv"
        
        File = open(filepath)
        Reader = csv.reader(File)
        Data = list(Reader)
        del(Data[0])
        
        list_of_entries = []
        for x in list (range(0,len(Data))):
            list_of_entries.append(Data[x][0])
            
        
        self.Product_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Product")
        self.Product_Label.grid(row=0, column=0,sticky="w",)
        
        self.Issue_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Issue")
        self.Issue_Label.grid(row=0, column=1,sticky="w",)
        
        self.Company_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Company")
        self.Company_Label.grid(row=0, column=2,sticky="w")
        
        self.ZIP_code_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="ZIP code")
        self.ZIP_code_Label.grid(row=0, column=3,sticky="w",)
        
        self.State_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="State")
        self.State_Label.grid(row=0, column=4,sticky="w",)
        
        self.Complaint_ID_Label = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Complaint ID")
        self.Complaint_ID_Label.grid(row=0, column=5,sticky="w",)
        
        
        
        
        self.Product_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Product")
        self.Product_Label2.grid(row=0, column=0,sticky="w",)
        
        self.Issue_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Issue")
        self.Issue_Label2.grid(row=0, column=1,sticky="w", )
        
        self.Company_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Company")
        self.Company_Label2.grid(row=0, column=2,sticky="w",)
        
        self.ZIP_code_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="ZIP code")
        self.ZIP_code_Label2.grid(row=0, column=3,sticky="w",)
        
        self.Product_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="State")
        self.Product_Label2.grid(row=0, column=4,sticky="w", )
        
        self.Complaint_ID_Label2 = customtkinter.CTkLabel(master=self.frame_right,width=75,fg_color="white",text="Complaint ID")
        self.Complaint_ID_Label2.grid(row=0, column=5,sticky="w",)


        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(15, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="İstenilen verileri \n giriniz",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.Sütun1= customtkinter.CTkOptionMenu(master=self.frame_left,
                                                    values=["Product", "Issue"])
        self.Sütun1.grid(row=2, column=0, pady=10, padx=20)
    
        
        self.ThreadSayısı = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="Thread Sayısı")
        self.ThreadSayısı.grid(row=4, column=0, pady=10, padx=20)

        self.BenzerlikOranı_Label = customtkinter.CTkLabel(master=self.frame_left,width=150,fg_color="white",text="Benzerlik Oranı : %50")
        self.BenzerlikOranı_Label.grid(row=5, column=0,pady=10)
            
        self.BenzerlikOranı_Slider = customtkinter.CTkSlider(master=self.frame_left,
                                                command=self.change,
                                                from_=0,
                                                number_of_steps=10,
                                                to=100
                                                )
        self.BenzerlikOranı_Slider.grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="ARA",
                                                border_width=2,
                                                fg_color=None,
                                                command=self.search_button_event)
        self.button_1.grid(row=10, column=0, pady=20, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=13, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=14, column=0, pady=10, padx=20, sticky="w")
    
    
    def change(self,val):
        self.BenzerlikOranı_Label = customtkinter.CTkLabel(master=self.frame_left,width=150,fg_color="white",text="Benzerlik Oranı : %"+str(int(val)))
        self.BenzerlikOranı_Label.grid(row=5, column=0,pady=10)


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    
    def search_button_event(self):
        similarityValue=self.BenzerlikOranı_Slider.get()
        columsValue = self.Sütun1.get()
        threadValue= int(self.ThreadSayısı.get())

        th.threading(columsValue,similarityValue,threadValue)

        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    
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
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Product', text="Product", anchor=W)
    tree.heading('Issue', text="Issue", anchor=W)
    tree.heading('Company', text="Company", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    
    
    filepath = "C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv"
    
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Product = row['Product']
            Issue = row['Issue']
            Company = row['Company']
            tree.insert("", 0, values=(Product, Issue, Company))

if __name__ == '__main__':
    root.mainloop()