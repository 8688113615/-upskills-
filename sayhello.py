from tkinter import*
mw=Tk()
mw.title("tic tak")
def sayhellow():
    name=user.get()
    greet="hellow"+name+"!"
    if name!="":
      text.config(text=greet)
      user.delete(0,END)
user=Entry(mw,width=20,font=("Arial",18))
user.pack(padx=10,pady=10)
text=Label(mw,text="Enter your name",font=("Arial",18))
text.pack()
btn=Button(mw,text="say hellow",font=("Arial",20),command=sayhellow)
btn.pack(pady=5)
mw.mainloop()