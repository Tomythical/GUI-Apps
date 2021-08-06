from tkinter import *
import time
from tkinter import messagebox
from tkmacosx import Button
import webbrowser


root = Tk()
root.geometry('200x200')
# root.resizable(0,0)
root.config(bg ="#263D42")
root.title('Animedoro')
Label(root, text = 'Animedoro' , font = 'arial 20 bold',  bg ="#263D42").pack()

# def clock():
#     clock_time = time.strftime('%H:%M:%S %p')
#     curr_time.config(text = clock_time)
#     curr_time.after(1000,clock)

flag = True
five_mins = 20*60
twentyfive_mins = 45*60

time_number = twentyfive_mins

def timer():
    count = 0
    global time_number
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
            # messagebox.showinfo("Time Countdown", "Time's up ")
            pause()
            if count % 2 == 0:
                time_number = twentyfive_mins
            else:
                webbrowser.open('https://animekisa.tv/wonder-egg-priority')
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

def skip():
    global time_number
    time_number = 0

count_label = Label(root, font ='arial 15 bold',bg ="#263D42" )
count_label.place(relx = 0.35 , rely = 0.5)
curr_time =Label(root, font ='arial 35 bold',bg ="#263D42")
curr_time.place(relx = 0.3 , rely = 0.2)
btn_text = StringVar()
btn = Button(root, textvariable=btn_text, command= pause)
btn_text.set("Pause")
btn_text2 = StringVar()
btn2 = Button(root, textvariable=btn_text2, command= skip)
btn_text2.set("Skip")
btn.place(relx = 0.27, rely = 0.675)
btn2.place(relx = 0.27, rely = 0.825)
timer()

root.mainloop()