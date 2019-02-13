'''
Filename: Assignment 4.
Author: Tejveer Singh
Course Name: Programming Language Research Project
Course Number: CST8333
Lab	Sec #: 351
Exercise Number: 3
Professors Name: Stanley Pieda.
'''
import dataBase
import threading
from tkinter import *
import tkinter.messagebox

d = dataBase.dataBaseClass
count = 1

try:
    #getting and array from database
    ar = d.selctRowFromMysql(count)[0]
except:
    print("Load Data First")
def buttonClick1():
    print("I am delete button")
    print(ar[0])
    d.deleteRowInDb(ar[0])

def updateClick1():
    global ar,count
    d.updateRowInDb(ar[0],entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get(),entry15.get(),entry16.get())
    ar = d.selctRowFromMysql(count)[0]
    insertionInEntryNull()
    insertionInEntry()
    print("Updated")


def searchIt():
    global ar, count
    value = int(entrySpecific.get())
    print(value)
    try:
        ar = dataBase.dataBaseClass.selctRowFromMysql(value)[0]
        count = value
        insertionInEntryNull()
        insertionInEntry()
    except:
        print("Enter an integer please")



def buttonClick2():
    print("I am button3 button")
def buttonClick3():
    # global ar
    # dataBase.dataBaseClass.createTableWithDataInDataBase()# class method
    # ar = dataBase.dataBaseClass.selctRowFromMysql(2)[0]
    # insertionInEntryNull()
    # insertionInEntry()
    entrySpecific.delete(0, 'end')
    entrySpecific.insert(0, "Please Wait Loading...")
    try:
        t = threading.Thread(target=rundb)
        t.start()
    except:
        print("thread not running")
    MessageBoxForInfo()


def rundb():
    global ar,count
    dataBase.dataBaseClass.createTableWithDataInDataBase()  # class method
    ar = dataBase.dataBaseClass.selctRowFromMysql(count)[0]
    insertionInEntryNull()
    insertionInEntry()

def blankIt():
    insertionInEntryNull()


def previous():
    print("I am previous button")
    global count, ar
    if count <= 1:
        count = 2
    count = count - 1
    try:
        ar = dataBase.dataBaseClass.selctRowFromMysql(count)[0]
    except:
        insertionInEntryNull()
        print("entry does not exists")
    entrySpecific.delete(0, 'end')
    entrySpecific.insert(0, count)
    insertionInEntryNull()
    insertionInEntry()


def Next():
    print("I am next button")
    global count, ar
    count = count + 1
    try:
        ar = dataBase.dataBaseClass.selctRowFromMysql(count)[0]
    except:
        insertionInEntryNull()
        print("entry does not exists")
    entrySpecific.delete(0,'end')
    entrySpecific.insert(0, count)
    insertionInEntryNull()
    insertionInEntry()

def InsertIt():
    d.insertTheNewData( entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(),
                    entry7.get(), entry8.get(), entry9.get(), entry10.get(), entry11.get(), entry12.get(),
                    entry13.get(), entry14.get(), entry15.get(), entry16.get())
    print("Inserted")

def MessageBoxForInfo():
    tkinter.messagebox.showinfo("Important Information", "Please Wait 30 sec so that data can load into database")


root = Tk()# main window
topFrame = Frame(root) #upper frame
topFrame.pack()
middleFrame = Frame(root)
middleFrame.pack()
middleFrame2 = Frame(root)
middleFrame2.pack()
bottomFrame = Frame(root)# lower Frame
bottomFrame.pack(side=BOTTOM)

#button Declaration
button1 =Button(bottomFrame ,text="Update", command=updateClick1)
button2 =Button(bottomFrame, text="Delete", command=buttonClick1)
button3 =Button(bottomFrame, text="Quit",command=quit)
button4 =Button(bottomFrame, text="Start Application",command=buttonClick3,bg="red")#on click will load data
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
#button for middle

buttonNext = Button(middleFrame, text="Next", command=Next)
entrySpecific = Entry(middleFrame)
buttonPrevios = Button(middleFrame, text="Previous", command=previous)
buttonNext.pack(side=RIGHT)
entrySpecific.pack(side=RIGHT)
buttonPrevios.pack(side=RIGHT)



#button for middle2

buttonInsert = Button(middleFrame2, text="Insert", command=InsertIt)
buttonInsert.pack(side=RIGHT)
buttonSearch = Button(middleFrame2, text="Search", command=searchIt)
buttonSearch.pack(side=RIGHT)
buttonBlankIt = Button(middleFrame2, text="BlankIt", command=blankIt)
buttonBlankIt.pack(side=RIGHT)


#label declaration
label1 = Label(topFrame, text="REF_DATE")
label1.grid(row = 0, column = 0)
label2 = Label(topFrame, text="GEO")
label2.grid(row=1, column=0)
label3 = Label(topFrame, text="DGUID")
label3.grid(row=2, column=0)
label4 = Label(topFrame, text="Food categories")
label4.grid(row=3, column=0)
label5 = Label(topFrame, text="Commodity")
label5.grid(row=4, column=0)
label6 = Label(topFrame, text="UOM")
label6.grid(row=5, column=0)
label7 = Label(topFrame, text="UOM_ID")
label7.grid(row=6, column=0)
label8 = Label(topFrame, text="SCALAR_FACTOR")
label8.grid(row=7, column=0)
label81 = Label(topFrame, text="SCALAR_ID")
label81.grid(row=8, column=0)
label9 = Label(topFrame, text="VECTOR")
label9.grid(row=9, column=0)
label10 = Label(topFrame, text="COORDINATE")
label10.grid(row=10, column=0)
label11= Label(topFrame, text="VALUE")
label11.grid(row=11, column=0)
label12 = Label(topFrame, text="STATUS")
label12.grid(row=12, column=0)
label13 = Label(topFrame, text="SYMBOL")
label13.grid(row=13, column=0)
label14= Label(topFrame, text="TERMINATED")
label14.grid(row=14, column=0)
label15= Label(topFrame, text="DECIMALS")
label15.grid(row=15, column=0)


#entry Declaration
entry1 = Entry(topFrame)
entry1.grid(row=0, column=1)
entry2 = Entry(topFrame)
entry2.grid(row=1, column=1)
entry3 = Entry(topFrame)
entry3.grid(row=2, column=1)
entry4 = Entry(topFrame)
entry4.grid(row=3, column=1)
entry5 = Entry(topFrame)
entry5.grid(row=4, column=1)
entry6 = Entry(topFrame)
entry6.grid(row=5, column=1)
entry7 = Entry(topFrame)
entry7.grid(row=6, column=1)
entry8 = Entry(topFrame)
entry8.grid(row=7, column=1)
entry9 = Entry(topFrame)
entry9.grid(row=8, column=1)
entry10 = Entry(topFrame)
entry10.grid(row=9, column=1)
entry11 = Entry(topFrame)
entry11.grid(row=10, column=1)
entry12 = Entry(topFrame)
entry12.grid(row=11, column=1)
entry13 = Entry(topFrame)
entry13.grid(row=12, column=1)
entry14 = Entry(topFrame)
entry14.grid(row=13, column=1)
entry15 = Entry(topFrame)
entry15.grid(row=14, column=1)
entry16 = Entry(topFrame)
entry16.grid(row=15, column=1)
def insertionInEntry():
    entry1.insert(0, ar[1])
    entry2.insert(0, ar[2])
    entry3.insert(0, ar[3])
    entry4.insert(0, ar[4])
    entry5.insert(0, ar[5])
    entry6.insert(0, ar[6])
    entry7.insert(0, ar[7])
    entry8.insert(0, ar[8])
    entry9.insert(0, ar[9])
    entry10.insert(0, ar[10])
    entry11.insert(0, ar[11])
    entry12.insert(0, ar[12])
    entry13.insert(0, ar[13])
    entry14.insert(0, ar[14])
    entry15.insert(0, ar[15])
    entry16.insert(0, ar[16])
def insertionInEntryNull():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    entry7.delete(0, 'end')
    entry8.delete(0, 'end')
    entry9.delete(0, 'end')
    entry10.delete(0, 'end')
    entry11.delete(0, 'end')
    entry12.delete(0, 'end')
    entry13.delete(0, 'end')
    entry14.delete(0, 'end')
    entry15.delete(0, 'end')
    entry16.delete(0, 'end')
entrySpecific.delete(0,'end')
entrySpecific.insert(0, count)
tkinter.messagebox.showinfo("Important Information", "If you are running the app for the first time make sure that the credential for database in data.py class are correct then start the application with start application button")
try:
    insertionInEntry()
except:
    print("Load data first")
root.mainloop()
