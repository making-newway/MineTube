'''
Created on 24-Dec-2020

@author: SAYAN DEY
'''
from tkinter import *
from tkinter.filedialog import *
from pytube import YouTube
import webbrowser
from PIL import Image, ImageTk
#const colors
#------------------------------------------------------------------------------

prim_color = "#222"
seco_color = "#445799"
bhul_color = "#e84a35"

semi_prim_color = "#666"
semi_seco_color = "#095787"
semi_bhul_color = "#574747"

root = Tk()
root.geometry("720x540")
root.title("YouTube Video Downloader")
root.resizable(False, False)


fbimag = Image.open("E:/Eclipse/mYPy/WindowsApp/fb.png").resize((30, 30), Image.ANTIALIAS)
fbimg = ImageTk.PhotoImage(fbimag)
ghimag = Image.open("E:/Eclipse/mYPy/WindowsApp/gh.png").resize((30, 30), Image.ANTIALIAS)
ghimg = ImageTk.PhotoImage(ghimag)

#https://youtu.be/g2orJgNOpnU

#Back-end Work
#------------------------------------------------------------------------------


link = StringVar()
path = StringVar()
nameText = StringVar(root)
nameText.set("Video Name : ")
opt = ["none"]
s = StringVar(root)
s.set(opt[0])
options = []


def getLink():
    options.clear()
    links = ytlink.get()
    link.set(links)
    py = nameText.get()
    if len(links) > 1:
        yt = YouTube(links)
        ca = yt.title
        nameText.set(py + " " + ca)
    else:
        nameText.set(py + " " + "No video")
    
    videos = yt.streams
    i = 1
    for video in videos:
        vid = str(video)
        typ = vid.find("mime_type=")
        els = ""
        qs = ""
        res = 0
        if "vcodec" in vid and "acodec" in vid:
            els += "Video & Audio"
            res = vid.find("res=")
            qs += re.sub("[^0-9]+", "", vid[res+5:res+9]) + 'p'
        elif "vcodec" in vid:
            els += "Video Only"
            res = vid.find("res=")
            qs += re.sub("[^0-9]+", "", vid[res+5:res+9]) + 'p'
            if "None" in vid:
                continue
        elif "acodec" in vid:
            els += "Audio Only"
            res = vid.find("abr=")
            qs += re.sub("[^0-9]+", "", vid[res+5:res+9]) + 'kbps'
        options.append(str(i) +" " + els + " "+ qs +" "+ vid[typ+11:res-2])
        i+=1
    quality.children["menu"].delete(0, "end")
    for option in options:
        quality.children["menu"].add_command(label=option, command=lambda o=option: s.set(o))
    
def director():
    dirr = askdirectory(initialdir="C:/Users")
    path.set(dirr)
    
def download():
    ytubelink = link.get()
    choice = s.get()
    choice = int(choice[:2].strip())
    paths = path.get()
    ytube = YouTube(ytubelink).streams
    stream = ytube[choice-1]
    stream.download(paths)
    
    
"""
choice = int(input("Give the Choice"))
stream = videos[choice-1]
stream.download('C:/Users/SAYAN DEY/Desktop')

print("downloaded")"""


#Front-End Work
#------------------------------------------------------------------------------


"""*-----------------------------Header Area-----------------------------*"""

header = Label(root, text="YouTube Video Downloader", height="2", width="600" , bg=seco_color, fg="white", font=("Jokerman", 24))
header.pack()

"""*-----------------------------Link Given Area-----------------------------*"""

data = Frame(root, height="2", width="600", bg=prim_color )
data.pack(side=TOP)

Label(data, text="Give The Link: ",bg=prim_color, fg="white", font=("Castellar", 20), width="600").pack()
setFrame = Frame(data, height="150", width="720", bg=prim_color)
setFrame.pack(side=TOP)
ytlink = Entry(setFrame, width="30", bg=semi_prim_color, fg="White", textvariable=link, font=("Arial", 20))
ytlink.grid(row=0, column=0, padx="2")
ytbutt = Button(setFrame, text="Search", height="1", width="12", bg=seco_color, fg="White", font=("Arial", 14),  command=getLink)
ytbutt.grid(row=0, column=1)


"""*-----------------------------Video Name Area-----------------------------*"""

Label(data, textvariable=nameText, fg="white", bg=prim_color, height="3", font=("Arial", 12)).pack()


"""*-----------------------------Quality Area-----------------------------*"""

directory = Frame(root, height="180", width="720", bg="white")
directory.pack(side=TOP)

qual = Label(directory, height="3", width="720", bg="white")
qual.pack()
Label(qual, text="Download quality", bg="white", font=("Arial", 20)).grid(row=0, column=0)
quality = OptionMenu(qual, s, *opt)
quality.grid(row=0, column=1)
#https://youtu.be/Al7WF2aq6to

"""*-----------------------------Video Saving Area-----------------------------*"""

Label(directory ,bg="white", fg="white", font=("Castellar", 20), width="600").pack()
dirFrame = Frame(directory, height="140", width="720", bg="white")
dirFrame.pack(side=TOP)
Label(dirFrame, text="Save the Video :- ",bg="white", fg="black", font=("Constantia", 12)).grid(row=1, column=0)
download_path = Entry(dirFrame, width="30", fg="Black", font=("Arial", 20), highlightcolor="black", bd=3, textvariable=path)
download_path.grid(row=1, column=1, padx="2")
Button(dirFrame, text="Browse", height="1", width="8", bg=prim_color, fg="white",font=("Arial", 10), command=director).grid(row=1, column=3)


"""*-----------------------------Download Area-----------------------------*"""

down = Frame(root, height="100", width="720", bg="white")
down.pack()
Label(down ,bg="white", fg="white", font=("Castellar", 20), width="600").pack()
Button(down, text="Download", bg=bhul_color, height="1", width="20", font=("Arial", 20), command=download).pack(side=BOTTOM)

"""*-----------------------------Footer Area-----------------------------*"""

Label(root, text="Follow me in here ", height="30").pack(side=LEFT)
link1 = Label(root, image=fbimg, fg="blue", cursor="hand2", height="30", width="30")
link1.pack(side=RIGHT)
link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.facebook.com/profile.php?id=100013563634745"))

link2 = Label(root, image=ghimg, fg="blue", cursor="hand2", height="30", width="30")
link2.pack(side=RIGHT)
link2.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/making-newway"))


root.mainloop()