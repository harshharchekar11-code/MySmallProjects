from tkinter import *
def create_window2():
            global window2
            window2=Toplevel(window)
            window2.title("second window")
            window2.geometry("200x200")
            button1=Button(window2,text='close',command=window2.destroy)
            button1.pack()
            button2=Button(window2,text='something',command=labelling)
            button2.pack()
            
            
            
def labelling():
      label2=Label(window2,font=('Arial',20,'bold'),text="welcome to secret base")
      greeting=f"hello {name}"
      label3=Label(window2,font=('Arial',20,'bold'),text=greeting)
      label2.pack()
      label3.pack()
      


window=Tk()
username=Entry()
username.config(bg='light blue',fg='dark blue',font=('Arial',20,'bold'))
username.pack()
password=Entry()
password.config(bg='light blue',fg='dark blue',font=('Arial',20,'bold'),show='*')
password.pack()
def submit():
    global name
    name=username.get()
    syskey=password.get()
    if syskey =='smeet':
        create_window2()
    else:
        label=Label(window,text="wrong password!!!!")
        label.config(font=('monospace',50,'bold'))
        label.pack()
submit_button=Button(window,text='submit',command=submit)
submit_button.pack(side=RIGHT)
close_button=Button(window,text='close',font=('Ink free',12,'bold'),relief=RIDGE,command=window.destroy)
close_button.pack()

window.mainloop()    