# CTK Repo:     https://customtkinter.tomschimansky.com/
# Pytube Repo:  https://pytube.io/en/latest/api.html#pytube.YouTube.thumbnail_url

import tkinter, customtkinter, urllib.request, io
from pytube import YouTube, Playlist
from PIL import ImageTk, Image

# Var
ctk = customtkinter


# fix this based on this tutorial
def DisplayThumbnail(thumb_url):
    with urllib.request.urlopen(thumb_url) as u:
        raw_data = u.read()
    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)
    thumb = ctk.CTkLabel(app, image="")
    thumb.configure(image=photo)
    return image, photo

def StartDownload():
    try: 
        ytLink  = link.get()
        ytObject= YouTube(ytLink, on_progress_callback = on_progress)
        video   = ytObject.streams.get_highest_resolution()
        # ytObject.streams -> use this to add video resolutions for download
        title.configure(text=ytObject.title, text_color="white")
        thumbnail = thumb.configure(text=ytObject.thumbnail_url, text_color="blue")
        thumb_url = ytObject.thumbnail_url
        print(thumb_url)
        video.download()
        print("Download Complete")
        finishLabel.configure(text="Downloaded!", text_color="green")
    except:
        finishLabel.configure(text="Download failed :(", text_color="red")
        print("Youtube link is invalid")
    return 
    
def on_progress(stream, chunk, bytes_remaining):
    total_size  = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size *100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    # Update Progress Bar
    progressBar.set(float(percentage_of_completion)/100)


# Playslist download function already made. Need to test and add a selector for implementation
def Playlist():
    ytLink=link.get()
    ytObject= Playlist(ytLink, on_progress_callback = on_progress)
    for video in ytObject.videos:
        video.streams.first().download()
    return



# System Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App Frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
title = ctk.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()

# Thumbnail
DisplayThumbnail("https://i.ytimg.com/vi/iO9L4QA1Phw/hq720.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYACpAWKAgwIABABGGUgTyhDMA8=&rs=AOn4CLC1Rzk_VGFMomiy5dTgnRpgglImJQ")
thumb = ctk.CTkLabel(app, image="")
thumb.pack()

# Progress percentage
pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = ctk.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack()

# Download Button
download = ctk.CTkButton(app, text="Download", command=StartDownload)
download.pack(padx=10, pady=10)

# Run App
app.mainloop()