import tkinter as tk
from tkinter import ttk

car = tk.Tk()
car.title("Class Attendance Record")
car.configure(bg="#769AC7")
car.geometry("1340x770")

#GRID LAYOUT PANG RESPONSIVE
for i in range(4):
    car.grid_columnconfigure(i, weight=1)
for i in range(20):
    car.grid_rowconfigure(i, weight=1)

#COMBOBOX LAYOUT
style = ttk.Style()
style.theme_use("default")
style.map("TCombobox",
          fieldbackground=[('readonly', '#769AC7')],
          background=[('readonly', '#769AC7')],
          foreground=[('readonly', 'black')],
          selectbackground=[('readonly', '#769AC7')],
          selectforeground=[('readonly', 'black')])

#LABELS
tk.Label(car, text="Professor : Jeremiah P. Delos Santos", font=('Arial', 18), bg="#769AC7").grid(row=0, column=0, sticky='w', padx=20, pady=10)

tk.Label(car, text="Subject : DASTRUC", font=('Arial', 18), bg="#769AC7").grid(row=1, column=0, sticky='w', padx=20, pady=10)

tk.Label(car, text="Schedule :", font=('Arial', 18), bg="#769AC7").grid(row=2, column=0, sticky='w', padx=20, pady=10)

#COMBOBOX VALUES
combo = ttk.Combobox(
    car,
    state="readonly",
    values=["Tuesday: 3:00 PM - 5:00 PM", "Friday: 3:00 PM - 5:00 PM"],
    font=("Arial", 15)
)
combo.set("Choose a schedule")
combo.grid(row=2, column=0, sticky='w', padx=150)

#HEADER
header_font = ('Arial', 16, 'bold')
tk.Label(car, text="Name", font=header_font, bg="#769AC7").grid(row=4, column=0, sticky='w', padx=50)
tk.Label(car, text="Time in", font=header_font, bg="#769AC7").grid(row=4, column=1, sticky='w', padx=50)
tk.Label(car, text="Time out", font=header_font, bg="#769AC7").grid(row=4, column=2, sticky='w', padx=50)
tk.Label(car, text="Status", font=header_font, bg="#769AC7").grid(row=4, column=3, sticky='w', padx=50)

#LEGENDS
legend_frame = tk.Frame(car, bg="#769AC7")
legend_frame.grid(row=0, column=3, rowspan=4, sticky='ne', padx=30, pady=30)

tk.Label(legend_frame, text="Legends :", font=('Arial', 18), bg="#769AC7").pack(anchor='w')

legend_items = [("On time", "lime"), ("Late", "yellow"), ("Absent", "red")]
for text, color in legend_items:
    row = tk.Frame(legend_frame, bg="#769AC7")
    row.pack(anchor='w', pady=2)
    canvas = tk.Canvas(row, width=20, height=20, bg="#769AC7", highlightthickness=0)
    canvas.create_oval(2, 2, 18, 18, fill=color)
    canvas.pack(side='left')
    tk.Label(row, text=text, font=('Arial', 14), bg="#769AC7").pack(side='left', padx=5)

car.mainloop()
