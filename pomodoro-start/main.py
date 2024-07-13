from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
#   reset checkmarks
    checkmarks.config(text="", fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=YELLOW)
    elif reps / 2 == 4:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # using dynamic typing change the count sec to a sting from an integer
    if count_sec == 0 or count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # takes in the time, the function its calling and the argument of the function i.e the input
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            checkmarks.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=200, height=223, bg=PINK, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="TIMER", bg=PINK, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

checkmarks = Label(text="", bg=PINK, fg=GREEN, font=(FONT_NAME, 24, "bold"))
checkmarks.grid(column=1, row=3)

start_button = Button(text="start", highlightbackground=PINK, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightbackground=PINK, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
