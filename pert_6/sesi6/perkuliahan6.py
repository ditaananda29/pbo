from tkinter import *
import time


class Jam:
    def _init_(self, parent):
        self.parent = parent
        self.komponen()
        self.perbaui()
    def komponen(self):
        self.teksJam = StringVar()
        self.teks = Label(text="Kodingbagus", bg ="white")
        self.teks.pack()
        layarJam = Frame(self.parent, bd=10)
        layarJam.pack()
        self.jam = Label(layarJam, textvariable=self.teksJam,font=('Helvetica', 40, 'bold'),bg = "light blue",fg="blue")
        self.jam.pack()
    def perbaui(self):
        datJam = time.strftime("%H:%M:%S", time.localtime())
        self.teksJam.set(datJam)
        self.timer = self.parent.after(1000, self.perbaui)
if _name_ == '_main_':
    root = Tk()
    root.title("jam digital")
    app = Jam(root)
    root.mainloop()