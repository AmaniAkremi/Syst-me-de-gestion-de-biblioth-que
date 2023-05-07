

from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from ViewIssued import *
import mysql.connector

#conexion base de donnée

mypass = "Mans98634630@our"
mydatabase="bibliotheque"
conn = mysql.connector.connect(host = "localhost",
                  user = 'root',
                  password = mypass,
                  database = mydatabase,
                  auth_plugin='mysql_native_password'
                               )
cur = conn.cursor()

#créer la fenetre principale
from tkinter import *
root=Tk()
root.title("Bibliothéque")
root.minsize(width=400,height=400)
root.geometry("600x500")

#Ajouter une image en arriére plan
background_image = ImageTk.PhotoImage(file="books.jpg")
label = Label(root, image=background_image)
label.pack()
#Mise en place de l'entéte
headingFrame1 = Frame(root,bg="#A52A2A", bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Bienvenue à \n notre bibliotéque", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#Ajouter les bouttons
btn1 = Button(root, text="Ajouter un livre", bg='Orange', fg='black', command=AddBook)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Effacer un livre", bg='Orange', fg='black', command=DeleteBook)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="Voir liste des livres", bg='Orange', fg='black', command=ViewBooks)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Préter un livre", bg='Orange', fg='black', command=IssueBook)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Rendre un livre", bg='Orange', fg='black', command=ReturnBook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text=" Voir liste des livres prétés", bg='Orange', fg='black', command=ViewIssued)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()











