import sys

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

import LoginSupport

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    LoginSupport.set_Tk_var()
    top = Request_a_loan (root)
    LoginSupport.init(root, top)
    root.mainloop()

w = None
def create_Request_a_loan(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    LoginSupport.set_Tk_var()
    top = Request_a_loan (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Request_a_loan():
    global w
    w.destroy()
    w = None


class Request_a_loan:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x719+720+110")
        top.title("Request a loan")
        top.configure(background="#93d993")



        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.46, rely=0.36, relheight=0.04, relwidth=0.31)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.46, rely=0.31, height=31, width=114)
        self.Label1.configure(background="#93d993")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Name of loan''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.46, rely=0.45, height=42, width=72)
        self.Button1.configure(activebackground="#2cd900")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#2cd900")
        self.Button1.configure(command=_support.accountsubmit)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.59, rely=0.45, height=42, width=66)
        self.Button2.configure(activebackground="#f48042")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#f48042")
        self.Button2.configure(command=_support.accountcancel)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Cancel''')

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.06, rely=0.32, relheight=0.27, relwidth=0.31)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ceffdb")
        self.Frame1.configure(width=245)

        self.Radiobutton1 = Radiobutton(self.Frame1)
        self.Radiobutton1.place(relx=0.04, rely=0.05, relheight=0.19
                , relwidth=0.69)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ceffdb")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Used vehicle loan''')
        self.Radiobutton1.configure(value="1")
        self.Radiobutton1.configure(variable=_support.Type)

        self.Radiobutton2 = Radiobutton(self.Frame1)
        self.Radiobutton2.place(relx=0.04, rely=0.21, relheight=0.19
                , relwidth=0.67)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ceffdb")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''New vehicle loan''')
        self.Radiobutton2.configure(value="2")
        self.Radiobutton2.configure(variable=_support.Type)

        self.Radiobutton3 = Radiobutton(self.Frame1)
        self.Radiobutton3.place(relx=0.04, rely=0.36, relheight=0.19
                , relwidth=0.49)
        self.Radiobutton3.configure(activebackground="#d9d9d9")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#ceffdb")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify=LEFT)
        self.Radiobutton3.configure(text='''Home loan''')
        self.Radiobutton3.configure(value="3")
        self.Radiobutton3.configure(variable=_support.Type)

        self.Radiobutton4 = Radiobutton(self.Frame1)
        self.Radiobutton4.place(relx=0.04, rely=0.51, relheight=0.19
                , relwidth=0.54)
        self.Radiobutton4.configure(activebackground="#d9d9d9")
        self.Radiobutton4.configure(activeforeground="#000000")
        self.Radiobutton4.configure(background="#ceffdb")
        self.Radiobutton4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton4.configure(foreground="#000000")
        self.Radiobutton4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton4.configure(highlightcolor="black")
        self.Radiobutton4.configure(justify=LEFT)
        self.Radiobutton4.configure(text='''Student loan''')
        self.Radiobutton4.configure(value="4")
        self.Radiobutton4.configure(variable=_support.Type)

        self.Radiobutton5 = Radiobutton(self.Frame1)
        self.Radiobutton5.place(relx=0.04, rely=0.67, relheight=0.19
                , relwidth=0.56)
        self.Radiobutton5.configure(activebackground="#d9d9d9")
        self.Radiobutton5.configure(activeforeground="#000000")
        self.Radiobutton5.configure(background="#ceffdb")
        self.Radiobutton5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton5.configure(foreground="#000000")
        self.Radiobutton5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton5.configure(highlightcolor="black")
        self.Radiobutton5.configure(justify=LEFT)
        self.Radiobutton5.configure(text='''Personal loan''')
        self.Radiobutton5.configure(value="5")
        self.Radiobutton5.configure(variable=_support.Type)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.41, rely=0.57, relheight=0.33, relwidth=0.5)

        self.TNotebook1.configure(width=300)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Vehical loans",underline="-1",)
        self.TNotebook1_t1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Home loan",underline="-1",)
        self.TNotebook1_t2 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Student",underline="-1",)
        self.TNotebook1_t3 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="Personal loan",underline="-1",)

        self.Message1 = Message(self.TNotebook1_t1)
        self.Message1.place(relx=0.0, rely=0.05, relheight=0.64, relwidth=0.99)
        self.Message1.configure(background="#ceffdb")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Vehicle loans are now as low as 4.5%
for a new vehicle loan and 2.3% for a used vehicle loan''')
        self.Message1.configure(width=392)

        self.Message2 = Message(self.TNotebook1_t1)
        self.Message2.place(relx=0.1, rely=0.05, relheight=0.89, relwidth=0.83)
        self.Message2.configure(background="#ceffdb")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''At our bank your family is important to us and thats why we
offer home loan rates as low as 90% interest with 60% down.''')
        self.Message2.configure(width=327)

        self.Message3 = Message(self.TNotebook1_t2)
        self.Message3.place(relx=0.1, rely=0.1, relheight=0.69, relwidth=0.84)
        self.Message3.configure(background="#ceffdb")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Don't worry about paying until you graduate
we're sure starbucks will cover the 30% interest.''')
        self.Message3.configure(width=331)

        self.Message4 = Message(self.TNotebook1_t3)
        self.Message4.place(relx=0.18, rely=0.1, relheight=0.61, relwidth=0.56)
        self.Message4.configure(background="#ceffdb")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text='''We know things come up in live and thats why we're offering personal loans at only 4%''')
        self.Message4.configure(width=222)






if __name__ == '__main__':
    vp_start_gui()
