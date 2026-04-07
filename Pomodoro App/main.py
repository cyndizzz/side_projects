from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN, bg=YELLOW)
    check_marks.config(text="", fg=GREEN, bg=YELLOW)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    interval = 1
    work_sec = WORK_MIN * interval
    short_break_sec = SHORT_BREAK_MIN * interval
    long_break_sec = LONG_BREAK_MIN * interval

    if reps % 2 == 1:
        timers = work_sec
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 8 ==0:
        timers = long_break_sec
        timer_label.config(text='Break', fg=RED)
    else:
        timers = short_break_sec
        timer_label.config(text='Break', fg=PINK)


    countdown(timers)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    mins = count // 60
    if mins <= 9:
        mins = f'0{mins}'
    secs = count % 60
    if secs <= 9:
        secs = f'0{secs}'

    canvas.itemconfig(timer_text, text = f'{mins}:{secs}')
    if count>0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        n_ticker = reps // 2
        check_marks.config(text="✔" * n_ticker, fg=GREEN, bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg=YELLOW)


# Timer Label
timer_label = Label(text = 'Timer', font =(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill = 'white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row = 1, column = 1)

# Start Button
start_button = Button(text = 'Start', highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text = 'Reset', highlightbackground=YELLOW, command=reset)
reset_button.grid(row=2, column=2)

# Ticker Status
check_marks = Label(text = "✔"*reps, fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)



window.mainloop()