import tkinter as tk
from pynput.mouse import Controller
import threading
import time

mouse = Controller()
last_x = mouse.position[0]

def centerWindow(window): # Function to center the GUI window to the center of my screen
    window.update_idletasks()
    
    width = window.winfo_width() # Take width of GUI
    height = window.winfo_height() # Take height of GUI
    
    screen_width = window.winfo_screenwidth() # Take screen width
    screen_height = window.winfo_screenheight() # Take screen height
    
    x = (screen_width - width) // 2 # Floor divison wrt to screen
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}") # Convert size accordingly
    
def buttonClick(): # Function to close the application
    global running
    running = False
    empty_window.destroy()
    
def track_mouse():
    global last_x, running
    while running:
        current_x = mouse.position[0]
        if current_x > last_x:
            print("Moving right")
        elif current_x < last_x:
            print("Moving left")
        last_x = current_x
        time.sleep(0.01)

empty_window = tk.Tk()
empty_window.title('Testing for now') 
empty_window.geometry("750x750")

testing_label = tk.Label(empty_window, text = "I am simply testing for now.")
testing_label.pack()

quit_button = tk.Button(empty_window, text = "Quit", command = buttonClick, width = 20, height = 2)
quit_button.pack(side = tk.BOTTOM, pady = 10, padx = 10, anchor = "se")

centerWindow(empty_window) # Calling centerWindow function here to put it in the center

running = True
threading.Thread(target=track_mouse, daemon=True).start()

empty_window.mainloop()