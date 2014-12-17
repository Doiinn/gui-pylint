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
        mainapp.resizable(0, 0)
        mainapp.config(bg='white')
        mainapp.title("GUI-Pylint")

        #Variable
        self.bgapp = 'white'
        self.appfont = 'Segoe UI'
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
        self.help_menu.add_command(label="View Guide", command=self.guide_window)
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
        self.about.geometry("300x180+500+280")
        self.about.config(bg=self.bgapp)
        self.about.focus_set()
        self.about.grab_set()
        self.about.resizable(0,0)
        self.about.title("About This Application")
        self.appversion = tk.Label(self.about, text="GUI-Pylint v1.0", font=(self.appfont, 16), bg='white').pack()
        self.dev_a = tk.Label(self.about, text="Sirirach Junta 57070112", font=(self.appfont, 10), bg='white').pack()
        self.dev_b = tk.Label(self.about, text="Worapong Malaiwong 57070103", font=(self.appfont, 10), bg='white').pack()
        self.edu = tk.Label(self.about, text="King Mongkut's Institute of Technology Ladkrabang", font=(self.appfont, 8), bg='white').pack(pady=10)
        self.edu2 = tk.Label(self.about, text="This app coding for PSIT Project", font=(self.appfont, 12), bg='white').pack(pady=0)
        self.edu2 = tk.Label(self.about, text="and a part of PSIT Subject", font=(self.appfont, 12), bg='white').pack(pady=0)

    def guide_window(self):
        """Display Guide Window by Help>View Guide"""
        self.guide = tk.Toplevel()
        self.guide.geometry("500x300+400+100")
        self.guide.config(bg=self.bgapp)
        self.guide.grab_set()
        self.guide.resizable(0,0)
        self.guide.title("View Guide")
        self.guide_a = tk.Label(self.guide, text="How to Use", font=(self.appfont, 16), bg='white').pack(pady=20)
        self.guide_b = tk.Label(self.guide, text="Click \"Browse\" button to select python file for check", font=(self.appfont, 12), bg='white').pack()
        self.guide_c = tk.Label(self.guide, text="Click \"Upload\" button to send file upload to server", font=(self.appfont, 12), bg='white').pack()
        self.guide_d = tk.Label(self.guide, text="Waiting for response", font=(self.appfont, 12), bg='white').pack()
        self.guide_e = tk.Label(self.guide, text="After recieve response, GUI-Pylint show result window", font=(self.appfont, 12), bg='white').pack()
        self.guide_f = tk.Label(self.guide, text="If your code are good, App will show \"No Problem!\"", font=(self.appfont, 12), bg='white').pack()
        self.guide_g = tk.Label(self.guide, text="If code isn't based on Python Style Guide", font=(self.appfont, 12), bg='white').pack()
        self.guide_h = tk.Label(self.guide, text="App will show problem of code", font=(self.appfont, 12), bg='white').pack()

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
            if 'Error' in result:
                dialog.showerror(title="Error", message=result['Error']['Status'])
            self.result_windows = tk.Toplevel()
            self.result_windows.minsize(width=666, height=366)
            self.result_windows.resizable(0, 0)
            self.result_windows.title(self.file_path.get())
            self.gpy_frame = tk.Frame(self.result_windows)
            self.gpy_frame.config(bg=self.bgapp)
            self.gpy_frame.pack()
            self.scrollbar = tk.Scrollbar(self.gpy_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.listbox = tk.Listbox(self.gpy_frame, width=116, height=20, yscrollcommand=self.scrollbar.set)
            self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
            self.scrollbar.config(command=self.listbox.yview)
            self.listbox.insert(tk.END, self.result_header.get())
            self.listbox.insert(tk.END, self.file_path.get())
            if result['Pass']['Data'] == []:
                self.listbox.insert(tk.END, "========================================No Problem!========================================")
            else:
                for item in result['Pass']['Data']:
                    self.listbox.insert(tk.END, item)
            self.gpy_found = tk.Label(self.result_windows, text="Found "+str(len(result['Pass']['Data']))+" Problem", font=(self.appfont, 16)).pack()
            self.gpy_pattern = tk.Label(self.result_windows, text="MESSAGE_TYPE, LINE_NUMBER, CHARACTER (Ex: C, 1,5)").pack()
            self.gpy_message = tk.Label(self.result_windows, text="Message Type in Pylint").pack()
            self.gpy_c = tk.Label(self.result_windows, text="(C) convention, for programming standard violation").pack()
            self.gpy_r = tk.Label(self.result_windows, text="(R) refactor, for bad code smell").pack()
            self.gpy_w = tk.Label(self.result_windows, text="(W) warning, for python specific problems").pack()
            self.gpy_e = tk.Label(self.result_windows, text="(E) error, for much probably bugs in the code").pack()
            self.gpy_f = tk.Label(self.result_windows, text="(F) fatal, if an error occurred which prevented pylint from doing further processing").pack()

def main():
    """run application"""
    root = tk.Tk()
    root.geometry("500x350+400+175")
    Aplication(root)
    root.mainloop()

main()
