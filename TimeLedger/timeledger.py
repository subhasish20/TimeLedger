
import subprocess # subprocess is used to run and communicate with external programs or system commands.
import  time # time is used to trace the time
import  sys # sys is used to apply exit()


class ScreenTimeTracker:
    def __init__(self):
        self.screen_time = {}

    def show_running_tasks(self,screen_time:dict):
        print("- - - - - - - - Running tasks - - - - - - - - ")
        for key in screen_time:
            print(f"App name :{key}\n")



    def show_final_screen_time(self,screen_time:dict):
        print("\n= = = = = = = = = = = = = = SCREEN TIME = = = = = = = = = = = = = = ")
        for key, value in screen_time.items():
            print(f"\n- - - - - - - - - - - - - - -\nApp name :{key}\nscreen time :{value //3600}hr--{(value % 3600) // 60}min--{value%3600}sec")


    def add_app_time(self,app_name, app_time):

        if app_name not in self.screen_time:
            self.screen_time[app_name] = 1
        else:
            self.screen_time[app_name] += 1
        self.show_running_tasks(self.screen_time)

    def get_current_active_app(self):
        try:
            # the process_id will give the name of the current process id
            process_id = subprocess.check_output(
                ["kdotool", "getactivewindow", "getwindowpid"],
                text=True
            ).strip()

            # we will fetch the app name by the below command
            app_name = subprocess.check_output(
                ["ps", "-p", process_id, "-o", "comm="],
                text=True
            ).strip()
        except subprocess.CalledProcessError:
            # if not in the app list
            app_name = "Unknown App"
        return  app_name

    def trace_active_app(self):

        start_time = time.time()
        while True:
            try:
                app_name = self.get_current_active_app()

                app_time = int(time.time() - start_time)
                self.add_app_time(app_name,app_time)
                time.sleep(1)

            except FileNotFoundError:
                print("kdotool is not installed.")
                sys.exit(0)

            except KeyboardInterrupt:
                self.show_final_screen_time(self.screen_time)
                print(end="")
                sys.exit(0)