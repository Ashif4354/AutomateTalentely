from tkinter import Tk, Label, Button
from requests import get
from json import load, loads
import winsound
from webbrowser import open_new

def check_update():
    response = get('https://tcsversion.netlify.app')
    new_version = loads(response.text)['version']

    with open('C:/Users//Documents/AutomateTalentely/Configuration.json', 'r') as file:
        old_version = load(file)['version']

    if new_version != old_version:
        winsound.MessageBeep(winsound.MB_ICONHAND)
        alert_box = Tk()
        alert_box.title("Good News")
        alert_box.geometry("300x100")
        label = Label(alert_box, text="A new version of the app is available")
        label.pack()
        label = Label(alert_box, text="Download now at ")
        label.pack()
        label = Label(alert_box, text='url', fg="blue", cursor="hand2")
        label.bind("<Button-1>", lambda event: open_new('google.com'))
        label.pack()
        button = Button(alert_box, text="OK", command=alert_box.destroy)
        button.config(width=10, height=1)
        button.pack()
        alert_box.mainloop()

check_update()