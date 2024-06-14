from tkinter import *
from tkinter import ttk
from pytube import YouTube

def videoDownload(*args):

    SAVE_PATH = "C:/Users/João/OneDrive/João Pedro/Vídeos"

    try:

        url = str(yt.get())
        video = YouTube(url)

        ttk.Label(mainframe, text=video.title).grid(column=2, row=3, sticky=(W,E))
        video.streams.first().download(SAVE_PATH)

    except:

        ttk.Label(mainframe, text="SOME ERROR!").grid(column=2, row=3, sticky=(W,E))

root = Tk()

root.name = "YouTube Dowloader"

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

yt = StringVar()
yt_entry = ttk.Entry(mainframe, width=30, textvariable=yt)
yt_entry.grid(column=2, row=2, sticky=(E,W))

ttk.Label(mainframe, text='Insert URL:').grid(column=1, row=2, sticky=E)

ttk.Button(mainframe, text='Dowload', command=videoDownload).grid(column=3, row=2, sticky=(W))

for child in mainframe.winfo_children():

    child.grid_configure(padx=10, pady=10)
yt_entry.focus()
root.bind("<Return>", videoDownload)


root.mainloop()


