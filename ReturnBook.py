from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "Mans98634630@our"
mydatabase="bibliotheque"

con = pymysql.connect(host="localhost",user="root", password=mypass,database=mydatabase)
cur = con.cursor()

# les noms de tableaux
issueTable = "books_issued"
bookTable = "books"

allBid = []  #récupération des id du livres


def returnn():

    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()

    extractBid = "select book_id from " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select satatus from " + bookTable + " where book_id = '" + bid + "'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'prété':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Vérifier l'ID du livre")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from " + issueTable + " where book_id = '" + bid + "'"

    print(bid in allBid)
    print(status)
    updateStatus = "update " + bookTable + " set satatus = 'disponible' where book_id = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Livre rendu avec succés")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "vérifiez l'ID du livre!")
            root.destroy()

    except:
        messagebox.showinfo("Search Error", "la valeure saisie est érronée, essayez encore! ")
    allBid.clear()
def ReturnBook() :
     global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

     root = Toplevel()
     root.title("Rendre un Livre")
     root.minsize(width=400, height=400)
     root.geometry("600x500")

    #Ajouter une image en arriére plan
     background_image = ImageTk.PhotoImage(file="Return.jpg")
     label = Label(root, image=background_image, bd=0)
     label.pack()

     headingFrame1 = Frame(root, bg="#17137C", bd=5)
     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

     headingLabel = Label(headingFrame1, text="Livre Rendu", bg='black', fg='white', font=('Courier', 15))
     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

     labelFrame = Frame(root, bg='#17137C')
     labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
     # Book ID to Delete
     lb1 = Label(labelFrame, text="ID du livre : ", bg='black', fg='white')
     lb1.place(relx=0.05, rely=0.5)

     bookInfo1 = Entry(labelFrame)
     bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

     # Submit Button
     SubmitBtn = Button(root, text="Valider", bg='#d1ccc0', fg='black', command=returnn)
     SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

     quitBtn = Button(root, text="Quiter", bg='#f7f1e3', fg='black', command=root.destroy)
     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

     root.mainloop()


