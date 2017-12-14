from Tkinter import *

root = Tk()
root.title("Name Check")

a = StringVar()

#Creating the frame
frame1 = Frame(root, width=300, height =250)

#Inserting  a label
lbl_1 = Label(root, text="Please enter your name")
#Inserting a textbox
txt_1 = Entry(root, textvariable=a)



def fn_PrintText():
    print ("This is the default value")
    # Inserting third label
    lbl_3 = Label(root, text="Your name is:")
    print (txt_1.get())
    a.set(txt_1.get())
    # print a
    lbl_3.pack()
    lbl_2 = Label(root, textvariable= a)
    lbl_2.pack()


#Creating a button
btn_1 = Button(root, text="Click me!", command=fn_PrintText)

#Saving value from texbox into the label 2

#lbl_2 = Label(txt_1.get())



#packing everything into the frame
lbl_1.pack()
txt_1.pack()
btn_1.pack()




frame1.bind(btn_1)

frame1.pack()

root.mainloop()

