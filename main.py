from tkinter import *
from TimeLedger.timeledger import  ScreenTimeTracker

root = Tk()

""""
root.title("TimeLedger")

root.geometry("600x600")
root.minsize(400, 400)

root.config(bg="#93F9B9")

root.mainloop()"""

tracker = ScreenTimeTracker()
tracker.trace_active_app()