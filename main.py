from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
file = 0
def progress1(stream=None,chunk=None,remaining=None):
    size = (file-remaining)
    per = (size/file)*100
    btn.config(text="{:00.0f} % downloaded...".format(per))



def searchvid():
    try:
        url = field.get()
        print(url)
        btn.config(text="please wait..")
        btn.config(state=DISABLED)

        ob = YouTube(url)
        strm = ob.streams.first()
        btn.config(text="Download")
        btn.config(state=NORMAL)
        title = Label(main, text="Title:- {}".format(strm.title), font=("vardana", 11), justify=LEFT)
        title.pack(side=TOP, padx=0)
        rating = Label(main, text="Rating:- {:0.1f}/5".format(ob.rating), font=("vardana", 11))
        rating.pack(side=TOP, pady=20)

        btn.config(command=startThread2)
    except Exception as e:
        print(e)
        print("something went wrong")
def startdownload():
    global file
    try:
        url2 = field.get()
        btn.config(text="please wait...")
        btn.config(state=DISABLED)
        save=askdirectory()
        print(save)
        if save is None:
            return
        ob = YouTube(url2, on_progress_callback=progress1)
        strm = ob.streams.first()
        file=strm.filesize
        strm.download(save)
        btn.config(text="Search")
        btn.config(state=NORMAL)
        btn.config(command=startThread)
    except Exception as e:
        print(e)
        print("something went wrong")

def startThread():
    thread=Thread(target=searchvid)
    thread.start()
def startThread2():
    thread2=Thread(target=startdownload)
    thread2.start()

main = Tk()
main.title("my YouTube downloader")
main.config(background="#FFFDFD")
file=PhotoImage(file='youtube.png')
logo=Label(main, image=file)
logo.pack(side=TOP)
field = Entry(main, font=("vardana", 18), justify=CENTER)
field.pack(side=TOP, fill=X, padx=10)
btn = Button(main, text='Search', font=("vardana", 18), relief='ridge', command=startThread)
btn.pack(side=TOP, fill=Y, pady=30)
main.geometry('500x600')
main.mainloop()
