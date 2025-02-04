from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer1)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="TIMER")
    tick.config(text=" ")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_sed=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        timer.config(text="Long Break",)
        count_timer(long_sec)
    elif reps%2==0:
        count_timer(short_sed)
        timer.config(text="Short Break")
    else:
        count_timer(work_sec)
        timer.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    count_min=math.floor(count/60)
    count_sec=count % 60

    if count_sec <10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
       global timer1
       timer1= window.after(1000,count_timer,count-1)
    else:
        start_countdown()
        mark=" "
        worksession=math.floor(reps/2)
        for i in range(worksession):
            mark+="✅"
            tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer=Label(text="TIMER",fg=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW,highlightthickness=0)
timer.grid(column=1,row=0)

canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start=Button(text="Start",command=start_countdown)
start.grid(column=0,row=2)

reset=Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=2)

tick=Label(bg=YELLOW)
tick.grid(column=1,row=3)

window.mainloop()
