"""
==== GUI-Pylint ====
Doiinn : 57070103
Madooding : 57070112
====================
"""
import Tkinter as tk
import tkMessageBox as dialog
import tkFileDialog as file_dialog
from gpylint import *
class Aplication:
    """Graphics User Interface for gpylint in GUI-Pylint"""
    def __init__(self, mainapp):
        """Initialize variable for this class"""
        self.mainapp = mainapp
        mainapp.resizable(0,0)
        mainapp.config(bg='white')
        mainapp.title("GUI-Pylint")

        self.bgapp = 'white'
        self.appfont = 'Segoe UI'

        #Variable
        self.file_path = tk.StringVar()
        self.file_path.set("No File Selected...")
        self.result_header = tk.StringVar()
        self.result_header.set("========================================GUI-Pylint========================================")

        self.frame = tk.Frame(mainapp)
        self.frame.config(bg=self.bgapp)
        self.frame.pack()

        self.menubar = tk.Menu(mainapp) #create menu bar
        self.help_menu = tk.Menu(self.menubar, tearoff=0) #create "Help" menu
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="View Guide")
        self.help_menu.add_command(label="About", command=self.about_window)
        mainapp.config(menu=self.menubar)

        self.applogo_img = tk.PhotoImage(file="gpy-logo.gif")
        self.applogo = tk.Label(self.frame, image=self.applogo_img)
        self.applogo.config(bg=self.bgapp)
        self.applogo.applogo_img = self.applogo_img

        self.applogo.pack()

        self.apptitle = tk.Label(self.frame, text="A Python Code Checker for Right Style Guide", font=(self.appfont, 10))
        self.apptitle.config(bg=self.bgapp)
        self.apptitle.pack()

        self.path_text = tk.Label(self.frame, textvariable=self.file_path, font=(self.appfont, 12))
        self.path_text.config(bg=self.bgapp)
        self.path_text.pack(padx=5, pady=20)

        self.browse = tk.Button(self.frame, text="Browse", font=(self.appfont, 14), fg='white', bg='#4183D7', activebackground='#3871BA', activeforeground='white', command=self.open_file)
        self.browse.config(borderwidth=0, width=15, height=2)
        self.browse.pack(side=tk.LEFT)

        self.upload = tk.Button(self.frame, text="Upload", font=(self.appfont, 14), fg='white', bg='#4183D7', activebackground='#3871BA', activeforeground='white', command=self.gpylint_checker)
        self.upload.config(borderwidth=0, width=15, height=2)
        self.upload.pack(side=tk.RIGHT, pady=10)

    def about_window(self):
        """Display About Window by Help>About"""
        self.about = tk.Toplevel()
        self.about.geometry("300x200+300+300")
        self.about.config(bg=self.bgapp)
        self.about.focus_set()
        self.about.grab_set()
        self.about.resizable(0,0)
        self.about.title("About This Application")
        self.appversion = tk.Label(self.about, text="GUI-Pylint v0.1", font=(self.appfont, 16)).pack()
        self.dev_a = tk.Label(self.about, text="Sirirach Junta 57070112", font=(self.appfont, 14)).pack()
        self.dev_b = tk.Label(self.about, text="Worapong Malaiwong 57070103", font=(self.appfont, 14)).pack()

    def open_file(self):
        """Open Python file by Browse Button"""
        self.name = file_dialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if self.name != '':
            self.file_path.set(self.name)
        #python_file = open(name, "r")

    def gpylint_checker(self):
        """Send file to gpylint via internet by Upload Button"""
        if self.file_path.get() == 'No File Selected...':
            dialog.showerror(title="GUI-Pylint", message="Please Select a file before upload.")
        else:
            obj = Gpylint()
            obj.analysis(self.file_path.get().replace('/', '\\'))
            result = obj.read()
            print result #for test
            if 'Error' in result:
                dialog.showerror(title="Error", message=result['Error']['Status'])
            self.result_windows = tk.Toplevel()
            self.result_windows.resizable(0,0)
            listbox = tk.Listbox(self.result_windows, width=116, height=(len(result['Pass']['Data'])+5))
            listbox.pack()
            listbox.insert(tk.END, self.result_header.get())
            listbox.insert(tk.END, self.file_path.get())
            if result['Pass']['Data'] == []:
                listbox.insert(tk.END, "========================================No Problem!========================================")
            else:
                for item in result['Pass']['Data']:
                    listbox.insert(tk.END, item)

def main():
    root = tk.Tk()
    root.geometry("500x350+500+500")
    Aplication(root)
    root.mainloop()

main()
