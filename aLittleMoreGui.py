import tkinter as tk
import subprocess

class App(tk.Frame):
    def __init__(self,master):
        #create the master element
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Hello World!")
        self.master.resizable(False,False)
        self.master.tk_setPalette(background="#DAF7A6")
        x=(self.master.winfo_screenwidth()-
           self.master.winfo_reqwidth()/2)
        y=(self.master.winfo_screenheight()-
           self.master.winfo_reqheight()/2)
        self.master.geometry("+{}+{}".format(x,y))
        self.master.config(menu= tk.Menu(self.master))
        #create a frame inside called dialog_frame
        dialog_frame= tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)
        tk.Label(self, text="This is the base gui."
                            "(highfive)").pack()
        self.master.protocol('WM_DELETE_WINDOW', self.click_cancel)
        self.master.bind('<Return>', self.click_ok)
        self.master.bind('<Escape>', self.click_cancel)
        #create another frame called button_frame
        button_frame=tk.Frame(self)
        button_frame.pack(padx=15, pady=(0,15), anchor='e')
        tk.Button(self, text='OK', default='active',command=self.click_ok).pack(side='right')
        tk.Button(self, text='Cancel', command=self.click_cancel).pack(side='right')
#called if they click ok. operated by 'command=self.click_ok'
def click_ok(self):
    print("the user clicked 'OK'")

#called if they click cancel. operated by 'command=self.click_cancel'
def click_cancel(self):
    print("the user clicked 'Cancel'")
    self.master.destroy()




if __name__ == '__main__':
    #brings the frame to the top of the window stack. don't know
    #if this works on linux
    subprocess.call(['/usr/bin/osascript', '-e',
    'tell app "finder" to set frontmost of process "Python" to true'])

    #build the frame
    root = tk.Tk()
    app = App(root)
    app.mainloop()