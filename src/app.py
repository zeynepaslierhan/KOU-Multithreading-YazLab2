from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

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

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="İstenilen verileri \n giriniz",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)


        #---------- Sütun Bilgileri -------

        self.combobox_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                    values=["Product", "Issue"])
        self.combobox_1.grid(row=2, column=0, pady=10, padx=20)

        self.combobox_2 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                    values=["2. Sütun","Product", "Issue"])
        self.combobox_2.grid(row=3, column=0, pady=10, padx=20)


        #----- THREAD SAYISI ----
    
        
        self.entry = customtkinter.CTkEntry(master=self.frame_left,
                                            width=120,
                                            placeholder_text="Thread Sayısı")
        self.entry.grid(row=4, column=0, pady=10, padx=20)

        def change(val):
            print(str(val))
                     
        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info,)
        self.progressbar.grid(row=7, column=0, sticky="ew", padx=10, pady=10)
            
        self.slider_2 = customtkinter.CTkSlider(master=self.frame_left,
                                                command=change,
                                                from_=0,
                                                to=100
                                                )
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2.set(0.7)
        self.progressbar.set(0.5)
        

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="ARA",
                                                border_width=2,
                                                fg_color=None,
                                                command=self.button_event)
        self.button_1.grid(row=7, column=0, pady=20, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")


    def button_event(self):
        self.label_mode2 = customtkinter.CTkLabel(master=self.frame_left,text="" + str(self.entry.get()))
        self.label_mode2.grid(row=6, column=0, pady=0, padx=20, sticky="w")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()