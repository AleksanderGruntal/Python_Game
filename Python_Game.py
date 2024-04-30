from tkinter import *
from tkinter import messagebox as mb
import random

def vali_suvaline_sõna():
    with open("sõnad.txt", "r") as file:
        sõnad = file.readlines()
        return random.choice(sõnad).strip().lower()

def kontrolli_sõna():
    arvatud_sõna = ""
    for entry in sissekanded:
        arvatud_sõna += entry.get().strip().lower()
    
    if len(arvatud_sõna) != 5:
        mb.showwarning("Viga", "Sõna peaks koosnema 5 tähest!")
        return
    
    if not arvatud_sõna.isalpha():
        mb.showwarning("Viga", "Sõna peaks koosnema ainult tähtedest!")
        return

    if arvatud_sõna in sõnade_nimekiri:
        mb.showinfo("Tulemus", f"Palju õnne! Arvasite õigesti sõna: {arvatud_sõna.capitalize()}!")
    else:
        mb.showinfo("Tulemus", f"Kahjuks sõna {arvatud_sõna.capitalize()} ei ole ära arvatud. Proovige uuesti!")
        püüde_arv.set(püüde_arv.get() - 1)  # Уменьшаем количество оставшихся попыток
        if püüde_arv.get() == 0:
            mb.showinfo("Tulemus", f"Teil on otsas katsed. Õige sõna oli: {valitud_sõna.capitalize()}!")
            root.quit()
    
    for i, täht in enumerate(valitud_sõna):
        if i < 5:
            if arvatud_sõna[i] == täht:
                sissekanded[i].config(fg="green")
            elif arvatud_sõna[i] in valitud_sõna:
                sissekanded[i].config(fg="yellow")
            else:
                sissekanded[i].config(fg="black")

def lisa_sõna():
    uus_sõna = texbox6.get().strip().lower()
    if uus_sõna:
        with open("sõnad.txt", "a") as file1:
            file1.write(uus_sõna + "\n")
        mb.showinfo("Teade", f"Sõna '{uus_sõna.capitalize()}' on lisatud!")
    else:
        mb.showwarning("Viga", "Sõnaväli on tühi!")

root = Tk()
root.geometry("400x300")
root.title("Wordle")

sõnade_nimekiri = []
with open("sõnad.txt", "r") as file:
    for rida in file:
        sõnade_nimekiri.append(rida.strip().lower())
valitud_sõna = vali_suvaline_sõna()

juhise_märgis = Label(root, text="Sisestage 5-täheline sõna:", font=("Helvetica", 12))
juhise_märgis.pack()

sissekanded = []

for i in range(5):
    sissekanne = Entry(root, font=("Helvetica", 12), width=3)
    sissekanne.pack(side=LEFT, padx=5)
    sissekanded.append(sissekanne)

kontrolli_nupp = Button(root, text="Kontrollima",
                        bg="#7a8994",
                       fg="#faab09",
                      font="Britannic_Bold 16",
                     width=16,
                    command=kontrolli_sõna)
kontrolli_nupp.pack(pady=10)

pealkiri1 = Label(root, text="Lisage uus sõna",
                  bg="#7a8994",
                 fg="#faf5f5",
                 font="Britannic_Bold 16",
                justify=CENTER,
               height=2, width=60)
pealkiri1.pack()

texbox6 = Entry(root, bg="#ffcc00",
                fg="#033e5c",
               font="Britannic_Bold 16",
              width=7,
             show="")
texbox6.pack()

lisamise_nupp = Button(root,
                       text="Lisa sõna",
                      bg="#7a8994",
                     fg="#faab09",
                    font="Britannic_Bold 16",
                   width=16, command=lisa_sõna)
lisamise_nupp.pack(pady=10)

püüde_arv = IntVar()  
püüde_arv.set(3) 

root.mainloop()
