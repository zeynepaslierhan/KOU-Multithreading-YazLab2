import mutlithreading as th

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter


customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 900
    HEIGHT = 500

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
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right,)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor" ,
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT,
                                                   )
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


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