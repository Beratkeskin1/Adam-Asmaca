import tkinter as tk
import turtle as t
from tkinter import messagebox

screen= t.Screen()
t.hideturtle()
FONT_turtle = ("arima",10,"bold")
FONT = ("arima",25,"bold")

kelime_label = tk.Label(text="bir kelime oluşturun:",font=FONT_turtle)
kelime_label.pack()

kelime_entry = tk.Entry(width=50)
kelime_entry.pack()

class Keliemeleri_belirle:
    def __init__(self):
        self.pos = []
        self.yanlış_harfler = []
        self.tekrar = []
        self.aynı_harf = set()
        self.harfleri_tut = set()

    def kelime_oluştur(self,kelime):
        if len(kelime) == 0:
            messagebox.showinfo("BOŞ YAZI HATASI ","lütfen bir yazı yazın ")
        else:
            for harf in kelime:
                t.forward(40)
                t.penup()
                t.forward(-20)
                t.pendown()
                self.pos.append(t.pos())
                t.penup()
                t.forward(30)
                t.pendown()
            kelime_entry.forget()
            kelime_belirleme_butonu.forget()
            kelime_label.forget()
    def harf_tahmin(self,kelime):
        tahmin = harf_tahmin_entry.get().lower()
        bulundumu = False
        if not tahmin  and not not kelime:
            messagebox.showinfo("BOŞ HARF HATASI ", "lütfen bir harf girin ")
            bulundumu = True
        elif not kelime and not tahmin:
            messagebox.showinfo("BOŞ İNDEXLER HATASI", "lütfen bir kelime belirleyin ve sonra da harf belirleyin")
            bulundumu = True
        elif not not tahmin and not kelime:
            messagebox.showinfo("BOŞ KELİME HATASI", "lütfen bir kelime seçin")
            bulundumu = True
        if len(tahmin) == 1:
            if tahmin in self.aynı_harf:
                messagebox.showinfo(title="AYNI HARF HATASI",message="LÜTFEN FARKLI BİR HARF GİRİN")
                return

            for bölüm,harf in enumerate(kelime):
                if harf == tahmin:
                    x,y = self.pos[bölüm]
                    t.penup()
                    t.setx(int(x))
                    t.pendown()
                    t.write(harf_tahmin_entry.get(),font=FONT)
                    bulundumu = True
                    self.aynı_harf.add(tahmin)
                    self.harfleri_tut.add(bölüm)
            if bulundumu:
                if all(kelime[i] in self.aynı_harf for i in range(len(kelime))):
                    harf_tahmin_entry.destroy()
                    harf_tahmin_button.destroy()
                    harf_tahmin_label.destroy()
                    messagebox.showinfo(title="OYUNU KAZANDIN!",message="TEBRİKLER OYUNU KAZANDINIZ")
                    t.bye()
            if len(self.harfleri_tut) != len(kelime):
                harf_tahmin_entry.delete(0, tk.END)

                        ###  KAFA    ###
                if bulundumu == False and 0 not in self.tekrar:
                    self.tekrar.append(0)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200,150)
                    t.pendown()
                    t.circle(30)
                    t.penup()
                    t.sety(0)
                    t.pendown()
                    harf_tahmin_entry.delete(0, tk.END)
                    t.penup()
                    t.setx(0)
                    t.sety(0)
                    t.pendown()                ### GÖVDE ###
                if bulundumu == False and  tahmin not in self.yanlış_harfler  and 1 not in self.tekrar:
                    self.tekrar.append(1)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200,150)
                    t.pendown()
                    t.right(90)
                    t.forward(100)
                    harf_tahmin_entry.delete(0, tk.END)
                    t.penup()
                    t.setx(0)
                    t.sety(0)
                    t.pendown()                ### SAĞ KOL ###
                if tahmin not in self.yanlış_harfler and bulundumu == False and 2 not in self.tekrar :
                    self.tekrar.append(2)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200,130)
                    t.pendown()
                    t.left(45)
                    t.forward(45)
                    harf_tahmin_entry.delete(0, tk.END)
                    t.penup()
                    t.setx(0)
                    t.sety(0)
                    t.pendown()                ### SOL KOL ###
                if tahmin not in self.yanlış_harfler and 3 not in self.tekrar and bulundumu == False:
                    self.tekrar.append(3)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200, 130)
                    t.pendown()
                    t.left(-90)
                    t.forward(45)
                    harf_tahmin_entry.delete(0, tk.END)
                    t.penup()
                    t.setx(0)
                    t.sety(0)
                    t.pendown()
                    ### SAĞ BACAK ###
                if tahmin not in self.yanlış_harfler and 4 not in self.tekrar and bulundumu == False:
                    self.tekrar.append(4)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200,50)
                    t.pendown()
                    t.right(5)
                    t.forward(50)
                    harf_tahmin_entry.delete(0, tk.END)
                    t.penup()
                    t.setx(0)
                    t.sety(0)
                    t.pendown()
                if tahmin not in self.yanlış_harfler and 5 not in self.tekrar and bulundumu == False:
                    self.tekrar.append(5)
                    self.yanlış_harfler.append(tahmin)
                    t.penup()
                    t.goto(-200,50)
                    t.pendown()
                    t.left(95)
                    t.forward(50)
                    harf_tahmin_entry.delete(0, tk.END)
                    harf_tahmin_entry.destroy()
                    harf_tahmin_button.destroy()
                    harf_tahmin_label.destroy()
                    t.penup()
                    t.goto(50,100)
                    t.pendown()
                    t.write("OYUNU KAYBETTİNİZ",font=FONT)
                    messagebox.showinfo(title="OYUNU KAYBETTİN",message="OYUNU KAYBETTİNİZ")
                    t.bye()
        elif len(tahmin) > 0:
            messagebox.showinfo(title="YAZININZ UZUN",message="LÜTFEN YALNIZCA BİR HARF GİRİN")

Kelimeleri_belirle = Keliemeleri_belirle()
kelime_belirleme_butonu = tk.Button(text="seç",command=lambda:Kelimeleri_belirle.kelime_oluştur(kelime_entry.get().lower()) )
kelime_belirleme_butonu.pack()

harf_tahmin_label = tk.Label(text="BİR HARF TAHMİNİNDE BULUNUN",font=FONT_turtle)
harf_tahmin_label.pack()

harf_tahmin_entry = tk.Entry(width=50,)
harf_tahmin_entry.pack()

harf_tahmin_button = tk.Button(text="Tahmin et",command=lambda:Kelimeleri_belirle.harf_tahmin(kelime_entry.get().lower()))
harf_tahmin_button.pack()

k = t.Turtle()

k.speed(0)
k.pensize(2)
screen.bgcolor("#4e4f30")
screen.setup(1000,800)
k.penup()
k.goto(x=-300,y=-10)
k.pendown()
k.left(-20)
k.forward(30)
k.penup()
k.goto(x=-300,y=-10)
k.pendown()
k.right(120)
k.forward(30)
k.hideturtle()
k.penup()
k.goto(x=-300,y=-10)
k.pendown()
k.right(130)
k.forward(240)
k.right(90)
k.forward(100)
k.right(90)
k.forward(20)
t.penup()
t.forward(-100)
t.pendown()
screen.mainloop()