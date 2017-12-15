from Tkinter import *
from Tkinter import Frame, Entry, Tk
import time
import datetime as dt
import unicodedata as u
import sqlite3
from sqlite3 import Error







#Function START
#This is the function to create a new stock item
def fn_CreateItem():
    window3 =Toplevel()
    window3.title( "Create New Stock Item")

    print "Create NEw"

    #Throw in the widgets
    lblCreateItem = Label(window3, text="SICO Create A New Item")
    lblStockItemName = Label(window3, text="Stock Item Name :")
    lblTaxExclAmount = Label(window3, text="Tax Exclusive Amount :")
    lblCgstRate= Label(window3, text="CGST Rate% :")
    lblSgstRate= Label(window3, text="SGST Rate% :")
    lblSku= Label(window3, text="SKU (If Known) :")
    txtStockItemName = Entry(window3, textvariable=vStockItemName)
    txtTaxExclAmount= Entry(window3, textvariable=vTaxExclAmt)
    txtCgstRate = Entry(window3, textvariable=vCGST)
    txtSgstRate = Entry(window3, textvariable=vSGST)
    txtSku = Entry(window3, textvariable=vSKU)
    btnSubmitCreateItem = Button(window3, text = "Submit" ,border=1, command=fn_SubmitCreateItem)


    #Bind the widgets to the grid
    lblCreateItem.grid(row=0, column=1)
    lblStockItemName.grid(row=2, column =0)
    lblTaxExclAmount.grid(row=3, column=0)
    lblCgstRate.grid(row=4, column=0)
    lblSgstRate.grid(row=5, column=0)
    lblSku.grid(row=6, column=0)
    txtStockItemName.grid(row=2, column =1)
    txtTaxExclAmount.grid(row=3, column=1)
    txtCgstRate.grid(row=4, column =1)
    txtSgstRate.grid(row=5, column =1)
    txtSku.grid(row=6, column =1)
    btnSubmitCreateItem.grid(row=8, column = 1, rowspan=2, sticky=W)
#Function END


#Function START
#This is the function for submit button to insert values into tr_inventory
def fn_SubmitCreateItem():
        print 'You clicked the button!'
        #print a.get()
        #variable = a.get()
        #print variable
        col1=vStockItemName.get()
        col2=vTaxExclAmt.get()
        col3=vCGST.get()
        col4=vSGST.get()
        col5=vSKU.get()
        #Capture the values from the textboxes to variables
        #Connect to the database and insert the values into the inventory table
        connection = sqlite3.connect('sicotrichy_qa')
        cur=connection.cursor()
        #cur.execute("select *  from tr_inventory where  stock_item_name = 'Melamine Ashtray'")
        #ohho = cur.fetchall()
        #print ohho
        #cur.execute('insert into tr_inventory (stock_item_name, tax_exclusive_amount, cgst_rate, sgst_rate, stock_keeping_unit) VALUES (?,?,?,?,?)', ('hel22lo', 123, 4 , 4 , 'Dunno'))
        #inserting Dynamic values
        cur.execute(
            'insert into tr_inventory (stock_item_name, tax_exclusive_amount, cgst_rate, sgst_rate, stock_keeping_unit) VALUES (?,?,?,?,?)',
            (col1, col2, col3, col4, col5))
        connection.commit()

#Function END












# The main function starts here starts here

root = Tk()
root.title ( "SICO Trichy")



#Variables Declaration
#vTime1 is used in the function to compute dynamic time
vTime1 = ''

#vDate is used to display todays date
vDate=dt.datetime.today().strftime("%d-%b-%Y")
# The company logo image #The company logo image
vCompanyLogo=PhotoImage(file="G:\Programming\AbiePyCharmWork\SICO_Logo.gif")
#The company alphabets in Tamil
vaCompanyLetters = [ u'\u0b87' , u'\u0baa' ,u'\u0bcd'  ,u'\u0bb0' ,u'\u0bbe', u'\u0bb9' ,u'\u0bbf', u'\u0bae' ,u'\u0bcd' ]
#Concatenate the tamil letters into one word
vtCompanyName= u''.join(vaCompanyLetters)

#Variables from the window CREATE NEW ITEM
vStockItemName = StringVar()
vTaxExclAmt = StringVar()
vCGST = StringVar()
vSGST = StringVar()
vSKU = StringVar()

#CREATING/CONFIGURING THE WIDGETS
#Throw in  labels
lblDate_1 = Label(root, text="Date:")
lblDate_2 = Label(root,text=vDate)
#lblShopName = Label(root, text="S. Ibrahim & Co., \n Trichy" + alist)
lblShopName = Label(root, font=(None, 25), text="S. " + vtCompanyName + " & Co\n S. Ibrahim & Co., \n  23, Palakarai Maizham \n Trichy - 620008")
lblClock = Label(root)
lblCompanyLogo = Label(root, image=vCompanyLogo)
lblThankyou = Label(root,text="Thank you come again!")
lblShoestring1 = Label(root , text="shoestringapp@gmail.com")
lblShoestring1.config(fg="blue")



#throw in textboxes

#Throw in buttons
btnNewBill = Button(root, text="Create New Bill", border=1)
btnExistBill = Button(root, text = "View Existing Bill", border=1)
btnCreateItem = Button(root, text = "Create New Item",border=1 ,command= fn_CreateItem)
btnEditItem = Button(root,text="Edit Existing Item",border=1)
#END OF WIDGETS


#LAYOUT OF WIDGETS ON THE GRID

# In Row 0
lblDate_1.grid(row=0, column=7)
lblDate_2.grid(row=0, column=8)
lblShopName.grid(row=0, column=4, sticky =W, columnspan=3)
lblCompanyLogo.grid(row=0, column=2, sticky =N)
# In Row 1
lblClock.grid(row=1,column=8, sticky=N)
# In row 2 we have only blank space

# In row 3 we have some stuff
btnNewBill.grid(row=3 , column =2)
btnExistBill.grid(row=3, column=4)
btnCreateItem.grid(row=3, column =6)
btnEditItem.grid(row=3, column=8)

#In the last row
lblThankyou.grid(row=15, column= 4, columnspan = 3, sticky=S)
lblShoestring1.grid(row=16, column= 4, columnspan = 3, rowspan=5, sticky=N)
#END OF LAYOUT

# To fix the column and row sizes to default
col_count, row_count = root.grid_size()

for col in xrange(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in xrange(row_count):
    root.grid_rowconfigure(row, minsize=20)
# END of fixing the column and row sizez

#Setup the clock timer to display
def fn_tick():
    global vTime1
    # get the current local time from the PC
    vTime2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if vTime2 != vTime1:
        vTime1 = vTime2
        lblClock.config(text=vTime2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    lblClock.after(200, fn_tick)
    #END OF CLOCK TICKER


#Call the clock ticker on initialization
fn_tick()





root.mainloop()



