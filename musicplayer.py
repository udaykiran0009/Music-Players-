from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer

pygame.mixer.init()
window=Tk()
window.geometry("500x300")
window.resizable(0,0)

paused = 1

#command for pause button
def Pause():
    global paused
    # pass
    if(paused % 2 !=0):
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    paused = paused + 1


#command for Next Button
def Next():
    nxt_song=song_box.curselection() #getting selected song  #song return a tupple (index,)
    nxt_song = nxt_song[0] + 1 #getting index of nxt song
    song = song_box.get(nxt_song)
    pygame.mixer.music.load(song)#load and play
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0,END) #clear Active Bar
    song_box.activate(nxt_song) # Activate new song bar(underline)
    song_box.select_set(nxt_song,last=None) # Activate new song bar(Active Box)


#command for Previous Button
def Previous():
    prv_song = song_box.curselection()  # getting selected song  #song return a tupple (index,)
    prv_song = prv_song[0] - 1  # getting index of Prevoius song
    song = song_box.get(prv_song)
    pygame.mixer.music.load(song)  # load and play
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)  # clear Active Bar
    song_box.activate(prv_song)  # Activate new song bar(underline)
    song_box.select_set(prv_song, last=None) # Activate new song bar(Active Box)
    #pass

#command for stop Button
def Stop():
    pygame.mixer.music.stop()

#command for play button
def Play():
    song=song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#command for Add_Many_songs
def Add_many_songs():
    songs=filedialog.askopenfilenames(title="Choose more then one song",filetypes=(("Mp3",".mp3"),("All",".*")))
    #adding songs through for loop
    for song in songs:
        song_box.insert(END, song)

#command for Remove Selected Song
def Remove_one_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

#command for Remove All Songs
def Remove_All_Songs():
    song_box.delete(0,END)
    pygame.mixer.music.stop()


#command for adding one song
def Add_one_song():
    song=filedialog.askopenfilename(title="choose a song",filetypes=(("Mp3",".mp3"),("All",".*")))
    song_box.insert(END,song)


#creating list box
song_box=Listbox(window,bg="black",fg="white",width=60,selectforeground="black")

#creating player controling buttons
nxt_button=Button(window,text='Next',fg='red',bg='black',activebackground='black',activeforeground='red',command=Next, width=8, font=('Arial Black', 12)) #forward Button

Prv_button=Button(window,text='Previous',fg='red',bg='black',activebackground='black',activeforeground='red',command=Previous, width=8, font=('Arial Black', 12)) #backward Button

play_button=Button(window,text='play',fg='green',bg='black',activebackground='black',activeforeground='green',command=Play, width=9, font=('Arial Black', 12)) #play Button

pause_button=Button(window,text='pause/play',fg='green',bg='black',activebackground='black',activeforeground='green',command=Pause, width=8, font=('Arial Black', 11)) #pause Button

stop_button=Button(window,text='stop',fg='green',bg='black',activebackground='black',activeforeground='green',command=Stop, width=8, font=('Arial Black', 12)) #stop Button

#adding add and remove menu
main_menu=Menu(window) #creating main menu
Add_Songs_menu = Menu(main_menu) #creating add menu
Remove_Songs_menu = Menu(main_menu) #creating remove menu

main_menu.add_cascade(label="Add Songs",menu=Add_Songs_menu) #addind Add songs menu to main menu
main_menu.add_cascade(label="Remove songs",menu=Remove_Songs_menu) #adding remove Songs menu to main menu

#adding options to Add Songs Menu
Add_Songs_menu.add_command(label="Add one song",command=Add_one_song)
Add_Songs_menu.add_command(label="Add more than one songs",command=Add_many_songs)

#adding options to Remove Songs Menu
Remove_Songs_menu.add_command(label="Remove selected song",command=Remove_one_song)
Remove_Songs_menu.add_command(label="Remove All Songs",command=Remove_All_Songs)

#placing buttons in a frame
song_box.pack(pady=20)
Prv_button.place(x=60,y=200)
play_button.place(x=160,y=200)
pause_button.place(x=270,y=200)
nxt_button.place(x=370,y=200)
stop_button.place(x=160,y=245)

window.config(menu=main_menu)
window.mainloop()