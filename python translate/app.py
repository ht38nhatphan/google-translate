
from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

root = Tk()
root.title('gg dich')
root.geometry("510x590")
root.iconbitmap(r'h:\python\file\python translate\logo.ico')

loat = Image.open(r'h:\python\file\python translate\background.jpg')
render = ImageTk.PhotoImage(loat)
img = Label(root,image = render)
img.place(x=0,y=0)

name = Label(root,text= "Translator",fg = '#FFFFFF',bd=0,bg='#010E21')
name.config(font =("Transformers Movie",30))
name.pack(pady=10)

box = Text(root,width = 28,height = 8,font = ("ROBOTO",16))
box.pack(pady=20)
box1 = Text(root,width = 28,height = 8,font = ("ROBOTO",16))
box1.pack(pady=50)
button = Frame(root).pack(side=BOTTOM)
def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    g = Translator()
    t = g.translate(INPUT,scr="vi",dest = "en")
    a = t.text
    box1.insert(END,a)
viet_button = Button(button,text = 'DỊCH',font=(("Arial"),10,'bold'),bg='#303030',fg='#FFFFFF',command=translate)
viet_button.place(x=290,y=310)

clear_button = Button(button,text = 'XÓA',font=(("Arial"),10,'bold'),bg='#303030',fg='#FFFFFF',command=clear)
clear_button.place(x=150,y=310)
root.mainloop()
