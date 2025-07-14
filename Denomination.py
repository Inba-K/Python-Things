from tkinter import *
window=Tk()

window.title("Denomination Calculator")
window.geometry("1000x600")

Label(text="How much money?",fg="black",bg="white",height=2,width=15).pack()

e=Entry(fg="black",bg="white",width=10)
e.pack()

result_label = Label(window, text="", justify='left', font=("Courier", 12))
result_label.pack(pady=10)

def den():
    try:
        amount=int(e.get())
        r=""
        a=[100,10,5,1]
        for z in a:
            c=amount//z
            if c:
                r+=f"{z} x {c} = {z*c}\n"
                amount=amount%z
        result_label.config(text=r)
    except:
        result_label.config(text="Enter a valid amount.")

Button(text="Press for denomination",fg="black",bg="red",width=20,height=2,bd=3,command=den).pack()

window.mainloop()
