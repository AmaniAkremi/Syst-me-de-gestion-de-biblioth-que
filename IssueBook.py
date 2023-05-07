
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


mypass = "Mans98634630@our"
mydatabase="bibliotheque"

con = pymysql.connect(host="localhost",user="root", password=mypass,database=mydatabase)
cur = con.cursor()


# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

allBid = []  #To store all the Book ID’s


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select book_id from " + bookTable
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

            if check == 'disponible':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except Exception as e :
        messagebox.showinfo("Error", e)

    issueSql = "insert into " + issueTable + " values ('" + bid + "','" + issueto + "')"
    show = "select * from " + issueTable

    updateStatus = "update " + bookTable + " set satatus = 'prété' where book_id = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Livre préter avec succés")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Livre déjà prété!")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "La valeur saisie est erronée, essayer de nouveau!")

    print(bid)
    print(issueto)

    allBid.clear()


def IssueBook():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Toplevel()
    root.title("Préter Un Livre")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Ajouter une image en arriére plan
    background_image = ImageTk.PhotoImage(file="pret3.jpg")
    label = Label(root, image=background_image, bd=0)
    label.pack()

    headingFrame1 = Frame(root, bg="#2ECC71", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Livre Prété", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#2ECC71')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="ID du Livre : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelFrame, text="Prété à : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Valider", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quiter", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()