import tkinter as tk
import time
import random

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ثانیه شمار")
        self.root.geometry("500x500")  # ابعاد تایمر افزایش یافته

        # تعیین متغیرها
        self.timer_running = False
        self.start_time = 0
        self.seconds = 0

        # تعیین رنگ‌های تصادفی برای کادر
        self.random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # ایجاد کادر
        self.frame = tk.Frame(root, bg=self.random_color)
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # نمایش تایمر
        self.timer_label = tk.Label(self.frame, text="00:00:00", font=("Helvetica", 36))
        self.timer_label.pack(side="top", pady=20)

        # نمایش فاصله شما از صاعقه
        self.distance_label = tk.Label(self.frame, text="فاصله شما از صاعقه: 0.00 کیلومتر", font=("Helvetica", 18))
        self.distance_label.pack(side="top", pady=20)

        # کلید شروع/توقف
        self.start_stop_button = tk.Button(self.frame, text="شروع", bg="green", font=("Helvetica", 20), command=self.toggle_timer)
        self.start_stop_button.pack(side="left", padx=20)

        # کلید Reset
        self.reset_button = tk.Button(self.frame, text="Reset", font=("Helvetica", 20), command=self.reset_timer)
        self.reset_button.pack(side="left", padx=10)

        # کلید Exit
        self.exit_button = tk.Button(self.frame, text="Exit", font=("Helvetica", 20), command=root.quit)
        self.exit_button.pack(side="right", padx=10)

    def toggle_timer(self):
        if not self.timer_running:
            self.start_timer()
        else:
            self.stop_timer()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time() - self.seconds
            self.update_timer()
            self.start_stop_button.config(text="توقف", bg="red")

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.seconds = time.time() - self.start_time
            self.display_distance()
            self.start_stop_button.config(text="شروع", bg="green")

    def reset_timer(self):
        self.timer_running = False
        self.start_time = 0
        self.seconds = 0
        self.timer_label.config(text="00:00:00")
        self.distance_label.config(text="فاصله شما از صاعقه: 0.00 کیلومتر")
        self.random_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.frame.config(bg=self.random_color)

    def update_timer(self):
        if self.timer_running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            self.seconds = elapsed_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            self.timer_label.config(text=formatted_time)
            self.root.after(1000, self.update_timer)

    def display_distance(self):
        distance = self.seconds * 0.32
        self.distance_label.config(text=f"فاصله شما از صاعقه: {distance:.2f} کیلومتر")

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
