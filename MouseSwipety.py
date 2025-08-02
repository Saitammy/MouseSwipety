import tkinter as tk
from pynput.mouse import Controller
import threading
import time

mouse = Controller()
last_x = mouse.position[0]

def centerWindow(window):
    window.update_idletasks()
    
    width = window.winfo_width() 
    height = window.winfo_height() 
    
    screen_width = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight() 
    
    x = (screen_width - width) // 2 
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}") 
    
def buttonClick():
    global running
    running = False
    empty_window.destroy()
    
def track_mouse():
    final_pos = tk.Label(empty_window, text = "No mouse movement", font=("Arial", 35), fg = "blue")
    final_pos.place(relx = 0.5, rely = 0.5, anchor="center")
    global last_x, running
    while running:
        current_x = mouse.position[0]
        if current_x > last_x:
            final_pos.config(text="Moving Right", fg = "green")
        elif current_x < last_x:
            final_pos.config(text="Moving Left", fg = "red")
        else:
            final_pos.config(text="No mouse movement", fg = "blue")
        last_x = current_x
        time.sleep(0.01)

empty_window = tk.Tk()
empty_window.title('MouseSwipety') 
empty_window.geometry("750x750")

testing_label = tk.Label(empty_window, text = "Mouse Action", font = ("Arial", 70))
testing_label.place(relx=0.5, rely=0.35, anchor="center")

quit_button = tk.Button(empty_window, text = "Quit", command = buttonClick, width = 20, height = 2)
quit_button.pack(side = tk.BOTTOM, pady = 10, padx = 10, anchor = "se")

centerWindow(empty_window)

running = True
threading.Thread(target=track_mouse, daemon=True).start()

empty_window.mainloop()