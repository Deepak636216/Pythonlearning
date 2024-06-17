from tkinter import *
window = Tk()
window.title("Calculator")
window.config(padx=20,pady=20)
# window.minsize(500 , 500)

# my_label1 = Label(text="Name", font=("arail,", 15, "bold"))
# my_label1.pack()
#
# my_label1["text"]="name"
# my_label1.config(text="name")
#
# input=Entry()
# input.pack()
#
#
# def change_label():
#     value = input.get()
#     my_label1.config(text=value)
#
# button=Button(text="click me",command=change_label)
# button.pack()
#
defi=Label(text="is equal to",font=("arial",15,"bold"))
defi.grid(column=0,row=1)

miles=Entry()
miles.grid(column=1,row=0)

lm=Label(text="miles",font=("arial",15,"bold"))
lm.grid(column=2,row=0)

km=Label(text="0")
km.grid(column=1,row=1)

lk=Label(text="Km's",font=("arial",15,"bold"))
lk.grid(column=2,row=1)

def calculator():
    value=miles.get()
    result=int(value)*1.609
    km.config(text=result)

button=Button(text="calculate",command=calculator)
button.grid(columns=2,row=2)




window.mainloop()