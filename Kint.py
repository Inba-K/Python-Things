from tkinter import *
window=Tk()
window.title("Example")
window.geometry("1000x600")
def button():
    print("Button pressed.")
Label(text="Welcome to the window.",fg="black",bg="white",width=30,height=5).pack()
Button(text="Press",fg="black",bg="red",width=10,height=5,bd=3,command=print(button())).pack()
Entry(fg="black",bg="white",width=25).pack()
Text(window,fg="black",bg="white",bd=3,height=10,width=50).pack()
window.mainloop()
