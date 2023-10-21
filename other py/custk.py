import tkinter
import customtkinter
from time import sleep
from threading import Thread

root = tkinter.Tk()
root.title("Custom Tkinter")
root.geometry("500x500")

def button_function():
    print("Button pressed")

# button = customtkinter.CTkButton(master=root, corner_radius=10, command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root,
                                           width=200,
                                           height=20,
                                           border_width=1,
                                           border_color="#000000",
                                           bg_color="#FFFFFF",
                                           fg_color="#000000",
                                           corner_radius=5,
                                           progress_color="green")

progressbar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def move_progressbar():
    for i in range(1, 100):
        progressbar.set(i / 100)
        sleep(.1)

thread = Thread(target=move_progressbar)
thread.start()

# progressbar.set(.9)

root.mainloop()



