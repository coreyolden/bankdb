import tkinter as tk
import string
import mysql.connector as dbconn
import datetime

# set up connection to server
db = dbconn.connect(host="localhost", \
                 user="root", passwd="root", db="bankdb")
cursor = db.cursor()


customerID =""
customerPassword =""



class login(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        #need a button to add new account and a button + 2 textboxes
        #for password and login. call login when pressed and have an if
        #statement based off of the input. load mainPage if int is good.


class makeAccount(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        #ask for email address and password. pop up a new window with
        #the new customer id and an okay button that takes you back
        #to the login page.

class displayID(tk.Frame):
    def __init__(self):


class mainPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
    #display all accounts, loans, and credit card numbers. we will need
    #a few options on the side for things like make payment.


#the view after you select the account
class inaccount(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        #display current balance as well as listing transactions


#the view inside the loans dialog.
class viewLoans(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        #things like pay loan, due date, past transactions, total amount.




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
    root = tk.Tk()
    app = login(root)
    app.mainloop()