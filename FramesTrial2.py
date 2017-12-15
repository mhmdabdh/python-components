from Tkinter import *





def create_window():  #step1
    window = Toplevel()  #step2

    txtStockItemName = Entry(window, textvariable= a) #step3   (Textbox creation)
    txtStockItemName.grid(row=0, column=0)  #step4 (textbox on grid)



    c = Button(window, text="Submit" , command=ugh_try)   # (Submit button creation with function)
    c.grid(row=0, column=1) #(button on grid)
    d = Label(window)
    d.grid(row=1, column=1)



def ugh_try():
    #variable = StringVar()
    print "Line 1"

    print (a.get()) #This is the value inside the textbox
    print "Line 2"
    variable = a.get()  #Storing the value into a variable!
    print "Line 3"
    print variable  # Printing the variable!



root = Tk()

a = StringVar()


b = Button(root, text="Create new window", command=create_window)
b.grid(row=0, column=0)
root.mainloop()