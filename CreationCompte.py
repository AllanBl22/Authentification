import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql

def clear():
    mailEntry.delete(0,END)
    LoginEntry.delete(0,END)
    mdpEntry.delete(0,END)
    ConfirmermdpEntry.delete(0,END)
    check.set(0)

def ConnDatabase():
    if mailEntry.get()=="" or LoginEntry.get()=="" or mdpEntry.get()=="" or ConfirmermdpEntry()=="":
        messagebox.showerror("Erreur","Tout n'est pas rempli !")

    elif mdpEntry.get() != ConfirmermdpEntry.get():
        messagebox.showerror("Erreur","Votre mot de passe de correspond pas au premier ! ")
    elif check.get()==0:
        messagebox.showerror("Erreur","Accepter les Termes & les Conditions !")
    else:
        try:
            connect=pymysql.connect(host="localhost",username="root",password="1234")
            cursor=connect.cursor()
        except:
            messagebox.showerror("Erreur","Problème de connection avec la Database, réessayer !")
            return

        try:
            query="create database banga"
            cursor.execute(query)
            query="use banga"
            cursor.execute(query)
            query="create table Utilisateurs(id int auto_increment primary key not null, mail varchar(50),login varchar(100), mdp varchar(100)"
        except:
            cursor.execute("use banga")
        query= "select * from Utilisateurs where login=%s"
        cursor.execute(query,(LoginEntry.get()))
        row=cursor.fetchone()
        if row !=None:
            messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà !")
        else:

            query="insert Utilisateurs(mail,login,mdp) values (%s,%s,%s)"
            cursor.execute(query,(mailEntry.get(),LoginEntry.get(),mdpEntry.get()))
            connect.commit()
            connect.close()
            messagebox.showinfo("L'enregistrement est un succès !")
            clear()
            creaCompte_windows.destroy()
            import Auth

def connectionPage():
    creaCompte_windows.destroy()
    import Auth



creaCompte_windows=Tk()

creaCompte_windows.title("Création nouveau compte")

frame=Frame(creaCompte_windows, width=50,height=20,bg="red")
frame.place(x=554,y=100)

heading=Label(frame,text="CREER UN NOUVEAU COMPTE",font=("Microsoft Yahei UI Light",18,"bold") 
                ,bg="white", fg="firebrick")
heading.grid(row=0,column=0)

mailLabel=Label(frame,text="Mail",font=("Microsoft Yahei UI Light",10,"bold"),bg="white"
                ,fg="firebrick")
mailLabel.grid(row=1,column=0,sticky="w",padx=30,pady=(10,0))

mailEntry=Entry(frame,width=25,font=("Microsoft Yahei UI Light",10,"bold")
                ,fg="white",bg="firebrick")
mailEntry.grid(row=2,column=0,sticky="w",padx=30)


LoginLabel=Label(frame,text="Login",font=("Microsoft Yahei UI Light",10,"bold"),bg="white"
                ,fg="firebrick")
LoginLabel.grid(row=3,column=0,sticky="w",padx=30,pady=(10,0))

LoginEntry=Entry(frame,width=25,font=("Microsoft Yahei UI Light",10,"bold")
                ,fg="white",bg="firebrick")
LoginEntry.grid(row=4,column=0,sticky="w",padx=30)


mdpLabel=Label(frame,text="Mot de passe",font=("Microsoft Yahei UI Light",10,"bold"),bg="white"
                ,fg="firebrick")
mdpLabel.grid(row=5,column=0,sticky="w",padx=30,pady=(10,0))

mdpEntry=Entry(frame,width=25,font=("Microsoft Yahei UI Light",10,"bold")
                ,fg="white",bg="firebrick")
mdpEntry.grid(row=6,column=0,sticky="w",padx=30)


ConfirmermdpLabel=Label(frame,text="Confirmer votre mot de passe",font=("Microsoft Yahei UI Light",10,"bold"),bg="white"
                        ,fg="firebrick")
ConfirmermdpLabel.grid(row=7,column=0,sticky="w",padx=30,pady=(10,0))

ConfirmermdpEntry=Entry(frame,width=25,font=("Microsoft Yahei UI Light",10,"bold")
                        ,fg="white",bg="firebrick")
ConfirmermdpEntry.grid(row=8,column=0,sticky="w",padx=30)

check=IntVar()

Termesansconditions=Checkbutton(frame,text=" j'accepte les Termes & les Conditions",font=("Microsoft Yahei UI Light",10,"bold")
                                ,fg="firebrick",bg="white",activebackground="white",activeforeground="firebrick",cursor="main2",variable=check)
Termesansconditions.grid(row=9,column=0,pady=10,padx=15)

creaCompteButton=Button(frame,text="Création",font=("Open Sans",16,"bold")
                        ,bd=0,bg="firebrick",fg="white",activebackground="firebrick",activeforeground="white",width=17,command=ConnDatabase)
creaCompteButton.grid(row=10,column=0,pady=10)

dejaCompte=Label(frame,text="Pas de compte ?",font=("Open Sans",9,"bold")
                 ,bg="white", fg="firebreak")
dejaCompte.grid(row=11,column=0,sticky="w",padx=25,pady=10)

connecterButton=Button(frame,text="Se connecter",font=("Open Sans",9,"bold underline")
                 ,bg="white", fg="blue",bd=0,cursor="main2",activebackground="white",activeforeground="blue",command=connectionPage)
connecterButton.place(x=170,y=484)

creaCompte_windows.mainloop()