import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
import csv
from tkinter import messagebox

attendance_data = {}
time_in_stack = []
time_out_stack = []

#NAMES
student_names = [
    "Abobo, Sunlyn T.", "Aguilar, Frances Heart B.", "Almazan, Neil Daniel G.",
    "Azul, Salvador lll L.", "Balaguer, Bryan Paulo G.", "Balde, Bryan Joshua Y.",
    "Baloyo, Princess Jade D.", "Baltazar, Jeremy J.", "Bolanos, Raneelhei M.",
    "Buizon, Nico Charlie C.", "Cabonce, Lawrence Carlylle A.", "Datanagan, Marc Janz O.",
    "De Jesus, Sandra Sophia", "Dela Vega, Eilsel C.", "De Leon, Seth Manuel M.",
    "Dequilla, Ruth Caye C.", "Galeno, Eddrian Y.", "Lachica, Andrea Beatrice C.",
    "Madrid, Maiko C.", "Mendoza, Kym Raimier M.", "Misolas, Ezekiel Manuel V.",
    "Nambio, Markie L.", "Norva, Chamique Ann R.", "Oliveros, Justine Lawrence A.",
    "Orde, Jione Rico M.", "Pamintuan, Alliah", "Racuya, Earlkin M.",
    "Regalia, Kent Romar A.", "Salalac, Fergo Emson A.", "Sambrano, Franz B.",
    "Suarez, Deirdrei D.", "Trocio, Julian S.", "Ullegue, Cholo Ley N.",
    "Villanueva, Sebastian F.", "Valeroso, Alexa Dylan O.", "Valle, Donn Rafael T.",
    "Yecla, Christian Rhanell G.", "Ylagan, Rachelle Elizabeth P.", "Zapirain, Jazley Mae E."
]

#EXPORT TO CSV FILE(EXCEL)
def export_to_csv():
    today_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"attendance_{today_str}.csv"

    # TIME IN TABLE
    students_with_time_in = []
    for student in student_names:
        times_in = attendance_data.get(student, {}).get("time_in", [])
        for time_in in times_in:
            students_with_time_in.append((student, time_in))

    #SORTED BY ASCENDING ORDER FIRST COMERS GO TO THE BOTTOM OF THE CSV
    students_with_time_in.sort(key=lambda x: datetime.strptime(x[1], "%I:%M:%S %p"), reverse=True)

    # TIME OUT TABLE
    students_with_time_out = []
    for student in student_names:
        times_out = attendance_data.get(student, {}).get("time_out", [])
        for time_out in times_out:
            students_with_time_out.append((student, time_out))

    #SAME AS TIME IN 
    students_with_time_out.sort(key=lambda x: datetime.strptime(x[1], "%I:%M:%S %p"), reverse=True)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # TIME IN TABLE
        writer.writerow(["Time In Records"])
        writer.writerow(["Name", "Time In", "Status"])
        for student, time_in in students_with_time_in:
            status = calculate_status_for_time_in(time_in)
            writer.writerow([student, time_in, status])

        writer.writerow([])
        writer.writerow([])

        # TIME OUT TABLE
        writer.writerow(["Time Out Records"])
        writer.writerow(["Name", "Time Out"])
        for student, time_out in students_with_time_out:
            writer.writerow([student, time_out])

def record_time_in(student_name):
    now = datetime.now()
    time_in = now.strftime("%I:%M:%S %p")
    if student_name not in attendance_data:
        attendance_data[student_name] = {"time_in": [], "time_out": []}
    attendance_data[student_name]["time_in"].append(time_in)
    time_in_stack.append((student_name, time_in))
    return time_in

def record_time_out(student_name):
    now = datetime.now()
    time_out = now.strftime("%I:%M:%S %p")
    if student_name not in attendance_data:
        attendance_data[student_name] = {"time_in": [], "time_out": []}
    attendance_data[student_name]["time_out"].append(time_out)
    time_out_stack.append((student_name, time_out))
    return time_out

def calculate_status_for_time_in(time_in, scheduled_time_in="03:00:00 PM"):
    if not time_in:
        return "Absent"
    fmt = "%I:%M:%S %p"
    time_in_dt = datetime.strptime(time_in, fmt)
    scheduled_dt = datetime.strptime(scheduled_time_in, fmt)
    return "On time" if time_in_dt <= scheduled_dt else "Late"

def undo_time_in():
    student_name = selected_student.get()
    if 'time_in' in attendance_data.get(student_name, {}) and attendance_data[student_name]['time_in']:
        removed = attendance_data[student_name]['time_in'].pop()

def undo_time_out():
    student_name = selected_student.get()
    if 'time_out' in attendance_data.get(student_name, {}) and attendance_data[student_name]['time_out']:
        removed = attendance_data[student_name]['time_out'].pop()

# GUI setup
car = tk.Tk()
car.title("Class Attendance Record")
car.geometry("1920x1080")
car.minsize(1280, 720)

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

# LABELS
create_text(40, 20, "Professor : Jeremiah P. Delos Santos", font=('Arial', 22, 'bold'))
create_text(40, 80, "Subject : DASTRUC", font=('Arial', 22, 'bold'))

datetime_text = canvas.create_text(1880, 20, text="", font=('Arial', 20), fill="black", anchor='ne')

# HEADER
header_font = ('Arial', 20, 'bold')
create_text(100, 200, "Name", font=header_font)
create_text(600, 200, "Time in", font=header_font)
create_text(1000, 200, "Time out", font=header_font)
create_text(1400, 200, "Status", font=header_font)

# DROPDOWN
selected_student = tk.StringVar()
selected_student.set(student_names[0])
dropdown = ttk.Combobox(car, textvariable=selected_student, values=student_names, font=('Arial', 14), width=30, state="readonly")
dropdown.place(x=80, y=280)

# DISPLAY TEXT INFO
time_in_text_id = canvas.create_text(600, 260, text="", font=('Arial', 18), anchor='nw', fill='black')
time_out_text_id = canvas.create_text(1000, 260, text="", font=('Arial', 18), anchor='nw', fill='black')
status_text_id = canvas.create_text(1400, 260, text="", font=('Arial', 18), anchor='nw', fill='black')

# BUTTON FUNCTIONS
def handle_time_in():
    student_name = selected_student.get()
    time_in = record_time_in(student_name)
    canvas.itemconfig(time_in_text_id, text=time_in)
    canvas.itemconfig(status_text_id, text=calculate_status_for_time_in(time_in))
    export_to_csv()

def handle_time_out():
    student_name = selected_student.get()
    times_in = attendance_data.get(student_name, {}).get("time_in", [])
    
    if not times_in:
        # Student has not timed in yet
        tk.messagebox.showwarning("Warning", f"{student_name} has not timed in yet!")
        return
    
    time_out = record_time_out(student_name)
    canvas.itemconfig(time_out_text_id, text=time_out)
    export_to_csv()

def handle_undo_time_in():
    undo_time_in()
    update_student_display()
    export_to_csv()

def handle_undo_time_out():
    undo_time_out()
    update_student_display()
    export_to_csv()

def update_student_display(*args):
    student_name = selected_student.get()
    times_in = attendance_data.get(student_name, {}).get('time_in', [])
    times_out = attendance_data.get(student_name, {}).get('time_out', [])
    last_time_in = times_in[-1] if times_in else ''
    last_time_out = times_out[-1] if times_out else ''
    status = calculate_status_for_time_in(last_time_in)
    canvas.itemconfig(time_in_text_id, text=last_time_in)
    canvas.itemconfig(time_out_text_id, text=last_time_out)
    canvas.itemconfig(status_text_id, text=status)

def make_button(text, x, y, color, command):
    btn = tk.Button(car, text=text, command=command, font=('Arial', 14), bg=color, fg="white")
    btn.place(x=x, y=y, width=160, height=50)
    return btn

# BUTTONS
make_button("Time In", 587, 340, "#4CAF50", handle_time_in)
make_button("Time Out", 997, 340, "#FF9800", handle_time_out)
make_button("Undo Time In", 587, 440, "#FF0000", handle_undo_time_in)
make_button("Undo Time Out", 997, 440, "#D32F2F", handle_undo_time_out)

dropdown.bind("<<ComboboxSelected>>", update_student_display)

def update_datetime():
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")
    time_str = now.strftime("%I:%M:%S %p")
    canvas.itemconfig(datetime_text, text=f"{date_str}   |   {time_str}")
    car.after(1000, update_datetime)

update_student_display()
update_datetime()
car.mainloop()
