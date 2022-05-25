#newid
# patient Project

from ast import Delete
from distutils.cmd import Command
from email.mime import image
from tkinter import *
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
from turtle import width
from xmlrpc.client import FastUnmarshaller
from PIL import Image, ImageTk
from cProfile import label

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect(r"D:\python\newid.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS newid (id PRIMARYKEY text, fname text, lname text, dob text, mob text, yob text, gender text, address text, phone text, email text, bgroup text, history text, doctor text, high text, weight text, push text)")
        self.dbConnection.commit()
    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, fname, lname, dob, mob, yob, gender, address, phone, email, bgroup, history, doctor,high,weight,push):
        self.dbCursor.execute("INSERT INTO newid VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, fname, lname, dob, mob, yob, gender, address, phone, email, bgroup, history, doctor,high,weight,push))
        self.dbConnection.commit()
        
    def Update(self, fname, lname, dob, mob, yob, gender,  address, phone, email, bgroup, history, doctor,high,weight,push, id):
        self.dbCursor.execute("UPDATE newid SET fname = ?, lname = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, bgroup = ?, history = ?, doctor = ?,high = ?, weight = ?, push = ? WHERE id = ?", (fname, lname, dob, mob, yob, gender,  address, phone, email, bgroup, history, doctor,high, weight, push,id))
        self.dbConnection.commit()
        
    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM newid WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
        
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM newid WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM newid")
        records = self.dbCursor.fetchall()
        return records

class Values:
    def Validate(self, id, fname, lname, phone, email, doctor,high,weight,push):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fname.isalpha()):
            return "fname"
        elif not (lname.isalpha()):
            return "lname"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0 and email.count("_") == 0 ):
            return "email"
        elif not (doctor.isalpha()):
            return "doctor"
        elif not (high.isdigit()):
            return "high"
        elif not (weight.isdigit()):
            return "weight"    
        elif not (push.isdigit()):
            return "push"
        else:
            return "SUCCESS"
        
class InsertWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Insert data")

        
        self.id = tkinter.StringVar()
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.high = tkinter.StringVar()
        self.weight = tkinter.StringVar()
        self.push = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.yearList = list(range(1900, 2023))
        self.bgroupList = ["A", "AB", "B", "O"]

        # Labels
        tkinter.Label(self.window, text = "Patient ID",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = "First Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Last Name",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "Date Of Birth",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "Month Of Birth",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Year Of Birth",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Gender",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "High (cm)",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Weight (kg)",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Blood pressure",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Home Address",  width = 25).grid(pady = 5, column = 1, row = 11)
        tkinter.Label(self.window, text = "Phone Number",  width = 25).grid(pady = 5, column = 1, row = 12)
        tkinter.Label(self.window, text = "Email",  width = 25).grid(pady = 5, column = 1, row = 13)
        tkinter.Label(self.window, text = "Blood Group",  width = 25).grid(pady = 5, column = 1, row = 14)
        tkinter.Label(self.window, text = "Patient History",  width = 25).grid(pady = 5, column = 1, row = 15)
        tkinter.Label(self.window, text = "Doctor",  width = 25).grid(pady = 5, column = 1, row = 16)

        
        # Entry widgets
        self.idEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.id)
        self.fnameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fname)
        self.lnameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lname)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.email)
        self.historyEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.history)
        self.doctorEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.doctor)
        self.highEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.high)
        self.weightEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.weight)
        self.pushEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.push)

        self.idEntry.grid(pady = 5, column = 3, row = 1)
        self.fnameEntry.grid(pady = 5, column = 3, row = 2)
        self.lnameEntry.grid(pady = 5, column = 3, row = 3)
        self.highEntry.grid(pady = 5, column = 3, row = 8)
        self.weightEntry.grid(pady = 5, column = 3, row = 9)
        self.pushEntry.grid(pady = 5, column = 3, row = 10)
        self.addressEntry.grid(pady = 5, column = 3, row = 11)
        self.phoneEntry.grid(pady = 5, column = 3, row = 12)
        self.emailEntry.grid(pady = 5, column = 3, row = 13)
        self.historyEntry.grid(pady = 5, column = 3, row = 15)
        self.doctorEntry.grid(pady = 5, column = 3, row = 16)

        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList, width = 20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, width = 20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList, width = 20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values = self.genderList, width = 20)
        self.bgroupBox = tkinter.ttk.Combobox(self.window, values = self.bgroupList, width = 20)

        self.dobBox.grid(pady = 5, column = 3, row = 4)
        self.mobBox.grid(pady = 5, column = 3, row = 5)
        self.yobBox.grid(pady = 5, column = 3, row = 6)
        self.genderBox.grid(pady = 5, column = 3, row = 7)
        self.bgroupBox.grid(pady = 5, column = 3, row = 14)

        # Button widgets
        tkinter.Button(self.window, width = 20, text = "INSERT", command = self.Insert).grid(pady = 15, padx = 5, column = 1, row = 17)
       
        tkinter.Button(self.window, width = 20, text = "CLOSE", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 17)
       
        self.window.mainloop()

    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(),self.fnameEntry.get(), self.lnameEntry.get() , self.phoneEntry.get(), self.emailEntry.get(), self.doctorEntry.get(),self.highEntry.get(), self.weightEntry.get(), self.pushEntry.get())
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.fnameEntry.get(), self.lnameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.highEntry.get(), self.weightEntry.get(), self.pushEntry.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.bgroupBox.get(), self.historyEntry.get(), self.doctorEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
        else:
            self.valueErrorMessage = "Invalid input in field " + self.test 
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    
    
class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")

        # Initializing all the variables
        self.id = id

        
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.high = tkinter.StringVar()
        self.weight = tkinter.StringVar()
        self.push = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Transgender", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.bgroupList = ["A", "AB", "B",  "O"]

        # Labels
        tkinter.Label(self.window, text = "Patient ID",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = id,  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "First Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Last Name",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "Date Of Birth",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "Month Of Birth",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Year Of Birth",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Gender",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "High (cm)",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Weight (kg)",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Blood pressure",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Home Address",  width = 25).grid(pady = 5, column = 1, row = 11)
        tkinter.Label(self.window, text = "Phone Number",  width = 25).grid(pady = 5, column = 1, row = 12)
        tkinter.Label(self.window, text = "Email",  width = 25).grid(pady = 5, column = 1, row = 13)
        tkinter.Label(self.window, text = "Blood Group",  width = 25).grid(pady = 5, column = 1, row = 14)
        tkinter.Label(self.window, text = "Patient History",  width = 25).grid(pady = 5, column = 1, row = 15)
        tkinter.Label(self.window, text = "Doctor",  width = 25).grid(pady = 5, column = 1, row = 16)

        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id)
        
        tkinter.Label(self.window, text = self.searchResults[0][1],  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = self.searchResults[0][2],  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = self.searchResults[0][3],  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = self.searchResults[0][4],  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = self.searchResults[0][5],  width = 25).grid(pady = 5, column = 2, row = 6)
        tkinter.Label(self.window, text = self.searchResults[0][6],  width = 25).grid(pady = 5, column = 2, row = 7)
        tkinter.Label(self.window, text = self.searchResults[0][7],  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text = self.searchResults[0][8],  width = 25).grid(pady = 5, column = 2, row = 9)
        tkinter.Label(self.window, text = self.searchResults[0][9],  width = 25).grid(pady = 5, column = 2, row = 10)
        tkinter.Label(self.window, text = self.searchResults[0][10],  width = 25).grid(pady = 5, column = 2, row = 11)
        tkinter.Label(self.window, text = self.searchResults[0][11],  width = 25).grid(pady = 5, column = 2, row = 12)
        tkinter.Label(self.window, text = self.searchResults[0][12],  width = 25).grid(pady = 5, column = 2, row = 13)
        tkinter.Label(self.window, text = self.searchResults[0][13],  width = 25).grid(pady = 5, column = 2, row = 14)
        tkinter.Label(self.window, text = self.searchResults[0][14],  width = 25).grid(pady = 5, column = 2, row = 15)
        tkinter.Label(self.window, text = self.searchResults[0][15],  width = 25).grid(pady = 5, column = 2, row = 16)

        
        # Entry widgets
        self.fnameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fname)
        self.lnameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lname)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.email)
        self.historyEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.history)
        self.doctorEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.doctor)
        self.highEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.high)
        self.weightEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.weight)
        self.pushEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.push)

        self.fnameEntry.grid(pady = 5, column = 3, row = 2)
        self.lnameEntry.grid(pady = 5, column = 3, row = 3)
        self.addressEntry.grid(pady = 5, column = 3, row = 11)
        self.phoneEntry.grid(pady = 5, column = 3, row = 12)
        self.emailEntry.grid(pady = 5, column = 3, row = 13)
        self.historyEntry.grid(pady = 5, column = 3, row = 15)
        self.doctorEntry.grid(pady = 5, column = 3, row = 16)
        self.highEntry.grid(pady = 5, column = 3, row = 8)
        self.weightEntry.grid(pady = 5, column = 3, row = 9)
        self.pushEntry.grid(pady = 5, column = 3, row = 10)

        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList, width = 20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, width = 20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList, width = 20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values = self.genderList, width = 20)
        self.bgroupBox = tkinter.ttk.Combobox(self.window, values = self.bgroupList, width = 20)

        self.dobBox.grid(pady = 5, column = 3, row = 4)
        self.mobBox.grid(pady = 5, column = 3, row = 5)
        self.yobBox.grid(pady = 5, column = 3, row = 6)
        self.genderBox.grid(pady = 5, column = 3, row = 7)
        self.bgroupBox.grid(pady = 5, column = 3, row = 14)

        # Button widgets
        tkinter.Button(self.window, width = 20, text = "UPDATE", command = self.Update).grid(pady = 15, padx = 5, column = 1, row = 17)
  
        tkinter.Button(self.window, width = 20, text = "CLOSE", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 17)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.fnameEntry.get(), self.lnameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.highEntry.get(), self.weightEntry.get(), self.pushEntry.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.bgroupBox.get(), self.historyEntry.get(), self.doctorEntry.get(), self.id)
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

   

class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text = "Database View Window",  width = 25).grid(pady = 5, column = 1, row = 1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady = 5, column = 1, row = 2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "fname", "lname", "dob", "mob", "yob", "gender", "high","weight","push","address","phone","email","bgroup","history","doctor")

        # Treeview column headings
        self.databaseView.heading("id", text = "ID")
        self.databaseView.heading("fname", text = "First Name")
        self.databaseView.heading("lname", text = "Last Name")
        self.databaseView.heading("dob", text = "Day Of Birth")
        self.databaseView.heading("mob", text = "Month Of Birth")
        self.databaseView.heading("yob", text = "Year Of Birth")
        self.databaseView.heading("gender", text = "Gender")
        self.databaseView.heading("address", text = "Home Address")
        self.databaseView.heading("phone", text = "Phone Number")
        self.databaseView.heading("email", text = "Email ")
        self.databaseView.heading("bgroup", text = "Blood Group")
        self.databaseView.heading("history", text = "History")
        self.databaseView.heading("doctor", text = "Doctor")
        self.databaseView.heading("high", text = "High")
        self.databaseView.heading("weight", text = "Weight")
        self.databaseView.heading("push", text = "Push")

        # Treeview columns
        self.databaseView.column("id", width = 40)
        self.databaseView.column("fname", width = 100)
        self.databaseView.column("lname", width = 100)
        self.databaseView.column("dob", width = 80)
        self.databaseView.column("mob", width = 90)
        self.databaseView.column("yob", width = 80)
        self.databaseView.column("gender", width = 60)
        self.databaseView.column("address", width = 100)
        self.databaseView.column("phone", width = 90)
        self.databaseView.column("email", width = 100)
        self.databaseView.column("bgroup", width = 100)
        self.databaseView.column("history", width = 80)
        self.databaseView.column("doctor", width = 100)
        self.databaseView.column("high", width = 50)
        self.databaseView.column("weight", width = 50)
        self.databaseView.column("push", width = 50)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()

class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fname = tkinter.StringVar()
        self.lname = tkinter.StringVar()
        self.heading = " Enter Patient ID to " + task

        # Labels
        tkinter.Label(window, text = self.heading, width = 50).grid(pady = 20, row = 1)
        tkinter.Label(window, text = "Patient ID", width = 10).grid(pady = 5, row = 2)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width = 5, textvariable = self.id)

        self.idEntry.grid(pady = 5, row = 3)

        # Button widgets
        if (task == "Search"):
            tkinter.Button(window, width = 20, text = task, command = self.Search).grid(pady = 15, padx = 5, column = 1, row = 14)
        elif (task == "Delete"):
            tkinter.Button(window, width = 20, text = task, command = self.Delete).grid(pady = 15, padx = 5, column = 1, row = 14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)
    
    def Delete(self):
        self.database = Database()
        sure = tkinter.messagebox.askokcancel(title="Confirm",message="Do you want to delete ?")
        if sure == True :
            self.database.Delete(self.idEntry.get())
        else :
            return()


class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Patient Information System")
        self.homePageWindow.geometry("720x460")

        
        
        tkinter.Label(self.homePageWindow, text = "HOME",height=2,  width = 100).grid(pady = 20, column = 1, row = 1)

        tkinter.Button(self.homePageWindow, width = 20, text = "INSERT", command = self.Insert).grid(pady = 15, column = 1, row = 2)
        tkinter.Button(self.homePageWindow, width = 20, text = "UPDATE", command = self.Update).grid(pady = 15, column = 1, row = 3)
        tkinter.Button(self.homePageWindow, width = 20, text = "SEARCH", command = self.Search).grid(pady = 15, column = 1, row = 4)
        tkinter.Button(self.homePageWindow, width = 20, text = "DELETE", command = self.Delete).grid(pady = 15, column = 1, row = 5)
        tkinter.Button(self.homePageWindow, width = 20, text = "DISPLAY", command = self.Display).grid(pady = 15, column = 1, row = 6)
        tkinter.Button(self.homePageWindow, width = 20, text = "EXIT", command = self.homePageWindow.destroy).place(x=520,y=400)
        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()
    
    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text = "Enter the ID to update", width = 50).grid(pady = 20, row = 1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width = 5, textvariable = self.id)
        
        self.idEntry.grid(pady = 10, row = 2)
        
        # Button widgets
        tkinter.Button(self.updateIDWindow, width = 20, text = "Update", command = self.updateID).grid(pady = 10, row = 3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")
        

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)

hompage = HomePage   

root = Tk()
root.title("Login")
root.geometry("594x420")
root.resizable(0,0)
global entry1
global entry2
def login() :
    data = sqlite3.connect(r"D:\python\newid.db")
    c = data.cursor() 
    cursor= data.execute('SELECT * FROM login')
    for i in cursor:
        if user.get()==i[0]and password.get()==i[1]: 
           root.destroy()
           HomePage()
    tkinter.messagebox.showerror("error"," incorrect password ")        
           

#################################################################
photo2=PhotoImage(file="C:\\Users\\arlic\\Downloads\\Login.png")
Label(root,image=photo2 ).place(x=0,y=0)
#################################################################

user = StringVar()
password = StringVar()

entry1 = Entry(root,bd=0,width=30,textvariable=user)
entry1.place(x=260,y=180)

entry2 = Entry(root,bd=0,width=30,textvariable=password)
entry2.place(x=260,y=246)
Button(root,text="",command=login,height=2,width=2,bd=0,bg="#004AAD").place(x=235,y=333)

root.mainloop()
