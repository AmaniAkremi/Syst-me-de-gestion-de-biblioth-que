from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


mypass = "Mans98634630@our"
mydatabase = "bibliotheque"

con = pymysql.connect (host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# les noms des tableaux :
issueTable = "books_issued"
bookTable = "books"
con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)

cur = con.cursor()


def delete():


    bid = bookInfo1.get()
    deleteSql = "delete from " + bookTable + " where book_id = " + bid
    deleteIssue = "delete from " + issueTable + " where book_id =  " + bid
    print(bid)

    try:


        cur.execute(deleteSql)
        if cur.rowcount==0 :
            raise Exception("not exisit")
        con.commit()

        cur.execute(deleteIssue)
        con.commit()


        messagebox.showinfo('Success', "Livre supprimer avec succé")

    except Exception as e:
        messagebox.showinfo("verefier votre id ")

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()


def DeleteBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root= Toplevel()
    root.title("Suprimer un livre")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    background_image = ImageTk.PhotoImage(file="del3.jpg")
    label = Label(root, image=background_image, bd=0)
    label.pack()


    headingFrame1 = Frame(root, bg="red", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Supprimer un livre", bg='#8B0000', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#8B0000')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame, text=" ID du livre : ", bg='#8B0000', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Valider", bg='#d1ccc0', fg='black', command=delete)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quiter", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()