import sys
import UpdateInfo
import Account

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

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
    top = LandingPage (root)
    LoginSupport.init(root, top)
    root.mainloop()

w = None
def create_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = LandingPage (w)
    LoginSupport.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Login():
    global w
    w.destroy()
    w = None


class LandingPage:

    def UpdateSettings(self):
        LoginSupport.destroy_window()
        UpdateInfo.vp_start_gui(accountid)
    def NewAccount(self):
        LoginSupport.destroy_window()
        Account.vp_start_gui(accountid)
    def killApp(self):
        messagebox.showinfo("note", "You have successfully signed out")
        LoginSupport.destroy_window()
    def intoAccount(self,account):
        LoginSupport.destroy_window()
        Account.vp_start_gui(account, accountid)


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 9 -weight normal -slant "  \
            "roman -underline 1 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("800x719+365+67")
        top.title("Main page")
        top.configure(background="#91d98c")
        root.resizable(False, False)

        sql = "SELECT accountname, accountnumber, currentbalance FROM customers NATURAL JOIN accounts WHERE customerid = %d" % \
              (accountid)
        cursor.execute(sql)
        space = 0
        for (accountname,account,  currentbalance) in cursor:

            currentbalance = str(currentbalance)



            self.loanButtons = Button(top)
            texts = "%s          $%s" % \
                    (accountname, currentbalance)
            self.loanButtons.place(relx=0.48, rely=0.2+space, height=27, width=400)
            self.loanButtons.configure(activebackground="#FFFFFF")
            self.loanButtons.configure(activeforeground="#FFFFFF")
            self.loanButtons.configure(background="#FFFFFF")
            self.loanButtons.configure(relief=FLAT)
            self.loanButtons.configure(text=texts, command=lambda account=account: self.intoAccount(account))
            #self.loanbuttons.configure( command=lambda account=account: self.intoAccount(account))
            space += .04

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.03, rely=0.07, relheight=0.48, relwidth=0.43)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFFFFF")
        self.Frame1.configure(width=275)



        self.makeAccountButton = Button(self.Frame1)
        self.makeAccountButton.place(relx=0.18, rely=0.22, height=27, width=200)
        self.makeAccountButton.configure(activebackground="#FFFFFF")
        self.makeAccountButton.configure(activeforeground="#FFFFFF")
        self.makeAccountButton.configure(background="#FFFFFF")
        self.makeAccountButton.configure(relief=FLAT)
        self.makeAccountButton.configure(text='''Make new account''')
        self.makeAccountButton.configure(command = self.NewAccount)


        self.makePaymentButton = Button(self.Frame1)
        self.makePaymentButton.place(relx=0.18, rely=0.32, height=27, width=200)
        self.makePaymentButton.configure(activebackground="#FFFFFF")
        self.makePaymentButton.configure(activeforeground="#FFFFFF")
        self.makePaymentButton.configure(background="#FFFFFF")
        self.makePaymentButton.configure(relief=FLAT)
        self.makePaymentButton.configure(text='''Make Payment''')

        self.loanButton = Button(self.Frame1)
        self.loanButton.place(relx=0.18, rely=0.42, height=27, width=200)
        self.loanButton.configure(activebackground="#FFFFFF")
        self.loanButton.configure(activeforeground="#FFFFFF")
        self.loanButton.configure(background="#FFFFFF")
        self.loanButton.configure(relief=FLAT)
        self.loanButton.configure(text='''Apply for a loan''')

        self.settingButton = Button(self.Frame1)
        self.settingButton.place(relx=0.18, rely=0.52, height=27, width=200)
        self.settingButton.configure(activebackground="#FFFFFF")
        self.settingButton.configure(activeforeground="#FFFFFF")
        self.settingButton.configure(background="#FFFFFF")
        self.settingButton.configure(relief=FLAT)
        self.settingButton.configure(text='''Change settings''')
        self.settingButton.configure(command= self.UpdateSettings)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.91, height=27, width=200)
        self.Button4.configure(activebackground="#FFFFFF")
        self.Button4.configure(activeforeground="#FFFFFF")
        self.Button4.configure(font=font10)
        self.Button4.configure(text='''Sign out''')
        self.Button4.configure(command = self.killApp)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.18, rely=0.08, height=19, width=200)
        self.Label1.configure(background="#FFFFFF")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ab0000")
        self.Label1.configure(text='''Options''')
        self.Label1.configure(width=176)





if __name__ == '__main__':
    vp_start_gui()


