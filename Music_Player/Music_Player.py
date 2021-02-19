from tkinter import*
import pygame
from pygame import mixer
import os
from PIL import Image, ImageTk

def play_song():
    song=screen.get(ACTIVE)
    print('song')
    mixer.music.load(song)
    status.set('Playing')
    mixer.music.play()

def pause_song():
    status.set('Resume')
    mixer.music.pause()

def Unpause_song():
    status.set('Resume')
    mixer.music.unpause()

def Stop_song():
    status.set('Stop')
    mixer.music.stop()

def Next_Song():
    current_song=screen.curselection()
    current_song=current_song[0]+1
    song=screen.get(current_song)
    mixer.music.load(song)
    mixer.music.play(loops=0)
    screen.selection_clear(0,END)
    screen.activate(current_song)
    screen.selection_set(current_song, last=None)

def Previous_Song():
    current_song=screen.curselection()
    current_song=current_song[0]-1
    song=screen.get(current_song)
    mixer.music.load(song)
    mixer.music.play(loops=0)
    screen.selection_clear(0,END)
    screen.activate(current_song)
    screen.selection_set(current_song, last=None)

def exit():
    root.destroy()


root=Tk()
root.title('Spearton Music System')


mixer.init()
status=StringVar()
status.set('Choosing')

canvas1=Canvas(root,height=201,width=400,bg='#FFFFFF')
canvas1.pack()

screen=Listbox(root,selectmode='Single',bd=2,bg='#15133D',fg='#7EC850',selectbackground='#7EC850',selectforeground='#15133D',font=('Courier,12'))
canvas1.create_window(201,49,height=100,width=398,window=screen)

os.chdir(r'C:\Users\Dell\Desktop\python\projects\Music_Player\Sample Song')
Songs=os.listdir()

for mp3 in Songs:
    screen.insert(END,mp3)

play1=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\play.jpg')
photo1=play1.resize((100,100),Image.ANTIALIAS)
play1=ImageTk.PhotoImage(photo1)

Resu=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\resume.jpg')
photo1=Resu.resize((40,40),Image.ANTIALIAS)
Resu=ImageTk.PhotoImage(photo1)

forward=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\forward.jpg')
photo1=forward.resize((50,50),Image.ANTIALIAS)
forward=ImageTk.PhotoImage(photo1)

previus=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\previous.jpg')
photo1=previus.resize((50,50),Image.ANTIALIAS)
previus=ImageTk.PhotoImage(photo1)

puse=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\pause.jpg')
photo1=puse.resize((40,40),Image.ANTIALIAS)
puse=ImageTk.PhotoImage(photo1)

stope=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\stop.jpg')
photo1=stope.resize((40,40),Image.ANTIALIAS)
stope=ImageTk.PhotoImage(photo1)

qt=Image.open(r'C:\Users\Dell\Desktop\python\projects\Music_Player\Quit.png')
photo1=qt.resize((40,40),Image.ANTIALIAS)
qt=ImageTk.PhotoImage(photo1)


play=Button(root,text='Play Song',image=play1,bd=0,bg='#FFFFFF',font=('Courier',11),command=play_song)
canvas1.create_window(200,150,window=play)

pause=Button(root,text='pause',bd=0,bg='#FFFFFF',image=puse,command=pause_song)
canvas1.create_window(330,150,window=pause)

resume=Button(root,text='Resume song',bd=0,bg='#FFFFFF',image=Resu,command=Unpause_song)
canvas1.create_window(70,150,window=resume)

stop=Button(root,text='Stop Song',bd=0,bg='#FFFFFF',image=stope,font=('Courier',11),command=Stop_song)
canvas1.create_window(25,150,window=stop)

next=Button(root,text='Next Song',image=forward,bg='#FFFFFF',bd=0,command=Next_Song)
canvas1.create_window(280,150,window=next)

previous=Button(root,text='Previous Song',bd=0,bg='#FFFFFF',image=previus,command=Previous_Song)
canvas1.create_window(120,150,window=previous)

quit=Button(root,text='quit',bd=0,bg='#FFFFFF',image=qt,command=exit)
canvas1.create_window(375,150,window=quit)

root.mainloop()
