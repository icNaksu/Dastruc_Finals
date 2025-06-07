from datetime import datetime

attendance_data = {}
attendance_stack = [] 

#MGA FUNCTIONS
def record_time_in(student_name):
    now = datetime.now()
    time_in = now.strftime("%I:%M:%S %p")
    if student_name not in attendance_data:
        attendance_data[student_name] = {}
    attendance_data[student_name]['time_in'] = time_in
    
     # TULAK SA STACK
    attendance_stack.append((student_name, 'time_in', time_in))
    
    return time_in

def record_time_out(student_name):
    now = datetime.now()
    time_out = now.strftime("%I:%M:%S %p")
    if student_name not in attendance_data:
        attendance_data[student_name] = {}
    attendance_data[student_name]['time_out'] = time_out

    # TULAK SA STACK
    attendance_stack.append((student_name, 'time_out', time_out))
    
    return time_out

def calculate_status(student_name, scheduled_time_in="06:05:00 PM"):
    fmt = "%I:%M:%S %p"
    if student_name not in attendance_data or 'time_in' not in attendance_data[student_name]:
        return "Absent"

    time_in = datetime.strptime(attendance_data[student_name]['time_in'], fmt)
    scheduled = datetime.strptime(scheduled_time_in, fmt)

    if time_in <= scheduled:
        return "On time"
    else:
        return "Late"

def pop_last_action():
    if attendance_stack:
        student_name, action_type, _ = attendance_stack.pop()
        if action_type in attendance_data.get(student_name, {}):
            del attendance_data[student_name][action_type]
        return f"Undid {action_type} for {student_name}"
    return "No actions to undo."

def view_stack():
    return attendance_stack[::-1]  
