import tkinter as tk
from tkinter import ttk

car = tk.Tk()
car.geometry("1340x770")
car.title("Class Attendance Record")
car.configure(bg="#769AC7")  

tk.Label(car, text="Professor :", font=('Arial', 18), bg="#769AC7").place(x=30, y=30)
tk.Label(car, text="Jeremiah P. Delos Santos", font=('Arial', 18), bg="#769AC7").place(x=150, y=30)

tk.Label(car, text="Subject :", font=('Arial', 18), bg="#769AC7").place(x=30, y=70)
tk.Label(car, text="DASTRUC", font=('Arial', 18), bg="#769AC7").place(x=150, y=70)

tk.Label(car, text="Schedule :", font=('Arial', 18), bg="#769AC7").place(x=30, y=110)

large_font = ("Arial", 15)
combo = ttk.Combobox(car, values=["Tuesday | 3:00 PM - 5:00 PM", "Friday | 3:00 PM - 5:00 PM"],
                     width=30, font=large_font)
combo.set("Choose a schedule")
combo.place(x=150, y=110)

headers = ["Name", "Time in", "Time out", "Status"]
positions = [80, 300, 520, 740]

for idx, text in enumerate(headers):
    tk.Label(car, text=text, font=('Arial', 16, 'bold'), bg="#769AC7").place(x=positions[idx], y=180)

for i in range(10):
    y = 220 + i * 40
    tk.Label(car, text=f"{i + 1}.", font=('Arial', 14), bg="#769AC7").place(x=50, y=y)

tk.Label(car, text="Legends :", font=('Arial', 18), bg="#769AC7").place(x=1100, y=30)

legend_items = [("On time", "lime"), ("Late", "yellow"), ("Absent", "red")]
for i, (text, color) in enumerate(legend_items):
    y = 70 + i * 30
    canvas = tk.Canvas(car, width=20, height=20, bg="#769AC7", highlightthickness=0)
    canvas.place(x=1100, y=y)
    canvas.create_oval(2, 2, 18, 18, fill=color)
    tk.Label(car, text=text, font=('Arial', 14), bg="#769AC7").place(x=1130, y=y)

car.mainloop()
