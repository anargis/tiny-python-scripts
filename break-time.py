import time
import subprocess
import webbrowser

class BreakTime:
    def __init__(self):
        while True:
            try:
                self.wait_minutes = int(input("When would you like your break to start? Enter time in minutes (e.g., 60): "))
                if self.wait_minutes < 0:
                    print("You must enter a positive integer, try again.")
                    continue
                self.break_time = int(input("How long should your break last? Enter time in minutes (e.g., 5): "))
                if self.break_time < 0:
                    print("You must enter a positive integer, try again.")
                    continue
                break
            except ValueError:
                print("You must enter an integer number, try again.")

    def schedule_break(self):
        print(f"Your break will start in {self.wait_minutes} minutes.")
        subprocess.run(['notify-send', 'Break Scheduled', f'Your break will start in {self.wait_minutes} minutes.'])
        time.sleep(self.wait_minutes * 60)

        subprocess.run(['notify-send', 'Break Started!', f'Your break for {self.break_time} minutes has started.'])
        print(f"Break started for {self.break_time} minutes.")
        time.sleep(self.break_time * 60)
        
        webbrowser.open("https://www.youtube.com/watch?v=4Gk_ROalMXQ")
        subprocess.run(['notify-send', 'Break Finished!', 'Your break is over!'])
        print("Break is over!")

if __name__ == "__main__":
    bt = BreakTime()
    bt.schedule_break()