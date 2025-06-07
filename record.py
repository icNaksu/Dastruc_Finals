import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk

attendance_data = {}
attendance_stack = []

#FUNCTIONS
def record_time_in(student_name):
    now = datetime.now()
    time_in = now.strftime("%I:%M:%S %p")

    if student_name not in attendance_data:
        attendance_data[student_name] = {}

    if 'time_in' not in attendance_data[student_name]:
        attendance_data[student_name]['time_in'] = time_in
        attendance_stack.append((student_name, 'time_in', time_in))
        return time_in
    return attendance_data[student_name]['time_in']

def record_time_out(student_name):
    now = datetime.now()
    time_out = now.strftime("%I:%M:%S %p")

    if student_name not in attendance_data:
        attendance_data[student_name] = {}

    if 'time_out' not in attendance_data[student_name]:
        attendance_data[student_name]['time_out'] = time_out
        attendance_stack.append((student_name, 'time_out', time_out))
        return time_out
    return attendance_data[student_name]['time_out']

def calculate_status(student_name, scheduled_time_in="03:00:00 PM"):
    fmt = "%I:%M:%S %p"
    if student_name not in attendance_data or 'time_in' not in attendance_data[student_name]:
        return "Absent"
    time_in = datetime.strptime(attendance_data[student_name]['time_in'], fmt)
    scheduled = datetime.strptime(scheduled_time_in, fmt)
    return "On time" if time_in <= scheduled else "Late"

def pop_last_action():
    if attendance_stack:
        student_name, action_type, _ = attendance_stack.pop()
        if action_type in attendance_data.get(student_name, {}):
            del attendance_data[student_name][action_type]
        return f"Undid {action_type} for {student_name}"
    return "No actions to undo."

#GUI
car = tk.Tk()
car.title("Class Attendance Record")
car.geometry("1920x1080")
car.minsize(1280, 720)

#BACKGROUND
try:
    original_bg = Image.open("bg/image.png")
except FileNotFoundError:
    print("Background image not found! Make sure 'bg/image.png' exists.")
    exit()

canvas = tk.Canvas(car, highlightthickness=0)
canvas.pack(fill="both", expand=True)

init_width, init_height = 1920, 1080
resized_init = original_bg.resize((init_width, init_height))
bg_photo = ImageTk.PhotoImage(resized_init)
bg_image = canvas.create_image(0, 0, anchor='nw', image=bg_photo)
canvas.bg_image = bg_photo

def resize_bg(event):
    if event.width < 100 or event.height < 100:
        return
    resized = original_bg.resize((event.width, event.height))
    new_bg = ImageTk.PhotoImage(resized)
    canvas.itemconfig(bg_image, image=new_bg)
    canvas.bg_image = new_bg

car.bind("<Configure>", resize_bg)

def create_text(x, y, text, font=('Arial', 18), fill='black', anchor='nw'):
    return canvas.create_text(x, y, text=text, font=font, fill=fill, anchor=anchor)

#LABELS
create_text(40, 20, "Professor : Jeremiah P. Delos Santos", font=('Arial', 22, 'bold'))
create_text(40, 80, "Subject : DASTRUC", font=('Arial', 22, 'bold'))

datetime_text = canvas.create_text(1880, 20, text="", font=('Arial', 20), fill="black", anchor='ne')

#HEADER
header_font = ('Arial', 20, 'bold')
create_text(100, 200, "Name", font=header_font)
create_text(600, 200, "Time in", font=header_font)
create_text(1000, 200, "Time out", font=header_font)
create_text(1400, 200, "Status", font=header_font)

#STUDENTS
student_name = "Abellera, Roinier"
create_text(100, 260, student_name, font=('Arial', 18))

time_in_text_id = canvas.create_text(600, 260, text="", font=('Arial', 18), anchor='nw', fill='black')
time_out_text_id = canvas.create_text(1000, 260, text="", font=('Arial', 18), anchor='nw', fill='black')
status_text_id = canvas.create_text(1400, 260, text="", font=('Arial', 18), anchor='nw', fill='black')

#BUTTONS
def make_button(text, x, y, color, command):
    btn = tk.Button(car, text=text, command=command, font=('Arial', 14), bg=color, fg="white")
    btn.place(x=x, y=y, width=160, height=50)
    return btn

btn_time_in = make_button("Time In", 600, 340, "#4CAF50", lambda: handle_time_in())
btn_time_out = make_button("Time Out", 800, 340, "#FF9800", lambda: handle_time_out())
btn_undo = make_button("Undo", 1000, 340, "#FF0000", lambda: handle_undo())

undo_label_id = canvas.create_text(600, 410, text="", font=('Arial', 14), fill='red', anchor='nw')

#BUTTON FUNCTIONS
def handle_time_in():
    time_in = record_time_in(student_name)
    canvas.itemconfig(time_in_text_id, text=time_in)
    status = calculate_status(student_name)
    canvas.itemconfig(status_text_id, text=status)

def handle_time_out():
    time_out = record_time_out(student_name)
    canvas.itemconfig(time_out_text_id, text=time_out)

def handle_undo():
    msg = pop_last_action()
    canvas.itemconfig(time_in_text_id, text=attendance_data.get(student_name, {}).get('time_in', ''))
    canvas.itemconfig(time_out_text_id, text=attendance_data.get(student_name, {}).get('time_out', ''))
    status = calculate_status(student_name)
    canvas.itemconfig(status_text_id, text=status)

#REALTIME CLOCK
def update_datetime():
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    time_str = now.strftime("%I:%M:%S %p")
    canvas.itemconfig(datetime_text, text=f"{date_str}   |   {time_str}")
    car.after(1000, update_datetime)

update_datetime()
car.mainloop()
