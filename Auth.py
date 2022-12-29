import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql




def oublieMDP():
    def changeMDP():
        if login_entry.get()=="" or Nouveaumdp_entry.get()=="":
            messagebox.showerror("Erreur","Tous les champs ne sont pas remplis !",parent=windows_reset)
        elif Nouveaumdp_entry.get()!=Confirmermdp_entry.get():
            messagebox.showerror("Erreur","Mot de passe et le mot de passe confirmer sont différents !",parent=windows_reset)
        else:
            connect=pymysql.connect(host="localhost",username="root",password="1234",database="banga")
            cursor=connect.cursor()
            query="select * from Utilisateurs where login=%s"
            cursor.execute(query,(LoginEntry.get()))
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Erreur","Le nom d'utilisateur est incorrecte",parent=windows_reset)
            else:
                query="update Utilisateurs set mdp=%s where login=%s"
                cursor.execute(query,(Nouveaumdp_entry.get(),login_entry.get()))
                connect.commit()
                connect.close()
                messagebox.showinfo("Le mot de passe à été changé !",parent=windows_reset)
                windows_reset.destroy()

    windows_reset=Toplevel()
    windows_reset.title("Chanegement de mot de passe")

    headinglabel=Label(windows_reset, text="Chnager mot de passe", font=("arial",18,"bold")
                        ,bg="white",fg="magenta")
    headinglabel.place(x=480,y=60)

    login_label=Label(windows_reset, text="Login",font=("arial",12,"bold")
                        ,bg="white",fg="archid")
    login_label.place(x=470,y=130)

    login_entry=Entry(windows_reset, width=25,fg="magenta",font=("arial",11,"bold")
                        ,bd=0)
    login_entry.place(x=470,y=160)

    frame2=Frame(windows_reset, width=250, height=2, bg="archid")
    frame2.place(x=470,y=210)

    mdp_label=Label(windows_reset, text="mot de passe",font=("arial",12,"bold")
                        ,bg="white",fg="archid")
    mdp_label.place(x=470,y=130)

    Nouveaumdp_entry=Entry(windows_reset, text="Nouveau mot de passe",font=("arial",12,"bold")
                        ,bd=0)
    Nouveaumdp_entry.place(x=470,y=240)

    frame3=Frame(windows_reset, width=250, height=2,bg="archid")
    frame3.place(x=470,y=260)

    Confirmermdp_label=Label(windows_reset, text="Confirmer votre mot de passe",font=("arial",12,"bold")
                        ,bd=0)
    Confirmermdp_label.place(x=470,y=290)

    Confirmermdp_entry=Entry(windows_reset,width=25,fg="magenta",font=("arial",12,"bold")
                        ,bd=0)
    Confirmermdp_entry.place(x=470,y=290)

    frame4=Frame(windows_reset, width=250, height=2,bg="archid")
    frame4.place(x=470,y=340)

    validerButton=Button(windows_reset, texte="Valider", bd=0,bg="magenta",fg="white",font=("Open Sans",16,"bold")
                        ,width=19,cursor="main2",activebackground="magenta",activeforeground="white",command=changeMDP)
    validerButton.place(x=470,y=390)

    windows_reset.mainloop()


def connectUtilisateur():
    if LoginEntry.get()=="" or mdp_enter.get()=="":
        messagebox.showerror("Erreur","Remplisser les champs !")
    else:
        try:
            connect=pymysql.connect(host="localhost",username="root",password="1234")
            cursor=connect.cursor()
        except:
            messagebox.showerror("Erreur","La connexion n'a pas été établie !")
            return
        query="use banga"
        cursor.execute(query)
        query="select * from Utilisateurs where login=%s and mdp=%s"
        cursor.execute(query,(LoginEntry.get(),mdpEntry.get()))
        row=cursor.fetchone()
        if row==None:
            messagebox.showerror("Erreur","Vérifier votre login/mot de passe")
        else:
            messagebox.showinfo("Connexion réussi !")


def creationPage():
    login_windows.destroy()
    import CreationCompte

def cache():
    openeye.config(file="closeeye.png")
    mdpEntry.config(show="*")
    oeilButton.config(command=show)

def show():
    openeye.config(file="openeye.png")
    mdpEntry.config(show="")
    oeilButton.config(command=cache)

def utilisateur_enter(event):
    if LoginEntry.get()=="Login":
        LoginEntry.delete(0,END)

def mdp_enter(event):
    if mdpEntry.get()=="Mot de passe":
        mdpEntry.delete(0,END)


login_windows=Tk()
login_windows.geometry("998x668+50+50")
login_windows.resizable(0,0)
login_windows.title("Authentification")

heading=Label (login_windows,text="USER LOGIN",font=("Microsoft Yahei UI Light",23,"bold") 
                ,bg="white", fg="firebrick")
heading.place(x=605, y=120)

LoginEntry=Entry(login_windows,width=25,font=("Microsoft Yahei UI Light",11,"bold") 
                ,bd=0, fg="firebrick")
LoginEntry.place(x=580,y=200)
LoginEntry.insert(0,"Login")

LoginEntry.bind("<FocusIn>",utilisateur_enter)


frame1=Frame(login_windows,width=250,height=2,bg="firebrick")
frame1.place(x=580,y=222)


mdpEntry=Entry(login_windows,width=25,font=("Microsoft Yahei UI Light",11,"bold") 
                ,bd=0, fg="firebrick")
mdpEntry.place(x=580,y=260)
mdpEntry.insert(0,"Mot de passe")

mdpEntry.bind("<FocusIn>",mdp_enter)

frame2=Frame(login_windows,width=250,height=2,bg="firebrick")
frame2.place(x=580,y=222)

openeye=PhotoImage(file='openeye.png')
oeilButton=Button(login_windows,image=openeye, bd=0,bg="white",activebackground="white"
                   ,cursor="main2", command=cache)
oeilButton.place(x=800,y=255)


oublieButton=Button(login_windows,text='Mot de passe oublié ?', bd=0,bg="white",activebackground="white"
                   ,cursor="main",font=("Microsoft Yahei UI Light",11,"bold"),fg="firebrick",activeforeground="firebrick",command=oublieMDP)
oublieButton.place(x=715,y=295)

connecterButton=Button(login_windows,text="Se connecter", font=("Open Sans",16,"bold")
                        ,fg="white",bg="firebrick",activeforeground="white", activebackground="white",cursor="main2",bd=0,width=19,command=connectUtilisateur)
connecterButton.place(x=578,y=358)


ouLabel=Label(login_windows,text="-------- OU --------",font=("Open Sans",16),fg="firebrick",bg="white")
ouLabel.place(x=583,y=400)


EnregistrementLabel=Label(login_windows,text="Pas de compte ?",font=("Open Sans",9,"bold"),fg="firebrick",bg="white")
EnregistrementLabel.place(x=590,y=500)

nouveauCompteButton=Button(login_windows,text="Créer un nouveau compte", font=("Open Sans",9,"bold underline")
                        ,fg="white",bg="white",activeforeground="blue", activebackground="white",cursor="main2",bd=0,command=creationPage)
nouveauCompteButton.place(x=727,y=500)

login_windows.mainloop()