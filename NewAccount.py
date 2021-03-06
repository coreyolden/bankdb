
import sys
import LandingPage
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
from tkinter import messagebox
import LoginSupport
import MySQLdb
db = MySQLdb.connect()
db = MySQLdb.connect(host="localhost", \
                user="root", passwd="oldenbec.09r", db="bankdb")
cursor = db.cursor()

def vp_start_gui(Accountid):
    '''Starting point when module is the main routine.'''
    global accountid
    accountid = Accountid
    global val, w, root
    root = Tk()
    LoginSupport.set_Tk_var()
    top = New_Account (root)
    LoginSupport.init(root, top)
    root.mainloop()

w = None
def create_New_Account(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    LoginSupport.set_Tk_var()
    top = New_Account (w)
    LoginSupport.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Account():
    global w
    w.destroy()
    w = None



class New_Account:

    def cancelbutton(self):
        LoginSupport.destroy_window()
        LandingPage.vp_start_gui(accountid)

    def submit(self):
        name = self.Entry1.get()
        if(self.var1.get() == 1):
            accountnum = 1
            getaccountnum = "SELECT MAX(accountnumber) FROM accounts WHERE accountnumber <2000000;"
            cursor.execute(getaccountnum)
            for (number) in cursor:
                number = str(number)
                table = str.maketrans(dict.fromkeys('(' ',)'))
                number = number.translate(table)

                accountnum +=int(number)

            sql = "INSERT INTO `accounts` VALUES (%d, '%s',%d,0,0)" % \
                 (accountid, name, accountnum)
            cursor.execute(sql)
            try:
                db.commit()
                messagebox.showinfo("Congrats", "Account created")
                db.close()
                LoginSupport.destroy_window()
                LandingPage.vp_start_gui(accountid)
            except:
                messagebox.showerror("Error","Account could not be created")

        elif(self.var1.get() == 2):
            accountnum = 1
            getaccountnum = "SELECT MAX(accountnumber) FROM accounts WHERE accountnumber <3000000;"
            cursor.execute(getaccountnum)
            for (number) in cursor:
                number = str(number)
                table = str.maketrans(dict.fromkeys('(' ',)'))
                number = number.translate(table)

                accountnum += int(number)

            sql = "INSERT INTO `accounts` VALUES (%d, '%s',%d,0,0)" % \
                  (accountid, name, accountnum)
            cursor.execute(sql)
            try:
                db.commit()
                messagebox.showinfo("Congrats", "Account created")
                db.close()
                LoginSupport.destroy_window()
                LandingPage.vp_start_gui(accountid)
            except:
                messagebox.showerror("Error", "Account could not be created")
        elif(self.var1.get() == 3):
            accountnum = 1
            getaccountnum = "SELECT MAX(accountnumber) FROM accounts WHERE accountnumber <4000000;"
            cursor.execute(getaccountnum)
            for (number) in cursor:
                number = str(number)
                table = str.maketrans(dict.fromkeys('(' ',)'))
                number = number.translate(table)

                accountnum += int(number)

            sql = "INSERT INTO `accounts` VALUES (%d, '%s',%d,0,0)" % \
                  (accountid, name, accountnum)
            cursor.execute(sql)
            try:
                db.commit()
                messagebox.showinfo("Congrats", "Account created")
                db.close()
                LoginSupport.destroy_window()
                LandingPage.vp_start_gui(accountid)
            except:
                messagebox.showerror("Error", "Account could not be created")



    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("800x719+365+67")
        top.title("New Account")
        top.configure(background="#93d993")
        root.resizable(False, False)
        self.var1 = IntVar()



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.35, rely=0.36, relheight=0.04, relwidth=0.31)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.35, rely=0.31, height=31, width=123)
        self.Label1.configure(background="#93d993")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Account Name''')

        self.Message1 = Message(top)
        self.Message1.place(relx=0.3, rely=0.45, relheight=0.41, relwidth=0.49)
        self.Message1.configure(background="#93d993")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''To create a new account at our institution simply
select what type of account it is, enter a name
and press submit''')
        self.Message1.configure(width=392)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.38, rely=0.45, height=42, width=72)
        self.Button1.configure(activebackground="#2cd900")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#2cd900")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command = self.submit)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.54, rely=0.45, height=42, width=68)
        self.Button2.configure(activebackground="#f48042")
        self.Button2.configure(background="#f48042")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#f48042")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Cancel''')
        self.Button2.configure(command = self.cancelbutton)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.06, rely=0.32, relheight=0.17, relwidth=0.24)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ceffdb")
        self.Frame1.configure(width=195)

        self.Radiobutton1 = Radiobutton(self.Frame1)
        self.Radiobutton1.place(relx=0.05, rely=0.08, relheight=0.3, relwidth=0.87)
        self.Radiobutton1.configure(activebackground="#ceffdb")
        self.Radiobutton1.configure(background="#ceffdb")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(borderwidth="0")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#ceffdb")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Checking account''')
        self.Radiobutton1.configure(value="1")
        self.Radiobutton1.configure(variable= self.var1)

        self.Radiobutton2 = Radiobutton(self.Frame1)
        self.Radiobutton2.place(relx=0.05, rely=0.32, relheight=0.3, relwidth=0.8)
        self.Radiobutton2.configure(activebackground="#ceffdb")
        self.Radiobutton2.configure(background="#ceffdb")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#ceffdb")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Saving account''')
        self.Radiobutton2.configure(value="2")
        self.Radiobutton2.configure(variable= self.var1)

        self.Radiobutton3 = Radiobutton(self.Frame1)
        self.Radiobutton3.place(relx=0.05, rely=0.56, relheight=0.3, relwidth=0.65)
        self.Radiobutton3.configure(activebackground="#ceffdb")
        self.Radiobutton3.configure(background="#ceffdb")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#ceffdb")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Other type''')
        self.Radiobutton3.configure(value="3")
        self.Radiobutton3.configure(variable=self.var1)






if __name__ == '__main__':
    vp_start_gui()

