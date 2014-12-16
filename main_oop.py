











        """Initialize variable for this class"""
        """test"""
        # Application Title Logo
        #Browse Button
        #File Path Text
        #Main Windows
        #Menu Bar
        #Text Variable
        #Upload Button
        mainapp.config(menu=self.menubar)
        mainapp.resizable(0,0)
        mainapp.title("GUI-Pylint")
        self.about = tk.Toplevel()
        self.about.focus_set()
        self.about.geometry("300x200+300+300")
        self.about.grab_set()
        self.about.resizable(0,0)
        self.about.title("About This Application")
        self.applogo = tk.Canvas(self.frame, width=400, height=147)
        self.applogo.create_image(200, 75, image=self.applogo_img)
        self.applogo.pack()
        self.applogo_img = ImageTk.PhotoImage(file="gpy-logo.png")
        self.apptitle = tk.Label(mainapp, text="A Python code checker", font=(None, 12)) #title below app logo
        self.apptitle.pack()
        self.appversion = tk.Label(self.about, text="GUI-Pylint v0.1").pack()
        self.browse = tk.Button(mainapp, text="Browse")
        self.browse.pack()
        self.dev_a = tk.Label(self.about, text="Sirirach Junta 57070112").pack()
        self.dev_b = tk.Label(self.about, text="Worapong Malaiwong 57070103").pack()
        self.file_path = tk.StringVar()
        self.file_path.set("Select file...")
        self.frame = tk.Frame(mainapp)
        self.frame.pack()
        self.help_menu = tk.Menu(self.menubar, tearoff=0) #create "Help" menu
        self.help_menu.add_command(label="About", command=self.about_window)
        self.help_menu.add_command(label="View Guide")
        self.mainapp = mainapp
        self.menubar = tk.Menu(mainapp) #create menu bar
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.path_text = tk.Label(mainapp, textvariable=self.file_path)
        self.path_text.pack()
        self.result_header = tk.StringVar()
        self.result_header.set("========================================GUI-Pylint========================================")
        self.upload = tk.Button(mainapp, text="Upload")
        self.upload.pack()
    """Graphics User Interface for gpylint in GUI-Pylint"""
    """test"""
    app = Aplication(root)
    def __init__(self, mainapp):
    def about_window(self):
    root = tk.Tk()
    root.geometry("400x400+300+300")
    root.mainloop()
"""
"""
==== GUI-Pylint ====
====================
class Aplication:
def main():
Doiinn : 57070103
from gpylint import *
import ImageTk
import tkFileDialog as file_dialog
import Tkinter as tk
import tkMessageBox as dialog
Madooding : 57070112
main()