from pytube import YouTube
import tkinter as tk
from tkinter import ttk
def startDownload():
    try :
        ytlink = textbox.get()
        ytOgj = YouTube(ytlink,on_progress_callback=on_progress)
        video = ytOgj.streams.get_highest_resolution()
        video.download()
        flabel.configure(text="Downloaded",fg="green")
    except:
        flabel.configure(text="Download Error",fg="red")
   
def on_progress(stream,chunk,byte_remain):
    file_size = stream.filesize
    byte_downloaded = file_size-byte_remain
    percentage  =byte_downloaded/file_size*100
    per = str(int(percentage))  
    pPercen.configure(text= per +"%")  
    pPercen.update()     
    
    #update progress bar
    progress["value"]= percentage  

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

#progress label
pPercen = tk.Label(root,text="",font=("Arial",10))
pPercen.pack()

#progress bar
progress = ttk.Progressbar(root,orient="horizontal",length=350)
progress["value"]= 0
progress.pack()

root.mainloop()