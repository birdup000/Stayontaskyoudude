import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def start_task():
    task_label.config(text="Working on task...")
    task_button.config(state="disabled")
    stop_button.config(state="normal")
    try:
        time = int(e1.get())
    except ValueError:
        messagebox.showerror("Stay on Task", "Please enter a valid number of minutes")
        return
    global alert_id
    alert_id = root.after(time*60*1000, alert) 

def stop_task():
    task_label.config(text="Task stopped.")
    task_button.config(state="normal")
    stop_button.config(state="disabled")
    root.after_cancel(alert_id)
    try:
        top.destroy()
    except NameError:
        pass

def alert():
    global top
    top = tk.Toplevel(root)
    top.geometry("300x150+500+200") 
    top.overrideredirect(True) 
    top.lift() 
    top.attributes("-topmost", True) 
    top.title("Stay on Task")
    label = tk.Label(top, text="Don't forget to stay on task! Close this window to close the bee picture.")
    label.pack(padx=10, pady=10)
    label.config(font=("Courier", 18), anchor="center")
    # Open the image file
    image = Image.open("bee.png")
    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(image)
    # Create a label to display the image
    label = tk.Label(top, image=photo)
    label.pack()
    # Keep a reference to the image object
    label.image = photo

root = tk.Tk()
root.geometry("400x200") 
root.title("Stay on Task")
try:
    root.iconbitmap("cake.ico")
except TclError:
    pass

task_label = tk.Label(root, text="Task not started.")
task_label.pack()

e1 = tk.Entry(root)
e1.pack()
e1.insert(0,"10")

minutes = tk.Label(root, text="Minutes")
minutes.pack()

task_button = tk.Button(root, text="Start Task", command=start_task)
task_button.pack()
stop_button = tk.Button(root, text="Stop Task", command=stop_task, state="disabled")
stop_button.pack()

root.mainloop()