from tkinter import *
import string
import mysql.connector as dbconn
import datetime
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Mainpage_support
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Main_page (root)
    Mainpage_support.init(root, top)
    root.mainloop()

w = None
def create_Main_page(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Main_page (w)
    Mainpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main_page():
    global w
    w.destroy()
    w = None

# set up connection to server
db = dbconn.connect(host="localhost", \
                 user="root", passwd="root", db="bankdb")
cursor = db.cursor()


customerID =""
customerPassword =""

#
#
# class login(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self, parent)
#         #need a button to add new account and a button + 2 textboxes
#         #for password and login. call login when pressed and have an if
#         #statement based off of the input. load mainPage if int is good.
#
#
# class makeAccount(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self, parent)
#         #ask for email address and password. pop up a new window with
#         #the new customer id and an okay button that takes you back
#         #to the login page.




class Main_page:
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

        top.geometry("1000x800+359+791")
        top.title("Main page")
        top.configure(background="#91d98c")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.09, relheight=0.62, relwidth=0.28)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FFFFFF")
        self.Frame1.configure(width=275)

        self.makeAccountButton = Button(self.Frame1)
        self.makeAccountButton.place(relx=0.11, rely=0.22, height=27, width=200)
        self.makeAccountButton.configure(activebackground="#FFFFFF")
        self.makeAccountButton.configure(activeforeground="#FFFFFF")
        self.makeAccountButton.configure(background="#FFFFFF")
        self.makeAccountButton.configure(relief=FLAT)
        self.makeAccountButton.configure(text='''Make new account''')

        self.makePaymentButton = Button(self.Frame1)
        self.makePaymentButton.place(relx=0.11, rely=0.3, height=27, width=200)
        self.makePaymentButton.configure(activebackground="#FFFFFF")
        self.makePaymentButton.configure(background="#FFFFFF")
        self.makePaymentButton.configure(relief=FLAT)
        self.makePaymentButton.configure(text='''Make Payment''')

        self.loanButton = Button(self.Frame1)
        self.loanButton.place(relx=0.11, rely=0.38, height=27, width=200)
        self.loanButton.configure(activebackground="#d9d9d9")
        self.loanButton.configure(background="#FFFFFF")
        self.loanButton.configure(relief=FLAT)
        self.loanButton.configure(text='''Apply for a loan''')

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.11, rely=0.91, height=27, width=200)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(font=font10)
        self.Button4.configure(text='''Sign out''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.11, rely=0.08, height=19, width=200)
        self.Label1.configure(background="#FFFFFF")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ab0000")
        self.Label1.configure(text='''Options''')
        self.Label1.configure(width=176)

        self.listAccounts = Listbox(top)
        self.listAccounts.place(relx=0.33, rely=0.05, relheight=0.91
                , relwidth=0.64)
        self.listAccounts.configure(background="white")
        self.listAccounts.configure(font="TkFixedFont")
        self.listAccounts.configure(width=644)


# #the view after you select the account
# class inaccount(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self, parent)
#         #display current balance as well as listing transactions
#
#
# #the view inside the loans dialog.
# class viewLoans(tk.Frame):
#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self, parent)
#         #things like pay loan, due date, past transactions, total amount.
#



#used when logging in, creating an account, or paying a bill.
def verifyInteger(toCheck):
    try:
        toCheck=int(toCheck)
        return 1
    except:
        return 0

def logInButton(self):
    # the login screen will have new account or log in buttons
    #need to check if values must be passed or if this can get them from main.
    sql = "SELECT * FROM customers WHERE customerid = %d AND customerpassword = %s" % \
          (customerID, customerPassword)


def onClickNewAccount(self):
    #the login screen will have new account or log in buttons



if __name__ == '__main__':
    vp_start_gui()