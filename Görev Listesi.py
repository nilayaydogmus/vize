from tkinter import *
from tkinter import messagebox


def yeniGorev():
    gorev = giris.get() #Kullanıcıdan giriş kutusunda sağlanan değeri çekmek.
   #Boşluk girişi olmaması için if-else koşulu kullanılır.
    if gorev != "":
        lb.insert(END,gorev)
        giris.delete(0,"end")
    else:
        messagebox.showwarning ("Uyarı","Lütfen Görev yazın")

#Seçilen görevin silinmesi.
def gorevSil():
    lb.delete(ANCHOR)

#Programın boyutu, ismi ve rengi belirlenir.
eleman = Tk()
eleman.geometry('500x450+500+200')
eleman.title('Görev Listesi')
eleman.config(bg='#FC9CBA')
eleman.resizable(width=False,height=False)

#Kaydırma çubuğu için frame.
frame = Frame(eleman)
frame.pack(pady=10)

#Liste kutusunun özellikleri.
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Arial',18),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#770428',
    activestyle="none",

)

lb.pack(side=LEFT,fill=BOTH)

#Veriler ve yeni veriler eklemek.
gorevListesi = [
    'Ders Çalış',
    'Spor Yap',
    'Yemek Hazırla',
    'Kitap Oku'
]

#Kaydırma çubuğu
for item in gorevListesi:
    lb.insert(END,item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#Kullanıcıdan değer almak.
giris = Entry(
    eleman,
    font=('Arial',24)
)

giris.pack(pady=20)

#Buton frameleri.
button_frame = Frame(eleman)
button_frame.pack(pady=20)

#Görev ekleme butonu
addGorev_btn = Button(
    button_frame,
    text='Görev Ekle',
    font=('Arial',14),
    bg='#8480B3',
    padx=20,
    pady=10,
    command= yeniGorev
)
addGorev_btn.pack(fill=BOTH,expand=True,side=LEFT)

#Görev silme butonu
delGorev_btn=Button(
    button_frame,
    text='Görev Sil',
    font=('Arial',14),
    bg='#8480B3',
    padx=20,
    pady=10,
    command= gorevSil
)
delGorev_btn.pack(fill=BOTH,expand=True,side= LEFT)


eleman.mainloop()