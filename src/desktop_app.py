import tkinter as tk
from tkinter import *

# form oluştu
form = tk.Tk()


# Uygulama Oluşturma ve Tasarlama

# pencere boyutu ayarlandı ve ekranın hangi kısmında açılacağı belirlendi
form.geometry('500x250+500+350')

# min/max ölçüyü belirlemek için 
# form.minsize()
# form.maxsize()

# pencere ölçüsünün değiştirilebilir olması x,y
form.resizable(False,True)

# forma başlık eklendi
form.title("KOU Yazlab1 Multithreading")

# pencere saydamlaştırma için
form.wm_attributes('-alpha',0.7)


# Tablo oluşturma

data=Frame()






# masaüstü uygulaması çalıştırıldı
def start():
    form.mainloop()