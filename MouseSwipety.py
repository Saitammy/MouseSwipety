import tkinter as tk

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
    empty_window.destroy()

empty_window = tk.Tk()
empty_window.title('Testing for now') #New COmment
empty_window.geometry("750x750")

testing_label = tk.Label(empty_window, text = "I am simply testing for now.")
testing_label.pack()

quit_button = tk.Button(empty_window, text = "Quit", command = buttonClick, width = 20, height = 2)
quit_button.pack(side = tk.BOTTOM, pady = 10, padx = 10, anchor = "se")

centerWindow(empty_window) # Calling centerWindow function here to put it in the center
empty_window.mainloop()

