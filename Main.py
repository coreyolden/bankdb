import sys
import string
#set up connection to server
import MySQLdb
db = MySQLdb.connect()
db = MySQLdb.connect(host="localhost", \
                user="root", passwd="oldenbec.09r", db="bankdb")
cursor = db.cursor()



import datetime
import NewCustomer
import LandingPage




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

table = str.maketrans(dict.fromkeys('(' ',)'))


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Login (root)
    LoginSupport.init(root, top)
    root.mainloop()

w = None
def create_Login(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Login (w)
    LoginSupport.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Login():
    global w
    w.destroy()
    w = None


class Login:

    def createCustomer(self):
        LoginSupport.destroy_window()
        NewCustomer.vp_start_gui()




    def LogSubmitFun(self):
        #gets the account id and password
        accountID = self.LogAccountBox.get()
        pWord = self.LogPassBox.get()

        if (len(accountID)>0 and len(pWord) > 0):
            try:
                accountID = int(accountID)
            except:
                messagebox.showerror("Error", "Account ID must be an Integer")
                return

            cusid = 0
            sql="SELECT customerid FROM customers"
            cursor.execute(sql)
            for(custids) in cursor:
                custids = str(custids)
                custids = custids.translate(table)
                custids = int(custids)

                if(custids == accountID):
                    cusid = 1


            if (cusid == 0):
                messagebox.showerror("Error", "That is not a account holder at our bank")
                return

            getpass = "Select customerid FROM customers WHERE customerid = %d AND password ='%s'" %\
                      (accountID, pWord)
            cursor.execute(getpass)
            passcorrect = 0
            for (custids) in cursor:
                passcorrect = passcorrect+1

            if(passcorrect ==1):
                # load mainpage
                messagebox.showinfo("It Worked", "You successfully signed in")
                LoginSupport.destroy_window()
                LandingPage.vp_start_gui(accountID)
            else:
                messagebox.showerror("Error", "The password is incorrect")
                return



        else:
            messagebox.showerror("Error", "Both password and accountID are required fields")


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("800x719+365+67")
        top.title("Login")
        top.configure(background="#93d993")
        root.resizable(False, False)



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.29, rely=0.19, relheight=0.59, relwidth=0.39)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#68d9c3")
        self.Frame1.configure(width=315)

        self.LogAccountBox = Entry(self.Frame1)
        self.LogAccountBox.place(relx=0.19, rely=0.21, relheight=0.05
                , relwidth=0.46)
        self.LogAccountBox.configure(background="white")
        self.LogAccountBox.configure(font="TkFixedFont")

        self.LogPassBox = Entry(self.Frame1)
        self.LogPassBox.place(relx=0.19, rely=0.31, relheight=0.05
                , relwidth=0.46)
        self.LogPassBox.configure(background="white")
        self.LogPassBox.configure(font="TkFixedFont")

        self.LogAccountLabel = Label(self.Frame1)
        self.LogAccountLabel.place(relx=0.19, rely=0.16, height=18, width=69)
        self.LogAccountLabel.configure(activebackground="#68d9c3")
        self.LogAccountLabel.configure(background="#68d9c3")
        self.LogAccountLabel.configure(text='''Account ID''')

        self.LogPassLabel = Label(self.Frame1)
        self.LogPassLabel.place(relx=0.19, rely=0.26, height=18, width=66)
        self.LogPassLabel.configure(activebackground="#68d9c3")
        self.LogPassLabel.configure(background="#68d9c3")
        self.LogPassLabel.configure(text='''Password''')
        self.LogPassLabel.configure(width=66)

        self.LogSubmitButton = Button(self.Frame1)
        self.LogSubmitButton.place(relx=0.19, rely=0.38, height=26, width=70)
        self.LogSubmitButton.configure(activebackground="#d9d9d9")
        self.LogSubmitButton.configure(background="#d9d91c")
        self.LogSubmitButton.configure(text='''Submit''')
        self.LogSubmitButton.configure(command = self.LogSubmitFun)

        self.LogMakeAccount = Button(self.Frame1)
        self.LogMakeAccount.place(relx=0.19, rely=0.79, height=26, width=200)
        self.LogMakeAccount.configure(activebackground="#d9d9d9")
        self.LogMakeAccount.configure(background="#d9d91c")
        self.LogMakeAccount.configure(text='''Forgot account ID?''')

        self.LogMakeAccount = Button(self.Frame1)
        self.LogMakeAccount.place(relx=0.19, rely=0.89, height=26, width=200)
        self.LogMakeAccount.configure(activebackground="#d9d9d9")
        self.LogMakeAccount.configure(background="#d9d91c")
        self.LogMakeAccount.configure(text='''Don't have an account?''')
        self.LogMakeAccount.configure(command = self.createCustomer)






if __name__ == '__main__':
    vp_start_gui()



