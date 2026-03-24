from tkinter import *
import pandas as pd
mainwindow=Tk()
mainwindow.title("friends")
mainwindow.geometry("330x220")
def new():
    BirthMonth=entry2.get()
    user_input=entry1.get()
    subwindow=Toplevel(mainwindow)
    label11=Label(subwindow,text=user_input,font="Arial")
    label11.grid(row=3,column=3)
    label12=Label(subwindow,text="Hello Welcome to friends group")
    label12.grid(row=4,column=3)
    Ndat=user_input.split(",")
    Bdat=BirthMonth.split(",")
    indexlist=[f"friend {i}" for i in range(1,len(Bdat)+1)]
    if len(Ndat)==len(Bdat):
        try:
            data={"name":Ndat,"birthmonth":Bdat}
            df=pd.DataFrame(data,index=indexlist)
            df.to_excel("friends_list.xlsx",sheet_name="My friends")
            label4=Label(subwindow,text="data stored")
            label4.grid(row=5,column=3)
        except Exception as e:
            Label(subwindow, text="Error: Count mismatch!", fg="red").pack(pady=10)
    else:
        label3=Label(subwindow,text="data not stored")
        label3.grid(row=5,column=3)
    def close_swindow():
        subwindow.destroy()
    button13=Button(subwindow,text="END",command=close_swindow)
    button13.grid(row=4,column=4)
label=Label(mainwindow,text="Name:")
label.grid(row=2, column=2)
entry1=Entry()
entry1.grid(row=2,column=3)

entry2=Entry()
entry2.grid(row=3,column=3)
label2=Label(mainwindow,text="BirthMonth:")
label2.grid(row=3, column=2)

button=Button(mainwindow,text="submit",command=new)
button.grid(row=10,column=10)
def close_window():
    mainwindow.destroy()
button1=Button(mainwindow,text="END",command=close_window)
button1.grid(row=12,column=12)
mainwindow.mainloop()
