import subprocess


class ScreenTimeTracker:

    def __init__(self):
        self.screen_time = {}

    def get_active_app(self):

        try:
            pid = subprocess.check_output(
                ['kdotool', 'getactivewindow', 'getwindowpid'],
                text=True
            ).strip()

            app = subprocess.check_output(
                ['ps', '-p', pid, '-o', 'comm='],
                text=True
            ).strip()

        except subprocess.CalledProcessError:
            app = "Unknown"

        return app

    def add_time(self, app):

        if app not in self.screen_time:
            self.screen_time[app] = 1
        else:
            self.screen_time[app] += 1

    def get_screen_time(self):
        return self.screen_time
