from tkinter import *

# creation fenetre
fenetre = Tk()

# def
def empana():
    fenetre.destroy()
    fenetre2 = Tk()
    fenetre2.title("JAIFAIM")
    fenetre2.geometry("700x400")
    fenetre2.minsize(100, 100)
    fenetre2.maxsize(1000, 1000)
    fenetre2.config(background='#0065fb')

    # créer frame
    frame = Frame(fenetre2, bg='#0065fb')

    # ajouter frame
    frame.pack()

    # bouton1
    bouton_C1 = Button(frame, text="Empanadas Boeuf", font=("Courrier", 25), bg='white', fg='black')
    bouton_C1.pack()

    # bouton1
    bouton_C2 = Button(frame, text="Empanadas Poulet", font=("Courrier", 25), bg='white', fg='black')
    bouton_C2.pack()

    # bouton1
    bouton_C2 = Button(frame, text="Empanadas Fromage", font=("Courrier", 25), bg='white', fg='black')
    bouton_C2.pack()


# personnalisation fenetres
fenetre.title("JAIFAIM")
fenetre.geometry("700x400")
fenetre.minsize(100, 100)
fenetre.maxsize(1000, 1000)
fenetre.config(background='#0065fb')

# créer frame
frame = Frame(fenetre, bg='#0065fb')

# text1
titre = Label(fenetre, text="Bienvenue sur JAIFAIM", font=("courrier", 30), bg='#0065fb', fg='white')
titre.pack()

# text2
sous_titre = Label(fenetre, text="Que voulez-vous mangez ?", font=("Courrier", 20), bg='#0065fb', fg='white')
sous_titre.pack()
# bouton
bouton_E = Button(frame, command = empana, text="Empanadas", font=("Courrier", 25), bg='white', fg='black')
bouton_E.pack()

# ajouter frame
frame.pack()

# afficher fenetre
fenetre.mainloop()
fenetre2.mainloop()