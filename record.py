import tkinter as tk
from tkinter import ttk
from datetime import datetime

car = tk.Tk()
car.title("Class Attendance Record")
car.configure(bg="#FFFFFF")
car.geometry("1340x770")

#GRID LAYOUT PANG RESPONSIVE
for i in range(4):
    car.grid_columnconfigure(i, weight=1)
for i in range(20):
    car.grid_rowconfigure(i, weight=1)

#LABELS
tk.Label(car, text="Professor : Jeremiah P. Delos Santos", font=('Arial', 18), bg="#FFFFFF").grid(row=0, column=0, sticky='w', padx=20, pady=10)
tk.Label(car, text="Subject : DASTRUC", font=('Arial', 18), bg="#FFFFFF").grid(row=1, column=0, sticky='w', padx=20, pady=10)
tk.Label(car, text="Schedule :", font=('Arial', 18), bg="#FFFFFF").grid(row=2, column=0, sticky='w', padx=20, pady=10)

#COMBOBOX LAYOUT
style = ttk.Style()
style.theme_use("default")
style.map("TCombobox",
          fieldbackground=[('readonly', '#FFFFFF')],
          background=[('readonly', '#FFFFFF')],
          foreground=[('readonly', 'black')],
          selectbackground=[('readonly', '#FFFFFF')],
          selectforeground=[('readonly', 'black')])

#COMBOBOX VALUES
combo = ttk.Combobox(
    car,
    state="readonly",
    values=["Tuesday | 3:00 PM - 5:00 PM", "Friday | 3:00 PM - 5:00 PM"],
    font=("Arial", 15),
    width=24
)
combo.set("Choose a schedule")
combo.grid(row=2, column=0, sticky='w', padx=150)

def update_datetime():
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")       # e.g., June 5, 2025
    time_str = now.strftime("%I:%M:%S %p")     # e.g., 03:45:22 PM
    datetime_label.config(text=f"{date_str}   |   {time_str}")
    car.after(1000, update_datetime)  # Update every 1000ms (1 second)
    
datetime_label = tk.Label(car, font=('Arial', 18), bg="white", fg="black")
datetime_label.grid(row=0, column=1, columnspan=2, sticky='e', padx=20, pady=10)

#LEGENDS
legend_frame = tk.Frame(car, bg="#FFFFFF")
legend_frame.grid(row=0, column=3, rowspan=4, sticky='ne', padx=30, pady=30)

tk.Label(legend_frame, text="Legends :", font=('Arial', 18), bg="#FFFFFF").pack(anchor='w')

legend_items = [("On time", "lime"), ("Late", "yellow"), ("Absent", "red")]
for text, color in legend_items:
    row = tk.Frame(legend_frame, bg="#FFFFFF")
    row.pack(anchor='w', pady=2)
    canvas = tk.Canvas(row, width=20, height=20, bg="#FFFFFF", highlightthickness=0)
    canvas.create_oval(2, 2, 18, 18, fill=color)
    canvas.pack(side='left')
    tk.Label(row, text=text, font=('Arial', 14), bg="#FFFFFF").pack(side='left', padx=5)

#HEADER
header_font = ('Arial', 16, 'bold')
tk.Label(car, text="Name", font=header_font, bg="#FFFFFF").grid(row=4, column=0, sticky='w', padx=50)
tk.Label(car, text="Time in", font=header_font, bg="#FFFFFF").grid(row=4, column=1, sticky='w', padx=50)
tk.Label(car, text="Time out", font=header_font, bg="#FFFFFF").grid(row=4, column=2, sticky='w', padx=50)
tk.Label(car, text="Status", font=header_font, bg="#FFFFFF").grid(row=4, column=3, sticky='w', padx=50)

#NAMES
tk.Label(car, text = "Abellera, Roinier", bg="#FFFFFF").grid(row=5, column=0, sticky='w', padx=50)




    
update_datetime()  # Start the loop
car.mainloop()
