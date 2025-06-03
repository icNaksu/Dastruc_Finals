#new

import tkinter as tk

root = tk.Tk()

root.geometry("1920x1080")
root.title("Class Attendance Record")

label = tk.Label(root, text="hhhhh", font = ('Arial', 18)) 

textbox = tk.Text(root, height=3)
textbox.pack(padx=10)


root.mainloop()
