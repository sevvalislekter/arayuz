from tkinter import *
from tkcalendar import DateEntry


master=Tk()
canvas=Canvas(master,height=450,width=750)

canvas.pack()

frameust=Frame(master, bg='#add8e6')
frameust.place(relx=0.1,rely=0.1,relwidth=0.75,relheight=0.1)

framealt=Frame(master, bg='#add8e6')
framealt.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)

framesag=Frame(master, bg='#add8e6')
framesag.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)


hatirlat=Label(frameust,bg='#add8e6',text="Hatırlatma tipi",font="verdana 12 bold")

hatirlat.pack(padx=10,pady=10,side=LEFT)

hatirlatop=StringVar(frameust)
hatirlatop.set("\t")

hatirlatac=OptionMenu(frameust,hatirlatop,"dogum gunu","alısveris","odeme")
hatirlatac.pack(padx=10,pady=10,side=LEFT)

hatirsec=DateEntry(frameust,width=12,bg='orange',foreground='black',borderwidth=1,locale="de_DE")
hatirsec._top_cal.overrideredirect(False)

hatirsec.pack(padx=10,pady=10,side=RIGHT)


hatirlat_tarih=Label(frameust,bg='#add8e6',text="Hatırlatma tarihi:",font="Verdana 12 bold")
hatirlat_tarih.pack(padx=10,pady=10,side=RIGHT)



Label(framealt,bg='#add8e6',text="Hatırlatma yontemi",font="verdana 10 bold").pack(padx=10,pady=10,anchor=NW)

var=IntVar()


R1=Radiobutton(framealt,text="sisteme kaydet",variable=var,value=1,bg='#add8e6',font="verdana 10")
R1.pack(anchor=NW,pady=5,padx=15)

R2=Radiobutton(framealt,text="e posta gonder",variable=var,value=2,bg='#add8e6',font="verdana 10")
R2.pack(anchor=NW,pady=5,padx=15)

var1=IntVar()
C1=Checkbutton(framealt,text="bir hafta önce",variable=var1,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10")
C1.pack(anchor=NW,pady=5,padx=25)

var2=IntVar()
C2=Checkbutton(framealt,text="bir gün önce",variable=var2,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10")
C2.pack(anchor=NW,pady=5,padx=25)

var3=IntVar()
C3=Checkbutton(framealt,text="ayni gün",variable=var3,onvalue=1,offvalue=0,bg='#add8e6',font="verdana 10")
C3.pack(anchor=NW,pady=5,padx=25)


from  tkinter import messagebox
def gonder():
    son=""
    if var.get():
        if var.get()==1:
            son+="veriniz basarıyla sisteme kaydedildi"
            tip=hatirlatop.get() if hatirlatop.get()=='' else 'genel'
            tarih=hatirsec.get()
            mesaj=metin.get("1.0","end")
            with open("hatırlatmalar.txt","w") as dosya:
                dosya.write(
                    '{} kategorsisinde ,{} tarihinne ve "{}" notuyla hatırlatma'.format(tip,tarih,mesaj))
                dosya.close()


        elif var.get()==2:
            son+="e posta yoluyla hatırlatma size ulasacaktır"
        messagebox.showinfo("basarılı işlem",son)

    else:
        son+="gerekli alanların dolduruldugundan emin olun"
        messagebox.showwarning("yetersiz işlem",son)


    return


Label(framesag,text="Hatırlatma mesajı",bg='#add8e6',font="Verdana 10 bold").pack(padx=10,pady=10,anchor=NW)
metin=Text(framesag,height=9,width=50)
metin.tag_configure('style',foreground='#bfbfbf',font=('Verdana',7,'bold'))
metin.pack()
karsi="mesajını buraya gir..."
metin.insert(END,karsi,'style')

gonder=Button(framesag,text="Gönder",command=gonder)
gonder.pack(anchor=S)


master.mainloop()

