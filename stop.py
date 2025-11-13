from tkinter import *
from time import strftime
from tkinter import messagebox
import time

tk = Tk()
tk.geometry("500x500")
tk.title("clock")
tk.config(background="blue")

hr = StringVar()
ms = StringVar()
ss = StringVar()

# --- Added global variable to control the stopwatch ---
running = False

def get_timer():
    global running
    running = True
    hour.config(state="readonly")
    second.config(state="readonly")
    minute.config(state="readonly")
    try:
        timer = int(hour.get()) * 60 * 60 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please enter valid values")
        messagebox.showerror("Error", "Please enter valid values")
        return
    
    while timer > -1 and running:
        m, s = divmod(timer, 60)
        h = 0
        if m > 60:
            h, m = divmod(m, 60)
        hr.set(h)
        ms.set(m)
        ss.set(s)
        tk.update()
        time.sleep(1)
        if not running:  # if stop button pressed, break loop
            break
        timer = timer - 1

def stop_timer():
    global running
    running = False

# --- Entry Boxes ---
hour = Entry(tk, border=5, relief="sunken", foreground="white", textvariable=hr, width=7)
hour.grid(row=1, column=1)
minute = Entry(tk, border=5, relief="sunken", foreground="white", textvariable=ms, width=7)
minute.grid(row=1, column=2)
second = Entry(tk, border=5, relief="sunken", foreground="white", textvariable=ss, width=7)
second.grid(row=1, column=3)

# --- Buttons (added labels + stop button) ---
Button(tk, text="Start", bg="red", command=get_timer).grid(row=2, column=2)
Button(tk, text="Stop", bg="yellow", command=stop_timer).grid(row=2, column=3)

tk.mainloop()
