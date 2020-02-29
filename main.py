from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file = 0
yo
def progress1(stream=None,chunk=None,remaining=None):
    size = (file-remaining)
    per = (size/file)*100
    btn.config(text="{:00.0f} % downloaded...".format(per))
def startdownload():
    global file
    try:
        url = field.get()
        print(url)
        btn.config(text="please wait..")
        btn.config(state=DISABLED)
        save = askdirectory()
        if save is None:
            return
        print(save)
        ob = YouTube(url,on_progress_callback=progress1)
        strm = ob.streams.first()
        file = strm.filesize
        title = Label(main, text="Title: {}".format(strm.title), font=("vardana", 11),justify=LEFT)
        title.pack(side=TOP, padx=0)
        rating=Label(main, text="rating: {}".format(ob.rating), font=("vardana",11))
        rating.pack(side=TOP, fill=X, padx=0)
        print(file)
        strm.download(save)
        field.delete(0,END)
        showinfo("download completed","download success")

        btn.config(text="Download")
        btn.config(state=NORMAL)
    except Exception as e:
        print(e)
        print("something went wrong")
def startThread():
    thread=Thread(target=startdownload)
    thread.start()

main = Tk()
main.title("my YouTube downloader")
main.config(background="#FFFDFD")
file=PhotoImage(file='youtube.png')
logo=Label(main, image=file)
logo.pack(side=TOP)
field = Entry(main, font=("vardana", 18), justify=CENTER)
field.pack(side=TOP, fill=X, padx=10)
btn = Button(main, text='Download', font=("vardana", 18), relief='ridge', command=startThread)
btn.pack(side=TOP, fill=Y, pady=10)
main.geometry('500x600')
main.mainloop()
