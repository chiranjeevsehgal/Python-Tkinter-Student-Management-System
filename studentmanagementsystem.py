from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def main():
    root = Tk()
    app = LoginPage(root)
    root.mainloop()

class LoginPage():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System : Login")
        # self.root.wm_iconbitmap("student.ico")
        self.root.geometry("1240x650")
        self.root.minsize(1240,650)
        self.root.configure(background="ivory2")
        self.headlbl = Label(self.root, text="Student Management System", bg="lightgrey", relief=GROOVE, bd=3, font="Arial 12 bold")
        self.headlbl.pack(side=TOP, fill=X)
        # VARIABLES-------------------------------------

        usernameinp =StringVar()
        passwordinp = StringVar()

        # ----------------------------------------------
        self.loginfrm = Frame(self.root, bd=3, relief=GROOVE, bg="lightgrey")
        self.loginfrm.place(x=400, y=150, height=300, width=500)

        self.loginhead = Label(self.loginfrm, text="Login", bg="lightgrey", font = "TimesNewRoman 15 bold",anchor=CENTER , bd=4, relief=GROOVE)
        self.loginhead.pack(fill=X,side=TOP)

        self.entryfrm = LabelFrame(self.loginfrm,text="Enter Details:", bd=3, relief=GROOVE, bg="lightgrey", height=20,width=550)
        self.entryfrm.pack(ipadx=140, ipady=100,padx=0,pady=0,side=TOP)
        
        self.usernamelbl = Label(self.entryfrm, text="Username:" , bg="lightgrey")
        self.usernamelbl.grid(row=0, column=0,padx=50,pady=28)
        self.usernameent = Entry(self.entryfrm, bd=4, relief=GROOVE,textvariable=usernameinp)
        self.usernameent.grid(row=0, column=1, ipadx=20)

        self.passwordlbl = Label(self.entryfrm, text="Password:" , bg="lightgrey")
        self.passwordlbl.grid(row=1, column=0,padx=50)
        self.passwordent = Entry(self.entryfrm, bd=4, relief=GROOVE,textvariable=passwordinp, show="*")
        self.passwordent.grid(row=1, column=1, ipadx=20)

        # FUNCTION-----------------------------

        def check_login():
            myusername = "admin"
            mypassword = "admin"
            if usernameinp.get() == myusername and passwordinp.get()== mypassword:
                self.newwindow = Toplevel(self.root)
                self.app = ManagementSystem(self.newwindow)
                usernameinp.set("")
                passwordinp.set("")
                
            else:
                messagebox.showerror("Error!", "Enter valid credentials.",parent=self.root)

        # -------------------------------------

        self.loginbtnfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.loginbtnfrm.grid(row=2, column=0,columnspan=5)

        self.loginbtn = Button(self.loginbtnfrm, text="Login", bd=4, bg="lightgrey",relief=GROOVE,width=15,command=check_login)
        self.loginbtn.grid(row=0, column=0, padx=180,pady=38,ipady=4)




class ManagementSystem():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1240x650")
        self.root.minsize(1240,650)
        self.root.title("Student Management System")
        # self.root.wm_iconbitmap("student.ico")
        self.root.configure(background="ivory2")
        self.maintitlelbl = Label(root, text="Student Management System", bg="lightgrey", relief=GROOVE, bd=3, font="Arial 12 bold")
        self.maintitlelbl.pack(side=TOP,fill=X)

        self.detailfrm = LabelFrame(root, text="Enter Details:",bg="lightgrey", bd=4,relief=GROOVE)
        self.detailfrm.place(x=30,y=50, width=300, height=551)

        # FUNCTIONS-----------------------------

        def fetch_data():
            ''' FUNCTION TO UPDATE THE DATABASE  '''
            dbconnect = pymysql.connect(host="localhost", user="root", password="", database = "smsdb")
            curs = dbconnect.cursor()
            curs.execute("SELECT * FROM studentdetails")
            rows=curs.fetchall()
            if len(rows) !=0:
                self.studentdatabase.delete(*self.studentdatabase.get_children())
                for row in rows:
                    self.studentdatabase.insert("",END,values=row)
                dbconnect.commit()
            dbconnect.close()

        def getdetails(event):

            ''' FUNCTION TO UPDATE THE ENTRY BOXES WITH DATABASE '''

            row = self.studentdatabase.focus()
            content = self.studentdatabase.item(row)
            cont = content['values']
            rollnuminp.set(cont[0])
            nameinp.set(cont[1])
            classinp.set(cont[2])
            sectioninp.set(cont[3])
            dobinp.set(cont[4])
            fathernameinp.set(cont[5])
            contactinp.set(cont[6])
            genderinp.set(cont[7])
            addressinp.set(cont[8])

        def addfunc():
            ''' FUNCTION TO ADD NEW FIELD TO THE DATABASE '''
            if rollnuminp.get() and nameinp.get() and classinp.get() and sectioninp.get() and dobinp.get() and fathernameinp.get() and contactinp.get() and genderinp.get() and addressinp.get():
                try:
                    mydb = pymysql.connect(host="localhost",user="root", password="", database=
                    "smsdb")
                    curs = mydb.cursor()
                    curs.execute("INSERT INTO studentdetails VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollnuminp.get(),nameinp.get(),classinp.get(), sectioninp.get(),dobinp.get(),fathernameinp.get(), contactinp.get(), genderinp.get(),addressinp.get()))
                    mydb.commit()
                    mydb.close()
                    fetch_data()
                    messagebox.showinfo("Success", "Data has been successfully added.",parent=self.root)
                except Exception as e:
                    messagebox.showerror("Error!", "Data could not be added.",parent=self.root)
            else:
                messagebox.showerror("Error!", "Please enter all the fields correctly.",parent=self.root)

        def clearfunc():
            ''' FUNCTION TO CLEAR THE ENTRY BOXES '''
            rollnuminp.set("")
            nameinp.set("")
            classinp.set("")
            sectioninp.set("")
            dobinp.set("")
            fathernameinp.set("")
            contactinp.set("")
            genderinp.set("")
            addressinp.set("")


        def updatefunc():
            ''' FUNCTION TO UPDATE THE DATABASE '''
            if rollnuminp.get() and nameinp.get() and classinp.get() and sectioninp.get() and dobinp.get() and fathernameinp.get() and contactinp.get() and genderinp.get() and addressinp.get():
                try:
                    mydb = pymysql.connect(host="localhost", user="root", password="", database="smsdb")
                    curs = mydb.cursor()
                    curs.execute("Update studentdetails set Name1=%s,Class1=%s,Section1=%s,DOB1=%s,FatherName1=%s,Contact1=%s,Gender1=%s,Address1=%s where RollNum1=%s",(nameinp.get(),classinp.get(),sectioninp.get(),dobinp.get(),fathernameinp.get(),contactinp.get(),genderinp.get(),addressinp.get(),rollnuminp.get()))
                    mydb.commit()
                    mydb.close()
                    fetch_data()
                    clearfunc()
                    messagebox.showinfo("Success", "Data has been successfully updated.",parent=self.root)
                except Exception as e:
                    messagebox.showerror("Error!", "Data could not be deleted, Please try again later.",parent=self.root)
            else:
                messagebox.showerror("Error!", "Please enter all the fields correctly.",parent=self.root)

        def deletefunc():
            ''' FUNCTION TO DELETE THE FIELD FROM DATABASE '''
            if rollnuminp.get() and nameinp.get() and classinp.get() and sectioninp.get() and dobinp.get() and fathernameinp.get() and contactinp.get() and genderinp.get() and addressinp.get():
                try:
                    mydb = pymysql.connect(host="localhost", user="root", password="", database="smsdb")
                    curs = mydb.cursor()
                    curs.execute("DELETE FROM studentdetails WHERE RollNum1 = %s",(rollnuminp.get()))
                    mydb.commit()
                    mydb.close()
                    fetch_data()
                    clearfunc()
                    messagebox.showinfo("Success!", "Data has been successfully deleted.",parent=self.root)
                except Exception as e:
                    messagebox.showerror("Error!", "Data could not be deleted, Please try again later.",parent=self.root)
            else:
                messagebox.showerror("Error!", "Please select the item to delete.",parent=self.root)

        def logoutfunc():
            # self.root.destroy()
            root.destroy()

        def exitfunc():
            self.root.quit()
            pass

        # --------------------------------------

        # VARIABLES-----------------------------

        rollnuminp = StringVar()
        nameinp = StringVar()
        classinp = StringVar()
        sectioninp = StringVar()
        dobinp = StringVar()
        fathernameinp = StringVar()
        contactinp = StringVar()
        genderinp = StringVar()
        addressinp = StringVar()
        filterinp = StringVar()
        searchinp = StringVar()

        # --------------------------------------

        # INPUT DETAILS-----------------------------

        self.rollnumlbl = Label(self.detailfrm, text="Roll No. - ", bg="lightgrey")
        self.rollnumlbl.grid(row=0,column=0, padx=15,pady=10)
        self.rollnument = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=rollnuminp)
        self.rollnument.grid(row=0,column=1,ipadx=8,ipady=2)

        self.namelbl = Label(self.detailfrm, text="Name - ", bg="lightgrey")
        self.namelbl.grid(row=1,column=0, padx=15,pady=10)
        self.nameent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=nameinp)
        self.nameent.grid(row=1,column=1,ipadx=8,ipady=2)

        self.classlbl = Label(self.detailfrm, text="Class - ", bg="lightgrey")
        self.classlbl.grid(row=2,column=0, padx=15,pady=10)
        self.classent = Entry(self.detailfrm, bd=3, relief=GROOVE,textvariable=classinp)
        self.classent.grid(row=2,column=1,ipadx=8,ipady=2)

        self.sectionlbl = Label(self.detailfrm, text="Section - ", bg="lightgrey")
        self.sectionlbl.grid(row=3,column=0, padx=15,pady=10)
        self.sectionent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=sectioninp)
        self.sectionent.grid(row=3,column=1,ipadx=8,ipady=2)

        self.doblbl = Label(self.detailfrm, text="D.O.B - ", bg="lightgrey")
        self.doblbl.grid(row=4,column=0, padx=15,pady=10)
        self.dobent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=dobinp)
        self.dobent.grid(row=4,column=1,ipadx=8,ipady=2)

        self.fathernamelbl = Label(self.detailfrm, text="Father's Name - ", bg="lightgrey")
        self.fathernamelbl.grid(row=5,column=0, padx=15,pady=10)
        self.fathernameent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=fathernameinp)
        self.fathernameent.grid(row=5,column=1,ipadx=8,ipady=2)

        self.contactlbl = Label(self.detailfrm, text="Contact - ", bg="lightgrey")
        self.contactlbl.grid(row=6,column=0, padx=15,pady=10)
        self.contactent = Entry(self.detailfrm, bd=3, relief=GROOVE,textvariable=contactinp)
        self.contactent.grid(row=6,column=1,ipadx=8,ipady=2)

        self.genderlbl = Label(self.detailfrm, text="Gender - ", bg="lightgrey")
        self.genderlbl.grid(row=7,column=0, padx=15,pady=10)
        self.genderent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=genderinp)
        self.genderent.grid(row=7,column=1,ipadx=8,ipady=2)

        self.addresslbl = Label(self.detailfrm, text="Address - ", bg="lightgrey")
        self.addresslbl.grid(row=8,column=0, padx=15,pady=10)
        self.addressent = Entry(self.detailfrm, bd=3, relief=GROOVE, textvariable=addressinp)
        self.addressent.grid(row=8,column=1,ipadx=8,ipady=2)

        # -------------------------------------------

        # DETAIL BUTTONS ----------------------------

        self.detailbtnfrm = Frame(self.detailfrm, bg="lightgrey", bd=3, relief=GROOVE, width=290, height=50)
        self.detailbtnfrm.grid(row=9, column=0,columnspan=8,pady=35,padx=24)

        self.detailaddbtn = Button(self.detailbtnfrm,text="Add", bg="lightgrey", bd=3, relief=GROOVE,width=15, command=addfunc)
        self.detailaddbtn.grid(row=0, column=0)

        self.detailupdatebtn = Button(self.detailbtnfrm,text="Update", bg="lightgrey", bd=3, relief=GROOVE,width=15,command=updatefunc)
        self.detailupdatebtn.grid(row=0, column=1)

        self.detaildeletebtn = Button(self.detailbtnfrm,text="Delete", bg="lightgrey", bd=3, relief=GROOVE,width=15,command=deletefunc)
        self.detaildeletebtn.grid(row=1, column=0)
        
        self.detailclearbtn = Button(self.detailbtnfrm,text="Clear", bg="lightgrey", bd=3, relief=GROOVE,width=15,command=clearfunc)
        self.detailclearbtn.grid(row=1, column=1)

        self.endfrm = Frame(self.detailfrm,bd=3, bg="lightgrey", relief=GROOVE)
        self.endfrm.place(x=25, y=480)

        self.logoutbtn = Button(self.endfrm,text="Log Out", bg="lightgrey", bd=3, relief=GROOVE,width=15,command=logoutfunc)
        self.logoutbtn.grid(row=0, column=0)

        self.exitbtn = Button(self.endfrm,text="Exit", bg="lightgrey", bd=3, relief=GROOVE,width=15,command=exitfunc)
        self.exitbtn.grid(row=0, column=1)

        # -------------------------------------------


        # SEARCH FUNCTIONS---------------------------

        def searchfilter():
            mydb = pymysql.connect(host="localhost", user="root", password="", database="smsdb")
            curs = mydb.cursor()

            if filterinp.get() == "Roll No.":
                curs.execute("SELECT * from studentdetails WHERE RollNum1 = %s",(searchinp.get()))
                content = curs.fetchall()
                if len(content) != 0:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    for row in content:
                        self.studentdatabase.insert("", END,values=row)
                else:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    messagebox.showerror("Error!", "No results found.",parent=self.root)
                mydb.commit()
                mydb.close()

            elif filterinp.get() == "Name":
                curs.execute("SELECT * from studentdetails WHERE Name1 =%s",(searchinp.get()))
                content = curs.fetchall()
                if len(content)!=0:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    for item in content:
                        self.studentdatabase.insert("",END, values=item)
                else:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    messagebox.showerror("Error!", "No results found.",parent=self.root)
                mydb.commit()
                mydb.close()

            elif filterinp.get() == "Class":
                curs.execute("SELECT * FROM studentdetails where Class1 = %s",(searchinp.get()))
                content = curs.fetchall()
                if len(content) != 0 :
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    for item in content:
                        self.studentdatabase.insert("", END, values=item)
                else:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    messagebox.showerror("Error!", "No results found.",parent=self.root)
                mydb.commit()
                mydb.close()

            elif filterinp.get() == "Contact":
                curs.execute("SELECT * FROM studentdetails where Contact1 = %s",(searchinp.get()))
                content = curs.fetchall()
                if len(content) != 0 :
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    for item in content:
                        self.studentdatabase.insert("", END, values=item)
                else:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    messagebox.showerror("Error!", "No results found.",parent=self.root)
                mydb.commit()
                mydb.close()

            elif filterinp.get() == "Gender":
                curs.execute("SELECT * FROM studentdetails where Gender1 = %s",(searchinp.get()))
                content = curs.fetchall()
                if len(content) != 0 :
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    for item in content:
                        self.studentdatabase.insert("", END, values=item)
                else:
                    self.studentdatabase.delete(*self.studentdatabase.get_children())
                    messagebox.showerror("Error!", "No results found.",parent=self.root)
                mydb.commit()
                mydb.close()
            
            elif filterinp.get()== "Select":
                messagebox.showerror("Error!", "Please choose the filter option.",parent=self.root)

        def showallfunc():
            fetch_data()
            self.filterbox.current(0)
            searchinp.set("")

        # ------------------------------------------

        # SEARCH ATTRIBUTES--------------------------
        self.datafrm = Frame(self.root,bg="lightgrey", bd=4,relief=GROOVE)              
        self.datafrm.place(x=390,y=55, width=850, height=545)

        self.searchfrm= Frame(self.datafrm, bg="lightgrey" , bd=5, relief=GROOVE)
        self.searchfrm.place(x=0, y=0,width=840, height=60)

        self.searchlbl = Label(self.searchfrm, text="Search:", bg="lightgrey", font="Arial 10 bold")
        self.searchlbl.grid(row=0, column=0, padx=25,pady=13)

        self.filterbox = ttk.Combobox(self.searchfrm, state="readonly", width=22, textvariable=filterinp)
        self.filterbox['values'] = ("Select","Roll No.","Name","Class","Contact","Gender")
        self.filterbox.grid(row=0, column=1, padx=25,ipady=4)
        self.filterbox.current(0)

        self.searchentry = Entry(self.searchfrm, bd=3, textvariable=searchinp)
        self.searchentry.grid(row=0, column=2,padx=25, ipady=4, ipadx=22)

        self.searchbtn = Button(self.searchfrm, text="Search", bd=4 ,bg="lightgrey", relief=GROOVE, width=15, command=searchfilter)
        self.searchbtn.grid(row=0, column=3)

        self.showallbtn = Button(self.searchfrm, text="Show All", bd=4 ,bg="lightgrey", relief=GROOVE, width=15, command=showallfunc)
        self.showallbtn.grid(row=0, column=4,padx=5)

        # ------------------------------------------

        # DATABASE-----------------------------
        self.databasefrm= Frame(self.datafrm, bg="lightgrey", bd=5, relief=GROOVE, width=840, height=375)
        self.databasefrm.place(x=0, y=60)


        self.xscrlbar = Scrollbar(self.databasefrm,orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm,orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)


        self.studentdatabase = ttk.Treeview(self.databasefrm,height=21, xscrollcommand=self.xscrlbar.set,yscrollcommand=self.yscrlbar.set)
        self.studentdatabase['columns'] = ('Roll No.','Name','Class','Section','D.O.B','Father Name','Contact','Gender','Address')

        self.studentdatabase.heading("Roll No.", text="Roll No.")
        self.studentdatabase.heading("Name", text="Name")
        self.studentdatabase.heading("Class", text="Class")
        self.studentdatabase.heading("Section", text="Section")
        self.studentdatabase.heading("D.O.B", text="D.O.B")
        self.studentdatabase.heading("Father Name", text="Father Name")
        self.studentdatabase.heading("Contact", text="Contact")
        self.studentdatabase.heading("Gender", text="Gender")
        self.studentdatabase.heading("Address", text="Address")

        self.studentdatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.studentdatabase.xview)
        self.yscrlbar.config(command=self.studentdatabase.yview)

        self.studentdatabase.column("Roll No.", width=70)
        self.studentdatabase.column("Name", width=120)
        self.studentdatabase.column("Class", width=80)
        self.studentdatabase.column("Section", width=80)
        self.studentdatabase.column("D.O.B", width=80)
        self.studentdatabase.column("Father Name", width=100)
        self.studentdatabase.column("Contact", width=80)
        self.studentdatabase.column("Gender", width=80)
        self.studentdatabase.column("Address", width=120)


        self.studentdatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()
        self.studentdatabase.bind("<ButtonRelease-1>",getdetails)




if __name__ == "__main__":
    main()