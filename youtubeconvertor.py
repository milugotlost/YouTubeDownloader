import tkinter as tk
from tkinter import filedialog
import pytube
import os

def browse():
    download_path.set(filedialog.askdirectory())

def download():
    url = entry_url.get()
    save_path = download_path.get()
    if not url.startswith("https://www.youtube.com/"):
        status_text.set("Invalid URL")
        return
    try:
        youtube = pytube.YouTube(url)
        status_text.set("Downloading...")
        if var_format.get() == "mp4":
            video = youtube.streams.get_highest_resolution()
        elif var_format.get() == "mp3":
            video = youtube.streams.filter(only_audio=True).first()
        else:
            status_text.set("Invalid format")
            return
        video.download(save_path)
        status_text.set("Download completed")
    except:
        status_text.set("Download failed")

root = tk.Tk()
root.title("YouTube Downloader")

download_path = tk.StringVar()
var_format = tk.StringVar()

label_url = tk.Label(root, text="URL:")
label_url.grid(row=0, column=0, padx=10, pady=10)

entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=10, pady=10)

label_format = tk.Label(root, text="Format:")
label_format.grid(row=1, column=0, padx=10, pady=10)

mp4_radio = tk.Radiobutton(root, text="mp4", variable=var_format, value="mp4")
mp4_radio.grid(row=1, column=1)

mp3_radio = tk.Radiobutton(root, text="mp3", variable=var_format, value="mp3")
mp3_radio.grid(row=1, column=2)

label_path = tk.Label(root, text="Download Path:")
label_path.grid(row=2, column=0, padx=10, pady=10)

entry_path = tk.Entry(root, width=50, textvariable=download_path)
entry_path.grid(row=2, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=browse)
button_browse.grid(row=2, column=2)

button_download = tk.Button(root, text="Download", command=download)
button_download.grid(row=3, column=1, padx=10, pady=10)

status_text = tk.StringVar()
status_text.set("Enter URL and choose format")
status_label = tk.Label(root, textvariable=status_text)
status_label.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
