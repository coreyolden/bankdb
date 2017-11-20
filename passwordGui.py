
import tkinter as tk

class App(tk.Frame):
    def __init_(self, master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Hello World!")

        tk.Label(self, text="This is the base gui."
                            "(highfive)").pack()
        tk.Message(self, text="Please enter username and password", justify='left',aspect=800).pack(pady=(15,0))
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor = 'w')
        tk.Label(dialog_frame, text='Username:').grid(row=0, column=0, sticky='w')
        self.user_input = tk.Entry(dialog_frame, background='white', width=24)
        self.user_input.grid(row=0, column=1, sticky='w')
        #when loaded this will be focused on
        self.user_input.focus_set()

        tk.Label(dialog_frame, text='Password:').grid(row=1, column=0, sticky='w')
        self.pass_input = tk.Entry(dialog_frame, background='white', width=24, show='*')
        self.pass_input.grid(row=1, column=1, sticky='w')


def click_ok(self, event=None):
    print("the user clicked 'OK':\nUsername: {}\nPassword: {}".format(self.user_input.get(),self.pass_input.get()))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()