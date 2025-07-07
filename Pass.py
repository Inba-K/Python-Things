from tkinter import *
import random
import string

window=Tk()
window.title("Password Generator")
window.geometry("1000x600")

def button(length):
    a=string.ascii_letters+string.digits+string.punctuation
    rs=''.join(random.choice(a) for _ in range(length))
    Label(text=rs,fg="black",bg="white",width=20,height=5).pack()
Label(text="Here is your newly generated password.",fg="black",bg="white",height=5,width=50).pack()
print(button(12))

window.mainloop()
