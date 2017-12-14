from Tkinter import *
import sqlite3
from sqlite3 import Error

root = Tk()
root.title("DB Connection check")

yourname = StringVar()
stockitemname = StringVar()
taxexclusive = StringVar()

#Creating the frame
frame1 = Frame(root, width=300, height =250)

#Inserting  a label
lbl_1 = Label(root, text="Please enter your name\n")
#Inserting a textbox
txt_1 = Entry(root, textvariable=yourname)
lbl_4 = Label(root, text="\n\nInput product Name to know amount")
txt_2 = Entry(root, textvariable=stockitemname)



def fn_PrintText():
    #print ("This is the default value")
    # Inserting third label
    lbl_3 = Label(root, text="Your name is:")
    #print (txt_1.get())
    yourname.set(txt_1.get())
    lbl_3.pack()
    lbl_2 = Label(root, textvariable= yourname)
    lbl_2.pack()


#2
def fn_PrintDatabase():
    print ("This is the DB value")
    conn = sqlite3.connect('sicotrichy_qa')
    print "Opened database successfully"
    #cursor = conn.execute("select * from tr_inventory where  sno=1;")
    #for row in cursor:
     #print "ID = ", row[0]
     #print "ADDRESS = ", row[2]
     #print "SALARY = ", row[3], "\n"
     #print "Operation done successfully"
    print "check 1"
    print txt_2.get()
    stockitemname.set(txt_2.get())
    print stockitemname
    print "check 2"
    lbl_5 = Label(root, textvariable= stockitemname)
    print stockitemname
    print "check 3"
    lbl_5.pack()
    print "check 4"
    cursor = conn.execute("select tax_exclusive_amount from tr_inventory where stock_item_name = 'Melamine Ashtray';")
    print "check 5"
    for row in cursor:
     print "check 6"
     print row[0]
     print "check 7"
     taxexclusive=row[0]
     print "check 8"
     print taxexclusive
    conn.close()
    print taxexclusive
    name = StringVar()
    name.set(taxexclusive)
    lbl_7 = Label(root, text="The tax exclusive amount is: ")
    lbl_7.pack()
    lbl_6 = Label(root, textvariable=name)
    lbl_6.pack()



#Creating a button
btn_1 = Button(root, text="Click me!", command=fn_PrintText)

#2 Creating button to fetch from DB
btn_2 = Button(root, text="Fetch from DB", command=fn_PrintDatabase)


#packing everything into the frame
lbl_1.pack()
txt_1.pack()
btn_1.pack()
lbl_4.pack()
txt_2.pack()
btn_2.pack()




frame1.bind(btn_1)
frame1.bind(btn_2)

frame1.pack()

root.mainloop()

