from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#connexion au MySQL server
import pymysql
mypass = "Mans98634630@our"
mydatabase="bibliotheque"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"
def ViewBooks():
    root = Toplevel()
    root.title("Liste des livres")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Ajouter une image en arriére plan
    background_image = ImageTk.PhotoImage(file="view3.jpg")
    label = Label(root, image=background_image, bd=0)
    label.pack()

    headingFrame1 = Frame(root, bg="#7B68EE", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Liste des livres", bg='black', fg='white', font=('Courier', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('ID', 'Titre', 'Auteur', 'Statu'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quiter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


