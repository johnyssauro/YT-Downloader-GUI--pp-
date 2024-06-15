from tkinter import *
from tkinter import ttk
from pytube import YouTube
from pytube import Playlist

def videoDownload(*args):

    SAVE_PATH = "C:/Users/João/OneDrive/João Pedro/Vídeos"
    SAVE_PATH_PLAYLIST = "C:/Users/João/OneDrive/João Pedro/Vídeos/Workout"

    try:
        if option.get() == "video":
            url = str(yt.get())
            video = YouTube(url)

            ttk.Label(mainframe, text=video.title).grid(column=2, row=3, sticky=(W,E))
            video.streams.first().download(SAVE_PATH)

        else:

            url = str(yt.get())
            playlist = Playlist(url)
            ttk.Label(mainframe, text=playlist.title).grid(column=2, row=3, sticky=(W,E))
            
            for video in playlist.videos:
                try:
                    ttk.Label(mainframe, text=playlist.title).grid(column=2, row=3, sticky=(W,E))
                    video.streams.first().download(SAVE_PATH_PLAYLIST)
                except:
                    ttk.Label(mainframe, text=f"*VIDEO* {video.title} *UNAVAILABLE*").grid(column=2, row=3, sticky=(W,E))

    except:

        ttk.Label(mainframe, text="SOME ERROR!").grid(column=2, row=3, sticky=(W,E))

root = Tk()

root.name = "YouTube Dowloader"

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=1, row=1, sticky=(N,W,E,S))

option = StringVar()
option.set("video")

frame1 = ttk.Frame(mainframe, padding="3 3 4 4")
frame1.grid(column=1, row=1, sticky=(N,S,W,E))

videoButton = ttk.Radiobutton(frame1, text = "Video", variable=option, value="video")
playlistButton = ttk.Radiobutton(frame1, text = "Playlist", variable=option, value="playlist")

videoButton.grid(column=1, row=1, sticky=(W))
playlistButton.grid(column=1, row=3, sticky=(W))

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
