import tkinter as tk



window = tk.Tk()


tracing = False

def toggle_trace():
    global tracing

    if tracing == False:
        tracing = True
        title_label.config(text="Tracing...")
        trace_button.config(text="Stop Trace")
        result_label.config(text="")
    else:
        tracing = False
        title_label.config(text="Tracing Stopped")
        trace_button.config(text="Trace")
        result_label.config(text="Result")


# Create window

window.title("Time Ledger")
window.geometry("600x400")
window.config(bg="black")

# Create frame
frame = tk.Frame(window, bg="black")
frame.pack(pady=50)

# Title
title_label = tk.Label(
    frame,
    text="Start Tracing",
    font=("Arial", 25),
    bg="black",
    fg="white"
)
title_label.pack(pady=10)

# Button
trace_button = tk.Button(
    frame,
    text="Trace",
    font=("Arial", 15),
    command=toggle_trace
)
trace_button.pack(pady=10)

# Result
result_label = tk.Label(
    frame,
    text="",
    font=("Arial", 18),
    bg="black",
    fg="white"
)
result_label.pack(pady=20)

# Run application
window.mainloop()
