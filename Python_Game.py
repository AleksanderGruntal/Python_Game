from tkinter import *
from tkinter import messagebox as mb
import random

def vali_sõna(): #Valib juhusliku sõna
    with open("sõnad.txt", "r") as file:
        sõnad = file.readlines()
        return random.choice(sõnad).strip().lower()

def kontrolli_sõna(): #Kontrollib, kas sõna on õigesti kirjutatud
    arvatud_sõna = ""
    for entry in sissekanded:
        arvatud_sõna += entry.get().strip().lower()
    
    if len(arvatud_sõna) != 5:
        mb.showwarning("Viga", "Sõna peaks koosnema 5 tähest!")
        return
    
    if not arvatud_sõna.isalpha():
        mb.showwarning("Viga", "Sõna peaks koosnema ainult tähtedest!")
        return

    if arvatud_sõna in sõnade_nimekiri: #Vastab, kas sisestasite sõna õigesti
        mb.showinfo("Tulemus", f"Palju õnne! Arvasite õigesti sõna: {arvatud_sõna.capitalize()}!")
    else:
        mb.showinfo("Tulemus", f"Kahjuks sõna {arvatud_sõna.capitalize()} ei ole ära arvatud. Proovige uuesti!")
        püüde.set(püüde.get() - 1)  #Vähendab katsete arvu
        if püüde.get() == 0:
            mb.showinfo("Tulemus", f"Teil on otsas katsed. Õige sõna oli: {valitud_sõna.capitalize()}!")
            aken.quit()
    
    for i, täht in enumerate(valitud_sõna): #Värvid
        if i < 5:
            if arvatud_sõna[i] == täht:
                sissekanded[i].config(fg="green")
            elif arvatud_sõna[i] in valitud_sõna:
                sissekanded[i].config(fg="yellow")
            else:
                sissekanded[i].config(fg="black")

def lisa_sõna(): #Sõna lisamine tekstifaili
    uus_sõna = texbox6.get().strip().lower()
    if uus_sõna:
        with open("sõnad.txt", "a") as file1:
            file1.write(uus_sõna + "\n")
        mb.showinfo("Teade", f"Sõna '{uus_sõna.capitalize()}' on lisatud!")
    else:
        mb.showwarning("Viga", "Sõnaväli on tühi!")

        #Visuaalne osa
aken = Tk()
aken.geometry("400x300")
aken.title("Wordle")

sõnade_nimekiri = []
with open("sõnad.txt", "r") as file:
    for rida in file:
        sõnade_nimekiri.append(rida.strip().lower())
valitud_sõna = vali_sõna()

juhise_märgis=Label(aken,
               text="Sisestage 5-täheline sõna",
               bg="#d6daf1",
               fg="#2a5fac", #-
               cursor="star",
               font="Britannic_Bold 16",
               justify=CENTER,
               height=3,width=26)
juhise_märgis.pack()

sissekanded = []

for i in range(5):
    sissekanne = Entry(aken, font=("Helvetica", 12), width=3)
    sissekanne.pack(side=LEFT, padx=5)
    sissekanded.append(sissekanne)

kontrolli_nupp = Button(aken, text="Kontrollima",
                              bg="#7a8994",
                              fg="#faab09",
                              font="Britannic_Bold 16",
                              width=16,
                              command=kontrolli_sõna)
kontrolli_nupp.pack(pady=10)

pealkiri1 = Label(aken, text="Lisage uus sõna",
                         bg="#7a8994",
                         fg="#faf5f5",
                         font="Britannic_Bold 16",
                         justify=CENTER,
                          height=2, width=60)

pealkiri1.pack()

texbox6 = Entry(aken, bg="#ffcc00",
                      fg="#033e5c",
                      font="Britannic_Bold 16",
                      width=7,
                      show="")
texbox6.pack()

lisamise_nupp = Button(aken,
                       text="Lisa sõna",
                       bg="#7a8994",
                       fg="#faab09",
                       font="Britannic_Bold 16",
                       width=16, command=lisa_sõna)
lisamise_nupp.pack(pady=10)

püüde = IntVar()  
püüde.set(3) 

aken.mainloop()
