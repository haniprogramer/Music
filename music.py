from tkinter import *
import pygame
import os


root = Tk()
root.geometry('600x401')
root.resizable(0, 0)
root.title('Music Player')

status=StringVar()
pygame.init()

pygame.mixer.init()

# -----------------------------function----------------------------------

def playsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.insert('1.0',playlist.get(ACTIVE))
    songtrack.config(state=DISABLED)

    status.set('჻ Playing')

    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()


def stopsong():
    songtrack.config(state=NORMAL)
    songtrack.delete('1.0', END)
    songtrack.config(state=DISABLED)

    status.set('Ø Stopped')

    pygame.mixer.music.stop()


def pausesong():
    status.set('։։ Pasued')
    pygame.mixer.music.pause()


def unpusesong():
    status.set('჻ Playing')
    pygame.mixer.music.unpause()




# --------------------------------track-------------------------------

trackfram=LabelFrame(root,text='Media Output ●─────────',font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white',relief=GROOVE)
trackfram.place(x=0,y=200,width=600,height=105)

songtrack=Text(trackfram,width=40,height=2,font=('Arial',15),bg='Sky blue',fg='white',state=DISABLED)
songtrack.grid(row=0,column=0,padx=10,pady=5)

trackstatus=Label(trackfram,textvariable=status,font=('Arial',14),bg='Sky blue',fg='white')
trackstatus.grid(row=0,column=1,padx=10,pady=5)


# ---------------------------contorol-----------------------------


contorolpanel=LabelFrame(root,text='© Contorol Panel',font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white',relief=GROOVE,pady=10)
contorolpanel.place(x=0,y=305,width=600,height=95)

playbtn=Button(contorolpanel,text='Play',width=6,height=1,font=('Arial',16),fg='white',bg='Sky blue',command=playsong)
playbtn.place(x=10,y=-5)

pausebtn=Button(contorolpanel,text='Pause',width=9,height=1,font=('Arial',16),fg='white',bg='Sky blue',command=pausesong)
pausebtn.place(x=111,y=-5)

unpausebtn=Button(contorolpanel,text='Unpause',width=9,height=1,font=('Arial',16),fg='white',bg='Sky blue',command=unpusesong)
unpausebtn.place(x=252,y=-5)

stopbtn=Button(contorolpanel,text='Stop',width=6,height=1,font=('Arial',16),fg='white',bg='Sky blue',command=stopsong)
stopbtn.place(x=394,y=-5)

closebtn = Button(contorolpanel,text='Close',width=6,height=1,font=('Arial',16),fg='white',bg='red',command=root.destroy)
closebtn.place(x=498,y=-5)

# ---------------------------------song---------------------------

songfram=LabelFrame(root,text='⌠⌡List of Songs',font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white',relief=GROOVE,pady=10)
songfram.place(x=0,y=0,width=600,height=200)

scroll_y=Scrollbar(songfram,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

playlist=Listbox(songfram,selectbackground='gold',selectmode=SINGLE,font=('Arial',12),bg='Sky blue',fg='navyblue',bd=5,relief=GROOVE,yscrollcommand=scroll_y.set)
playlist.pack(fill=BOTH)
scroll_y.config(command=playlist.yview)


# --------------------------------------------------------------


# Instead (?) Enter your account name
os.chdir(r'C:\Users\؟؟؟؟\Music')
songtracks=os.listdir()
for track in songtracks:
    if '.mp3'in track:
        playlist.insert(END,track)
    else:
        pass

root.mainloop()





