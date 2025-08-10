import tkinter as tk
from pynput.mouse import Controller
import threading
import time
import centerwindow

# Function to close the application when Quit button is pressed
def buttonClick(): 
    global running
    running = False
    empty_window.destroy()

# The controller function reads the mouse's current pointer position
mouse = Controller()
last_x = mouse.position[0]
last_y = mouse.position[1]
last_coor = (mouse.position[0], mouse.position[1])
    
def trackMouse():
    final_hor = tk.Label(empty_window, text = "No mouse movement", font = ("Arial", 35), fg = "blue")
    final_hor.place(relx = 0.5, rely = 0.4, anchor = "center")
    final_ver = tk.Label(empty_window, text = "No Vertical Movement", font = ("Arial", 35), fg = "blue")
    final_ver.place(relx = 0.5, rely = 0.5, anchor = "center")
    coor_display = tk.Label(empty_window, text = f"X - {mouse.position[0]}, Y - {mouse.position[1]}", font = ("Arial", 35), fg = "black")
    coor_display.place(relx = 0.5, rely = 0.6, anchor = "center")
    global last_x, last_y, running, last_coor
    
    while running:
        # Tracking X Coordinates
        current_x = mouse.position[0]
        if current_x > last_x:
            final_hor.config(text="Moving Right", fg = "green")
        elif current_x < last_x:
            final_hor.config(text="Moving Left", fg = "red")
        else:
            final_hor.config(text="No mouse movement", fg = "blue")
        last_x = current_x
        
        # Tracking Y coordinates
        current_y = mouse.position[1]
        if current_y < last_y:
            final_ver.config(text="Moving Up", fg="green")
        elif current_y > last_y:
            final_ver.config(text="Moving Down", fg="red")
        else:
            final_ver.config(text="No mouse movement", fg="blue")
        last_y = current_y
        
        # Tracking Coordinates
        coor_display.config(text=f"X - {mouse.position[0]}, Y - {mouse.position[1]}")

        
        time.sleep(0.01)
            

empty_window = tk.Tk()
empty_window.title('MouseSwipety') 
empty_window.geometry("750x750")

testing_label = tk.Label(empty_window, text = "Mouse Action", font = ("Arial", 70))
testing_label.place(relx=0.5, rely=0.2, anchor="center")

quit_button = tk.Button(empty_window, text = "Quit", command = buttonClick, width = 20, height = 2)
quit_button.pack(side = tk.BOTTOM, pady = 10, padx = 10, anchor = "se")

centerwindow.centerWindow(empty_window)

running = True
threading.Thread(target=trackMouse, daemon=True).start()

empty_window.mainloop()