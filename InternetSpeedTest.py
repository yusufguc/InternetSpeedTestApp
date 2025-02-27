from tkinter import *
import speedtest
import threading 

root=Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False,False)
root.configure(bg="#1a212d")



def check():
    button.config(state=DISABLED)  
    threading.Thread(target=run_speedtest).start()

def run_speedtest():
    test = speedtest.Speedtest()
    downloading = round(test.download() / (1024*1024), 2)
    uploading = round(test.upload() / (1024*1024), 2)
    ping_value = test.results.ping
    
    root.after(0, update_gui, downloading, uploading, ping_value)

def update_gui(downloading, uploading, ping_value):
    download.config(text=downloading)
    Download.config(text=downloading)
    upload.config(text=uploading)
    ping.config(text=ping_value)
    button.config(state=NORMAL) 


#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#Images

image_top=PhotoImage(file="top.png")
Label(root,image=image_top,bg="#1a212d").pack()

image_main=PhotoImage(file="main.png")
Label(root,image=image_main,bg="#1a212d").pack(pady=(40,0))

image_button=PhotoImage(file="button.png")
button=Button(root,image=image_button,bg="#1a212d",bd=0,cursor="hand2",activebackground="red",command=check)
button.pack(pady=10)

Label(root,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
Label(root,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
Label(root,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

Label(root,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
Label(root,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

Label(root,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=280)
Label(root,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

ping=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
ping.place(x=70,y=60,anchor="center")

download=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
download.place(x=180,y=60,anchor="center")

upload=Label(root,text="00",font="arial 13 bold",bg="#384056",fg="white")
upload.place(x=290,y=60,anchor="center")

Download=Label(root,text="00",font="arial 40 bold",bg="#384056")
Download.place(x=185,y=350,anchor="center")
root.mainloop()
