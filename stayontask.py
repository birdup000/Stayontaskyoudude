import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk

task_running = False
dark_mode = False

def start_task():
    global task_running
    if task_running:
        task_button.config(bg="red")
    else:
        task_button.config(bg="white")
        task_running = True
        task_label.config(text="Working on task...")
        stop_button.config(state="normal")
        try:
            time = int(e1.get())
        except ValueError:
            messagebox.showerror("Stay on Task", "Please enter a valid number of minutes")
            return
        global alert_id
        alert_id = root.after(time*60*1000, alert) 

def stop_task():
    global task_running
    task_running = False
    task_label.config(text="Task stopped.")
    stop_button.config(bg="red", state="disabled")
    root.after(3000, change_color)
    root.after_cancel(alert_id)
    if 'top' in globals() and top:
        top.destroy()
        
def change_color():
    stop_button.config(bg="white")

def alert():
    global top
    top = tk.Toplevel(root)
    top.overrideredirect(True) 
    top.lift() 
    top.attributes("-topmost", True) 
    top.title("Stay on Task")
    label = tk.Label(top, text="Don't forget to stay on task! Close this window to close the bee picture.")
    label.config(font=("Courier", 12), anchor="center")
    label.pack(padx=10, pady=10)
    
    # Open the image file
    image = Image.open("bee.png")
    # Resize the image
    image.thumbnail((200, 200))
    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(image)
    # Create a label to display the image
    label = tk.Label(top, image=photo, width=200, height=200)
    label.pack()
    # Keep a reference to the image object
    label.image = photo
    top.protocol("WM_DELETE_WINDOW", stop_task)
    top.mainloop()

root = tk.Tk()
root.geometry("400x200") 
root.title("Stay on Task")
try:
    root.iconbitmap("cake.ico")
except TclError:
    pass

task_label = tk.Label(root, text="Task not started.")
task_label.pack()

task_button = tk.Button(root, text="Start Task", command=start_task)
task_button.pack()
stop_button = tk.Button(root, text="Stop Task", command=stop_task, state="disabled")
stop_button.pack()


global alert_id


minutes = tk.Label(root, text="Minutes")
minutes.pack()

# Create the Spinbox widget
e1 = tk.Spinbox(root, from_=0, to=60)
e1.pack()
e1.delete(0, "end")
e1.insert(0, 10)

# Define validate_start function
def validate_start(start_func):
    global e1
    if not task_running:
        start_func()
    return True

e1.config(validate="key")


seconds_label = tk.Label(root, text="Seconds:")
seconds_label.pack()
e2 = tk.Spinbox(root, from_=0, to=59, increment=1)
e2.pack()
e2.delete(0, "end")
e2.insert(0, 0)



def start_task():
    global task_running
    if task_running:
        task_button.config(bg="red")
    else:
        task_button.config(bg="white")
        task_running = True
        task_label.config(text="Working on task...")
        stop_button.config(state="normal")
        try:
            minutes = int(e1.get())
            seconds = int(e2.get())
        except ValueError:
            messagebox.showerror("Stay on Task", "Please enter a valid number of minutes and seconds")
            return
        time = minutes * 60 + seconds
        global alert_id
        alert_id = root.after(time*1000, alert)



#Dark mode button

def dark():
    global dark_mode
    if dark_mode:
        root.config(bg='white')
        dark_mode = False
    else:
        root.config(bg='black')
        dark_mode = True

dark_button = tk.Button(root, text="Dark Mode", command=dark)
dark_button.pack()
root.mainloop()
