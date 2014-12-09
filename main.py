"""
==== GUI-Pylint ====
Doiinn : 57070103
Madooding : 57070112
====================
"""
from Tkinter import *
import ImageTk
import tkMessageBox as dialog
import tkFileDialog as file_dialog
from gpylint import *

def about_window():
	about = Toplevel()
	about.focus_set()
	about.grab_set()
	about.resizable(0,0)
	about.title("About This Application")
	appversion = Label(about, text="GUI-Pylint v0.1").pack()
	dev_a = Label(about, text="Sirirach Junta 57070112").pack()
	dev_b = Label(about, text="Worapong Malaiwong 57070103").pack()

def open_file():
	name = file_dialog.askopenfilename(filetypes=[("Python files", "*.py")])
	file_path.set(name)
	python_file = open(name, "r")

def gpylint_checker():
	obj = Gpylint()
	obj.analysis(file_path.get().replace('/', '\\'))
	print obj.read()

root = Tk()
root.resizable(0,0) #set to disable resize window
root.title("GUI-Pylint")    #title bar of app

frame = Frame(root, width=450, height=450) #frame(or windows) size
frame.pack()

#Variable
file_path = StringVar()
file_path.set("Select file...")

#Menu Bar
menubar = Menu(root) #create menu bar
file_menu = Menu(menubar, tearoff=0) #create "File" menu
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menubar, tearoff=0) #create "Help" menu
help_menu.add_command(label="View Guide")
help_menu.add_command(label="About", command=about_window)
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Application Title Logo
applogo = Canvas(frame, width=400, height=147)
applogo.pack()
applogo_img = ImageTk.PhotoImage(file="gpy-logo.png")
applogo.create_image(200, 75, image=applogo_img)

apptitle = Label(root, text="A Python code checker", font=(None, 12)) #title below app logo
apptitle.pack()

browse_file = Button(root, text="Browse", command=open_file)
browse_file.pack()

now_file = Label(root, textvariable=file_path)
now_file.pack()

upload_code = Button(root, text="Upload", command=gpylint_checker)
upload_code.pack()

root.mainloop()
