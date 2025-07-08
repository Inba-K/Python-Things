import tkinter as tk

window = tk.Tk()
window.title("GIF Display")

gif_image = tk.PhotoImage(file="Baby Yoda.gif")

gif_label = tk.Label(window, image=gif_image)
gif_label.pack()

window.mainloop()
