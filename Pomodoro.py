from tkinter import *
import time
from tkinter import messagebox
from tkmacosx import Button


root = Tk()
root.geometry('200x200')
# root.resizable(0,0)
root.config(bg ='blanched almond')
root.title('Pomodoro')
Label(root, text = 'Pomodoro' , font = 'arial 20 bold',  bg ='papaya whip').pack()

# def clock():
#     clock_time = time.strftime('%H:%M:%S %p')
#     curr_time.config(text = clock_time)
#     curr_time.after(1000,clock)

flag = True
five_mins = 5*60
twentyfive_mins = 25*60


def timer():
    count = 0
    time_number = twentyfive_mins
    while time_number > -1:
        mins = time_number//60
        secs = time_number%60
        str_secs = str(secs).zfill(2)
        curr_time.config(text = f"{mins}:{str_secs}")
        count_label.config(text = "Count: " + str(count//2))
        root.update()
        root.after(1000)
        if (time_number == 0):
            count += 1
            messagebox.showinfo("Time Countdown", "Time's up ")
            if count % 2 == 0:
                time_number = twentyfive_mins
            else:
                time_number = five_mins
        if flag:
            time_number -= 1



def pause():
    global flag
    if flag is True:
        btn_text.set("Start")
        flag = False
    else:
        btn_text.set("Pause")
        flag = True

count_label = Label(root, font ='arial 15 bold', fg = 'gray25' ,bg ='papaya whip' )
count_label.place(relx = 0.35 , rely = 0.5)
curr_time =Label(root, font ='arial 35 bold', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(relx = 0.3 , rely = 0.2)
btn_text = StringVar()
btn = Button(root, textvariable=btn_text, command= pause)
btn_text.set("Pause")
btn.place(relx = 0.27, rely = 0.8)
timer()

root.mainloop()