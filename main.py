import tkinter as tk
from TimeLedger.TimeLedger import ScreenTimeTracker


"""
Provides the graphical user interface for the screen time tracker.

The application allows the user to start and stop screen time tracking
and displays the accumulated usage time for each active application.
"""
tracker = ScreenTimeTracker()

running = False


def start():
    """
    Starts the screen time tracking process.

    Sets the tracking state to active and initiates the periodic tracking
    function.
    """
    global running

    running = True
    track()


def stop():
    """
    Stops the screen time tracking process.

    Sets the tracking state to inactive, preventing further tracking
    iterations from being scheduled.
    """
    global running

    running = False


def track():
    """
    Tracks the currently active application.

    Retrieves the active application, updates its accumulated screen time,
    refreshes the displayed usage information, and schedules the next
    tracking cycle at one-second intervals.
    """
    if running:
        # Retrieve and record the currently active application.
        app = tracker.get_active_app()

        tracker.add_time(app)
        # Refresh the displayed screen time.
        show_time()
        # Schedule the next tracking cycle to execute after a one-second delay.
        window.after(1000, track)


def show_time():
    """
    Updates the interface with the accumulated screen time.

    Converts the recorded time for each application from seconds into
    hours, minutes, and seconds before displaying the results.
    """
    result = ""

    for app, seconds in tracker.get_screen_time().items():

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        result += f"{app}: {hours:02d}:{minutes:02d}:{seconds:02d}\n"

    label.config(text=result)

"""
Initializes and configures the main application window, creates the
screen time control buttons and display label, and starts the Tkinter
event loop.
"""
window = tk.Tk()


# Configure the window title, dimensions, and background appearance.
window.title("Screen Time Tracker")
window.geometry("600x600")
window.config(bg="black")

# Create the button responsible for starting screen time tracking.

start_button = tk.Button(
    window,
    text="Start",
    command=start
)

start_button.pack(pady=20)


# Create the button responsible for stopping screen time tracking.
stop_button = tk.Button(
    window,
    text="Stop",
    command=stop
)

stop_button.pack(pady=10)



# Create the label used to display screen time information.
label = tk.Label(
    window,
    text="Press Start to activate the App",
    bg="black",
    fg="white",
    font=("Arial", 20)
)

label.pack(pady=20)


# Start the Tkinter event loop and handle user interactions.
window.mainloop()
