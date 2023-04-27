#working on it ------------------------
from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import subprocess
from dataBase import DataBase
import re 
import os

#__________________________Subprocess___________________________#

def button_suivant():
        v_generate_err=generate_err()
        v_regex_verification=regex_verification()
        if v_regex_verification and  v_generate_err  :
                db.insert_data_sign_up_phase1(field_nom.get(),prenom_field.get(),email_field.get(),téléphone_field.get(),date_de_naissan_field.get())
                window.destroy()      
                subprocess.run(["python",current_path+r"/signUp2.py"])
                print("travaille")
                

        
def go_to_luncher():
        subprocess.run(["python",current_path+r"/Luncher.py"])
        window.quit()      


















#________________________________varaibel a utiliser___________________________________#

current_path=os.getcwd()

x_nom_entry=300+100+100
y_nom_entry=150

x_nom_Label=400+100+100
y_nom_Label=100

x_non_icon=350+100+100
y_non_icon=90

x_nom_etoile=600+100+100
y_nom_etoile=100


icon_size=50

#__________________________________________some function ___________________________________________#


#----------------------------placehoder----------------------------#


############################"event argument is to detect if I ckliked on the field or not#############################""""""
def focus_In(event):
        if date_de_naissan_field.get()=="YYYY-MM-DD":
                date_de_naissan_field.delete(0,END)
                date_de_naissan_field.configure(foreground="black")

def focus_out(event):
        if date_de_naissan_field.get()=="":
                date_de_naissan_field.insert(0,"YYYY-MM-DD")
                date_de_naissan_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))


#--------place holder de l'email-----------------------------#
def focus_In_email(event):
        if email_field.get()=="school@service.com":
                email_field.delete(0,END)
                email_field.config(fg="black")

def focus_out_email(event):
        if email_field.get()=="":
                email_field.insert(0,"school@service.com")
                email_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))


#--------place holder de l'email----------------------------#

def focus_In_téléphone(event):
        if téléphone_field.get()=="06******** | 07********":
                téléphone_field.delete(0,END)
                téléphone_field.config(fg="black")

def focus_out_téléphone(event):
        if téléphone_field.get()=="":
                téléphone_field.insert(0,"06******** | 07********")
                téléphone_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))




#-----------------------create icon------------------------------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image





#---------creation of a function that generate us a  error if it was the case------------#
def generate_err():
        ok=True
        if field_nom.get()=="":
                Label(window,text="****svp entrer le nom",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40)
                ok=False
        else:
                Label(window,text="****svp entrer le nom",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40)

        if prenom_field.get()=="":
                Label(window,text="****svp entrer le prenom",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100)
                ok=False
        else:
                Label(window,text="****svp entrer le prenom",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100)

        if email_field.get() in ["","school@service.com"]:
                Label(window,text="****svp entrer l' email",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*2)
                ok=False
        else: 
                Label(window,text="****svp entrer l' email",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*2)

        if téléphone_field.get() in  ["","06******** | 07********"]:
                Label(window,text="****svp entrer votre numero",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+30+100*3+40)
                ok=False
        else:
                Label(window,text="****svp entrer votre numero",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+30+100*3+40)

        if date_de_naissan_field.get()=="" or date_de_naissan_field.get()=="YYYY-MM-DD":
                Label(window,text="****svp entrer la date de naissance",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*4+85)
                ok=False
        else:
                Label(window,text="****svp entrer la date de naissance",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*4+85)

        return ok

#------verifier le syntaxx par les expresions regulieres-----------#

def regex_verification():
        ok=True
        email=re.match(r"^\w+\.?\w*@\w+\.\w{2,}$",email_field.get())
        if  not bool(email) and email_field.get().strip()  not  in ('school@service.com',""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+40+100*2)
                print("email valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+40+100*2)
                

        téléphone=re.match(r"^0(6|7)\d{8}$",téléphone_field.get())
        if not bool(téléphone) and téléphone_field.get().strip() not in ("06******** | 07********",""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+30+100*3+40)
                print("téléphone valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+30+100*3+40)

        
        date=re.match(r"^[1-2]\d{3}-(0?[1-9]|1[0-2])-((0?[1-9])|[1-2]?\d|3[0-1])$",date_de_naissan_field.get())
        if not bool(date) and date_de_naissan_field.get().strip() not in ("YYYY-MM-DD",""):
                ok=False
                Label(window,text="****invalide syntxe",fg="red",bg="white",bd=1).place(x=x_nom_entry+90,y=y_nom_entry+40+100*4+85)
        else:
                Label(window,text="****invalide syntxe",fg="white",bg="white",bd=1).place(x=x_nom_entry+90,y=y_nom_entry+40+100*4+85)

        return ok




#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")

#--------------------creation de la conenection avec la base de donee------------------
db=DataBase()













#______________________________________________create the non widget______________________________________#



#-----enter the Entry name field------#
name_txt=StringVar()

field_nom=Entry(window, textvariable=name_txt, width=45,bd=0,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
field_nom.place(x=x_nom_entry,y=y_nom_entry)



#-----enter the name Label------#
nom=Label(window,text="Entrer votre nom  : ",fg="black",font=("Helvetica",15,"bold"),bg="white" ,highlightthickness=0)
nom.place(x=x_nom_Label,y=y_nom_Label)

necessary_point=Label (window, text="*", fg="red",font=("Arial",15),bg="white" ,highlightthickness=0)
necessary_point.place(x=x_nom_etoile,y=y_nom_etoile)


#--------------association of icon picture to the Entry-------------------#

personel_icon=create_icon("icons/person_icon.png",(45,45))
image_label=Label(window, image=personel_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_non_icon,y=y_non_icon)
image_label.config(highlightthickness=0)



#_______________________________________________________create a prenom widget __________________________________________________________#


                                                #----prenom Label-----#
prenom_Label=Label(window,text="Entrer votre prenom :",font=("Helvetica",15,"bold"),bg="white")
prenom_Label.place(x=x_nom_Label,y=y_nom_Label+100)



#--------creation de l'etoile---------#

prenom_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
prenom_etoile.place(x=x_nom_etoile+10,y=y_nom_etoile+100)


prenom_txt=StringVar()
prenom_field=Entry(window, textvariable=prenom_txt,bd=0,width=45,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
prenom_field.place(x=x_nom_entry,y=y_nom_entry+100)



#--------------creation de l'icon de prenom-------------------#

prenom_icon=create_icon("icons/person_icon.png",(45,45))

image_label=Label(window, image=prenom_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_non_icon,y=y_non_icon+100)
image_label.config(highlightthickness=0)








# ________________________________________creation du champ email___________________________________________________#

    
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> aa1d97fd446bd2364775e5720bdc23996e94d9f7
    
#--------------creation du label-------------------#
email_Label=Label(window, text="Entrer votre email :",font=("Halvetica",15,"bold"),bg="white")
email_Label.place(x=x_nom_Label,y=y_nom_Label+200)
<<<<<<< HEAD
=======
=======

def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon

def emploi():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT filiere from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    filier=result[0]
    cursorr.execute("SELECT link from emploidutemps where filier='"+filier+"';")
    print(filier)
    url =cursorr.fetchone() 
    link=url[0]
    print(link)
    webbrowser.open_new_tab(link)
def support():
    messagebox.showinfo(title="SUPPORT", message="CONTACTER UN DES ADMINS :\n\n\nAFKIR MOHAMED \t email\n\n\nAKKOUH LOKMANE \t lokmaneakkouh10@gmail.com\n\n\n BEN TOUHAMI MOHAMED RIDA \t email")

#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database ETUDIANT------------------------------------    
database = mysql.connector.connect(host="localhost",
      user="root",
      password="root", 
      database="projet")
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()
#------------------------connect to the database ADRESSE------------------------------------    
database = mysql.connector.connect(host="127.0.0.1",
      user="root",
      password="root", 
      database="projet")
#------------------------create cursor---------------------------------------------
cursorr1=database.cursor()

#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
school_icon_button.place(x=25,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
paper_button.place(x=24,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=emploi, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,command=support,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------
# hello=Label(text="HELLO\t"+get_user_second_name(),font=("Arial",30),fg="#258EF5",bg="white")
# hello.place(x=700,y=30)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=170,y=100)
#-------------------- personal picture import ----------------------------------------------------------
photo=imporicon(get_user_picture(),(200,200))
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------


firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
firstName_label.place(x=180,y=110)
firstName_label2=Label(body_frame,text=get_user_first_name(),bg="#B5EFFF",fg="white",font=("Arila",20))
firstName_label2.place(x=600,y=110)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
second_Name_label.place(x=180,y=200)
second_Name_label2=Label(body_frame,text=get_user_second_name(),bg="#B5EFFF",fg="white",font=("Arila",20))
second_Name_label2.place(x=600,y=200)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CNE_label.place(x=180,y=250)
CNE_label2=Label(body_frame,text=get_user_CNE(),bg="#B5EFFF",fg="white",font=("Arila",20))
CNE_label2.place(x=600,y=250)


CIN_label=Label(body_frame,text="CIN:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CIN_label.place(x=180,y=300)
CIN_label2=Label(body_frame,text=get_user_CIN(),bg="#B5EFFF",fg="white",font=("Arila",20))
CIN_label2.place(x=600,y=300)


filiere_label=Label(body_frame,text="FILIERE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
filiere_label.place(x=180,y=350)
filiere_label2=Label(body_frame,text=get_filiere(),bg="#B5EFFF",fg="white",font=("Arila",20))
filiere_label2.place(x=600,y=400)
>>>>>>> b688d539ab8474e17aadeddfcd1cb75bf8dfc633
>>>>>>> aa1d97fd446bd2364775e5720bdc23996e94d9f7



#--------------creation du entry of email------------#

email_txt=StringVar()
email_field=Entry(window,textvariable=email_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff",fg="black")
email_field.place(x=x_nom_entry,y=y_nom_entry+200)
email_field.insert(0,"school@service.com")
email_field.configure(fg="gray")
email_field.bind("<FocusIn>",focus_In_email)
email_field.bind("<FocusOut>",focus_out_email)


#------------creation de l'étoile--------------#
email_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
email_etoile.place(x=x_nom_etoile-15,y=y_nom_etoile+200)

#---------------craetion de l'icon ----------#
email_icon=create_icon("icons/email_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=email_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+206)








#_______________________________creation du numero de telephone______________________________________#


#--------------creation du label-------------------#
téléphone_Label=Label(window, text="Entrer votre téléphone  :",font=("Halvetica",15,"bold"),bg="white")
téléphone_Label.place(x=x_nom_Label,y=y_nom_Label+330)


#--------------creation du entry of téléphone------------#
téléphone_txt=StringVar()
téléphone_field=Entry(window,textvariable=téléphone_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
téléphone_field.place(x=x_nom_entry,y=y_nom_entry+330)
téléphone_field.insert(0,"06******** | 07********")
téléphone_field.configure(fg="gray")
téléphone_field.bind("<FocusIn>",focus_In_téléphone)
téléphone_field.bind("<FocusOut>",focus_out_téléphone)


#------------creation de l'étoile--------------#
téléphone_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
téléphone_etoile.place(x=x_nom_etoile+40,y=y_nom_etoile+330)

#---------------craetion de l'icon ----------#
téléphone_icon=create_icon("icons/phone_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=téléphone_icon,bd=0,bg="white",fg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+336)






#______________________________________________creation de date de naissance_________________________________________________________________#


#--------------creation du label-------------------#
date_de_naissan_Label=Label(window, text="Entrer la date de naissance  :",font=("Louis George Cafe Bold",15,"bold"),bg="white")
date_de_naissan_Label.place(x=x_nom_Label,y=y_nom_Label+430+50)



#--------------creation du entry of date_de_naissan------------#
date_de_naissan_txt=StringVar()
date_de_naissan_field=Entry(window,textvariable=date_de_naissan_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff",fg="black")
date_de_naissan_field.place(x=x_nom_entry,y=y_nom_entry+430+50)

date_de_naissan_field.insert(0,"YYYY-MM-DD")
date_de_naissan_field.configure(fg="gray")
date_de_naissan_field.bind("<FocusIn>",focus_In)
date_de_naissan_field.bind("<FocusOut>",focus_out)

#-------------------creation de l'étoile-----------------#
date_de_naissan_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
date_de_naissan_etoile.place(x=x_nom_etoile+80,y=y_nom_etoile+480)

#---------------craetion de l'icon ----------#
date_de_naissan_icon=create_icon("icons/date_de_naissance_icon.png",(icon_size-15,icon_size-15))
icon_label=Label(window,image=date_de_naissan_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+430+50)




#___________________________________________creation des button_________________________________________#


#----------creation du boutton suivant-----------#
button_suivant=Button(window, text="suivant",fg="white",bg="#258EF5",width=20,activebackground="#258EF5",activeforeground="blue",font=("Louis George Cafe Bold",10,"bold"),command=button_suivant)
button_suivant.place(x=1070,y=680)

#-----------creartion du button go back----------#
go_back_icon=create_icon("icons/go_back.jpg",(45,15))
go_back_button=Button(window, text="Précedent",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Louis George Cafe Bold",10,"bold"),activebackground="#15b4ea",activeforeground="blue",command=go_to_luncher)
go_back_button.place(x=300+100,y=680)
















#______________________________________________________creation d'un frame___________________________________________________#



frame_title =Frame(window,bg="white" )
frame_title.place(x=290,y=0,width=3500,height=80)

frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=290+100,height=7000)


school_image=create_icon("icons/school1.jpg",(300+100,780))
picture_label=Label(frame,image=school_image)
picture_label.place(x=0,y=0)

#--------creation du titre--------#


espace_etudiant=Label(frame_title,text="ESPACE      ETUDIANT", font=("LEMONMILK-Medium",50),bg="white",pady=0,)
espace_etudiant.place(x=150,y=5)
                                                                                                                                                                                        








window.mainloop()