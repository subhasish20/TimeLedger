import subprocess


class ScreenTimeTracker:
    """
    Tracks the amount of time spent using active applications.

    The tracker identifies the application associated with the currently
    active window and maintains the accumulated screen time for each
    application.
    """

    def __init__(self):
        """
        Initializes the screen time tracker.

        Creates an empty dictionary to store the accumulated screen time
        for each application.
        """
        self.screen_time = {}

    def get_active_app(self):
        """
        Retrieves the name of the currently active application.

        Determines the process ID of the active window and uses it to
        identify the corresponding application.

        Returns:
            str: The name of the active application, or "Unknown" if the
            active application cannot be determined.
        """
        try:
         # Retrieve the process ID of the currently active window.
            pid = subprocess.check_output(
                ['kdotool', 'getactivewindow', 'getwindowpid'],
                text=True
            ).strip()
            # Retrieve the application name associated with the process ID.
            app = subprocess.check_output(
                ['ps', '-p', pid, '-o', 'comm='],
                text=True
            ).strip()
             # Assign a fallback value when the required system commands fail.
        except subprocess.CalledProcessError:
            app = "Unknown"

        return app

    def add_time(self, app):
        """
        Updates the accumulated screen time for an application.

        Initializes the application's screen time when it is encountered
        for the first time and increments it for subsequent occurrences.

        Args:
            app (str): Name of the application whose screen time is updated.
        """
        if app not in self.screen_time:
            self.screen_time[app] = 1
        else:
            self.screen_time[app] += 1
        """
        Returns the accumulated screen time for all tracked applications.

        Returns:
            dict: A dictionary containing application names as keys and
            their accumulated screen time as values.
        """
    def get_screen_time(self):
        return self.screen_time
