"""
==== GUI-Pylint ====
Doiinn : 57070103
Madooding : 57070112
====================
"""
from Tkinter import *
import ImageTk

root = Tk()
root.resizable(0,0) #set to disable resize window
root.title("GUI-Pylint")    #title bar of app

frame = Frame(root, width=450, height=450) #frame(or windows) size
frame.pack()

applogo = Canvas(frame, width=400, height=147)
applogo.pack()

applogo_img = ImageTk.PhotoImage(file="gpy-logo.png")
applogo.create_image(200, 75, image=applogo_img)

root.mainloop()
