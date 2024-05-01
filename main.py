from pytube import YouTube
import tkinter as tk

def startDownload():
    try :
        ytlink = textbox.get()
        ytOgj = YouTube(ytlink)
        video = ytOgj.streams.get_highest_resolution()
        video.download()
    except:
        print("Your link is invalid")
    flabel.configure(text="Downloaded")
        

#System setting
root = tk.Tk()
root.geometry("500x500")
root.title("Youtube video Downloader")

label = tk.Label(root, text="YouTube video Downloader",font=("Arial",20))
label.pack(padx=0,pady=15)

label2 = tk.Label(root, text="Insert Your URL",font=("Arial",15))
label2.pack(padx=0,pady=0)

#link input
url_var = tk.StringVar()
textbox = tk.Entry(root,width=40,font=("Arial",15),textvariable=url_var)
textbox.pack(pady=12)
#button
button = tk.Button(root,text="Download",font=("Arial",15),command=startDownload)
button.pack(pady=10)

#finish label
flabel = tk.Label(root,text="",font=("Arial",15))
flabel.pack()
root.mainloop()