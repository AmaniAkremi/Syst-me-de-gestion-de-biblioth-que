from tkinter import *
from PIL import Image as im
from PIL import ImageTk
from tkinter import messagebox
import pymysql

bookTable = "books"
def RegisterBook():

    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into " + bookTable + " values ('" + bid + "','" + title + "','" + author + "','" + status + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Livre ajouté avec succé")
    except:
        messagebox.showinfo("Error", "Impossible d'ajouter un livre à la base de donnée")

    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()

def AddBook ():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Toplevel()
    root.title("Ajout d'un livre")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "Mans98634630@our"
    mydatabase = "bibliotheque"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    # Ajouter une image en arriére plan
    background_image = ImageTk.PhotoImage(file="add2.jpg")
    label = Label(root, image=background_image, bd=0)
    label.pack()

    headingFrame1 = Frame(root, bg="pink", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ajout d'un livre", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='pink')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="ID du livre : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Titre
    lb2 = Label(labelFrame, text="Titre : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Auteur
    lb3 = Label(labelFrame, text="Auteur : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Status
    lb4 = Label(labelFrame, text="Statu(Dispo/Prété) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # bouton Valider/Quitter
    SubmitBtn = Button(root, text="Valider", bg='#d1ccc0', fg='black', command=RegisterBook)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quiter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()




