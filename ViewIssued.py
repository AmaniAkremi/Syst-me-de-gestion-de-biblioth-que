from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
#connexion au MySQL server
import pymysql
mypass = "Mans98634630@our"
mydatabase="bibliotheque"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
cur1=con.cursor()
# Nom de Tableaux
bookTable = "books_issued"
bookTable2="books"
def ViewIssued():
    root = Toplevel()
    root.title("Liste des livres Prétés")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Ajouter une image en arriére plan
    background_image = ImageTk.PhotoImage(file="ViewIssueed.jpg")
    label = Label(root, image=background_image, bd=0)
    label.pack()

    headingFrame1 = Frame(root, bg="#EB53B4", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Livres Prétés", bg='black', fg='white', font=('Courier', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-30s%-40s%s" % ('ID', 'Titre','Prété à',''),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            book_id = i[0]
            issued_to = i[1]

            # Requête pour récupérer le titre du livre
            getTitle = "SELECT title FROM " + bookTable2 + " WHERE book_id = %s"
            cur1.execute(getTitle, (book_id,))
            title = cur1.fetchone()[0]

            # Créer le label avec l'ID, le titre et le prêté à
            Label(labelFrame, text="%-10s%-30s%-40s" % (book_id, title, issued_to), bg='black', fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="Quiter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()



