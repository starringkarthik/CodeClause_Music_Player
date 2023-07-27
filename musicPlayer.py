from tkinter import *
import pygame
import os

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("MUSIC PLAYER")
    self.root.geometry("320x460")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    trackframe = LabelFrame(self.root,text=" Music Player ",font=("arial",12,"bold"),bg="black",fg="green",bd=9,relief=GROOVE)
    trackframe.place(x=0,y=0,width=320,height=360)
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("arial",11,"bold"),bg="green",fg="#B0FC38").grid(row=0,column=0,padx=10,pady=5)
    trackstatus = Label(trackframe,textvariable=self.status,font=("arial",12,"bold"),bg="green",fg="#B0FC38").grid(row=0,column=1,padx=10,pady=5)

    songsframe = LabelFrame(self.root,text=" Playlist ",font=("arial",12,"bold"),bg="black",fg="green",bd=9,relief=GROOVE)
    songsframe.place(x=0,y=100,width=320,height=340)
    scroll_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="#B0FC38",selectmode=SINGLE,font=("arial",12,"bold"),bg="green",fg="black",bd=5)   
    scroll_y.config(command=self.playlist.yview)
    scroll_y.pack(side=RIGHT)
    self.playlist.pack(fill=BOTH)
    os.chdir("X:\\Music\\")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END,track)
    
    buttonframe = LabelFrame(self.root,text=" Control Panel ",font=("arial",12,"bold"),bg="black",fg="green",bd=9,relief=GROOVE)
    buttonframe.place(x=0,y=340,width=320,height=120)
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=13,height=1,font=("arial",13,"bold"),fg="black",bg="red").grid(row=0,column=0,padx=5,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=13,height=1,font=("arial",13,"bold"),fg="black",bg="red").grid(row=1,column=0,padx=5,pady=5)
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=13,height=1,font=("arial",13,"bold"),fg="black",bg="red").grid(row=1,column=1,padx=5,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=13,height=1,font=("arial",13,"bold"),fg="black",bg="red").grid(row=0,column=1,padx=5,pady=5)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("...Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def stopsong(self):
    self.status.set("...Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    self.status.set("...Paused")
    pygame.mixer.music.pause()

  def unpausesong(self):
    self.status.set("...Playing")
    pygame.mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()