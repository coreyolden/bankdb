import sys
import UpdateInfo
import Account
import RequestLoan
import NewAccount
import Loan
import Main
import CreditCard
import RequestCC
import MakePayment

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

def destroy_LandingPage():
    global w
    w.destroy()
    w = None


class LandingPage:

    def UpdateSettings(self):
        LoginSupport.destroy_window()
        UpdateInfo.vp_start_gui(accountid)
    def NewAccount(self):
        LoginSupport.destroy_window()
        NewAccount.vp_start_gui(accountid)
    def killApp(self):
        messagebox.showinfo("note", "You have successfully signed out")
        db.close()
        LoginSupport.destroy_window()
        Main.vp_start_gui()
    def intoAccount(self,account):
        LoginSupport.destroy_window()
        Account.vp_start_gui(account, accountid)
    def intoloan(self,account):
        LoginSupport.destroy_window()
        Loan.vp_start_gui(account,accountid)
    def creditCard(self,account):
        LoginSupport.destroy_window()
        CreditCard.vp_start_gui(account, accountid)
    def loan(self):
        LoginSupport.destroy_window()
        RequestLoan.vp_start_gui(accountid)
    def Requestcc(self):
        LoginSupport.destroy_window()
        RequestCC.vp_start_gui(accountid)
    def makepayment(self):
        LoginSupport.destroy_window()
        MakePayment.vp_start_gui(accountid)

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

        self.Accountlabel = Label(top)
        self.Accountlabel.place(relx=0.6, rely=0.15, height=19, width=200)
        self.Accountlabel.configure(background="#FFFFFF")
        self.Accountlabel.configure(font=font9)
        self.Accountlabel.configure(foreground="#000000")
        self.Accountlabel.configure(text='''Accounts''')
        self.Accountlabel.configure(width=176)

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
            self.loanButtons.configure(activeforeground="#000000")
            self.loanButtons.configure(background="#FFFFFF")
            self.loanButtons.configure(relief=FLAT)
            self.loanButtons.configure(text=texts, command=lambda account=account: self.intoAccount(account))
            space += .04

        self.Loanslabel = Label(top)
        self.Loanslabel.place(relx=0.6, rely=0.45, height=19, width=200)
        self.Loanslabel.configure(background="#FFFFFF")
        self.Loanslabel.configure(font=font9)
        self.Loanslabel.configure(foreground="#000000")
        self.Loanslabel.configure(text='''Loans''')
        self.Loanslabel.configure(width=176)

        sql = "SELECT loanname, accountnumber, ammountleft FROM customers NATURAL JOIN loans WHERE customerid = %d" % \
              (accountid)
        cursor.execute(sql)

        space = 0
        for (loanname, account, currentbalance) in cursor:
            currentbalance = str(currentbalance)

            self.loanButtons = Button(top)
            texts = "%s          $%s" % \
                    (loanname, currentbalance)
            self.loanButtons.place(relx=0.48, rely=0.5 + space, height=27, width=400)
            self.loanButtons.configure(activebackground="#FFFFFF")
            self.loanButtons.configure(activeforeground="#000000")
            self.loanButtons.configure(background="#FFFFFF")
            self.loanButtons.configure(relief=FLAT)
            self.loanButtons.configure(text=texts, command=lambda account=account: self.intoloan(account))
            space += .04

        self.Loanslabel = Label(top)
        self.Loanslabel.place(relx=0.6, rely=0.8, height=19, width=200)
        self.Loanslabel.configure(background="#FFFFFF")
        self.Loanslabel.configure(font=font9)
        self.Loanslabel.configure(foreground="#000000")
        self.Loanslabel.configure(text='''Credit Cards''')
        self.Loanslabel.configure(width=176)

        sql = "SELECT cardnumber, currentbalance FROM CreditCard WHERE customerid = %d" % \
              (accountid)
        cursor.execute(sql)
        space = 0
        for (cardnumber, currentbalance) in cursor:
            currentbalance = str(currentbalance)
            self.loanButtons = Button(top)
            texts = "%s          $%s" % \
                    (cardnumber, currentbalance)
            self.loanButtons.place(relx=0.48, rely=0.85 + space, height=27, width=400)
            self.loanButtons.configure(activebackground="#FFFFFF")
            self.loanButtons.configure(activeforeground="#000000")
            self.loanButtons.configure(background="#FFFFFF")
            self.loanButtons.configure(relief=FLAT)
            self.loanButtons.configure(text=texts, command=lambda account=cardnumber: self.creditCard(account))
            space += .04

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.03, rely=0.2, relheight=0.48, relwidth=0.43)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFFFFF")
        self.Frame1.configure(width=275)



        self.makeAccountButton = Button(self.Frame1)
        self.makeAccountButton.place(relx=0.18, rely=0.22, height=27, width=200)
        self.makeAccountButton.configure(activebackground="#FFFFFF")
        self.makeAccountButton.configure(activeforeground="#000000")
        self.makeAccountButton.configure(background="#FFFFFF")
        self.makeAccountButton.configure(relief=FLAT)
        self.makeAccountButton.configure(text='''Make new account''')
        self.makeAccountButton.configure(command = self.NewAccount)


        self.makePaymentButton = Button(self.Frame1)
        self.makePaymentButton.place(relx=0.18, rely=0.32, height=27, width=200)
        self.makePaymentButton.configure(activebackground="#FFFFFF")
        self.makePaymentButton.configure(activeforeground="#000000")
        self.makePaymentButton.configure(background="#FFFFFF")
        self.makePaymentButton.configure(relief=FLAT)
        self.makePaymentButton.configure(text='''Make Payment''')
        self.makePaymentButton.configure(command = self.makepayment)

        self.loanButton = Button(self.Frame1)
        self.loanButton.place(relx=0.18, rely=0.42, height=27, width=200)
        self.loanButton.configure(activebackground="#FFFFFF")
        self.loanButton.configure(activeforeground="#000000")
        self.loanButton.configure(background="#FFFFFF")
        self.loanButton.configure(relief=FLAT)
        self.loanButton.configure(text='''Apply for a loan''')
        self.loanButton.configure(command = self.loan)

        self.CreditcardButton = Button(self.Frame1)
        self.CreditcardButton.place(relx=0.18, rely=0.52, height=27, width=200)
        self.CreditcardButton.configure(activebackground="#FFFFFF")
        self.CreditcardButton.configure(activeforeground="#000000")
        self.CreditcardButton.configure(background="#FFFFFF")
        self.CreditcardButton.configure(relief=FLAT)
        self.CreditcardButton.configure(text='''Sign up for a credit card''')
        self.CreditcardButton.configure(command=self.Requestcc)

        self.settingButton = Button(self.Frame1)
        self.settingButton.place(relx=0.18, rely=0.62, height=27, width=200)
        self.settingButton.configure(activebackground="#FFFFFF")
        self.settingButton.configure(activeforeground="#000000")
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


