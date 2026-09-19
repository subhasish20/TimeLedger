import tkinter as tk

from pkg.MyTrace import ScreenTimeTracker


tracker = ScreenTimeTracker()

running = False


def start():
    global running

    running = True
    track()


def stop():
    global running

    running = False


def track():

    if running:

        app = tracker.get_active_app()

        tracker.add_time(app)

        show_time()

        window.after(1000, track)


def show_time():

    result = ""

    for app, seconds in tracker.get_screen_time().items():

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        result += f"{app}: {hours:02d}:{minutes:02d}:{seconds:02d}\n"

    label.config(text=result)


window = tk.Tk()

window.title("Screen Time Tracker")
window.geometry("600x600")
window.config(bg="black")


start_button = tk.Button(
    window,
    text="Start",
    command=start
)

start_button.pack(pady=20)


stop_button = tk.Button(
    window,
    text="Stop",
    command=stop
)

stop_button.pack(pady=10)


label = tk.Label(
    window,
    text="Press Start to activate the App",
    bg="black",
    fg="white",
    font=("Arial", 20)
)

label.pack(pady=20)


window.mainloop()
