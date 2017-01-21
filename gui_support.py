#! /usr/bin/env python
VIDEO_PATH="/path/to/your/recording/directory"

import os
import sys
import subprocess
import time
import ffmpy
from shutil import copy
from lib.upload_video import *

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

argparser.add_argument("--file", required=True, help="Video file to upload")
argparser.add_argument("--title", help="Video title", default="Test Title")
argparser.add_argument("--description", help="Video description", default="Test Description")
argparser.add_argument("--category", default="20", help="Numeric video category. " + "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
argparser.add_argument("--keywords", help="Video keywords, comma separated", default="")
argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES, default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")

youtube_description = """Put the info you want in the description here
You can even do multiple lines"""

youtube_keywords ="Gaming,Super Smash Bros"

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global combobox
    combobox = StringVar()


    global combobox1
    combobox1 = StringVar()
    global combobox2
    combobox2 = StringVar()
    global combobox3
    combobox3 = StringVar()
    global combobox4
    combobox4 = StringVar()
    global game
    game = StringVar()


    global P1_Entry
    P1_Entry = StringVar()
    global P1T_Entry
    P1T_Entry = StringVar()
    global P2_Entry
    P2_Entry = StringVar()
    global P2T_Entry
    P2T_Entry = StringVar()
    global P3_Entry
    P3_Entry = StringVar()
    global P3T_Entry
    P3T_Entry = StringVar()
    global P4_Entry
    P4_Entry = StringVar()
    global P4T_Entry
    P4T_Entry = StringVar()
    global EventSH_Entry
    EventSH_Entry = StringVar()
    global Event_Entry
    Event_Entry = StringVar()
    global Round_Entry
    Round_Entry = StringVar()
    global P1_Wins
    P1_Wins = StringVar()
    global P2_Wins
    P2_Wins = StringVar()
    global Com1_Entry
    Com1_Entry = StringVar()
    global Com1T_Entry
    Com1T_Entry = StringVar()
    global Com2_Entry
    Com2_Entry = StringVar()
    global Com2T_Entry
    Com2T_Entry = StringVar()

def char_img(directory, character, x):
    char_dict = {
    "Bayonetta": "Bayonetta.png",
    "Bowser": "Bowser.png",
    "Bowser Jr.": "Bowser-Jr.png",
    "Captain Falcon": "Captain-Falcon.png",
    "Charizard": "Charizard.png",
    "Cloud": "Cloud.png",
    "Corrin": "Corrin.png" ,
    "Dark Pit": "Dark-Pit.png",
    "Diddy Kong": "Diddy-Kong.png",
    "Donkey Kong": "Donkey-Kong.png",
    "Dr. Mario": "Doctor-Mario.png",
    "Duck Hunt": "Duck-Hunt.png",
    "Falco": "Falco.png",
    "Fox": "Fox.png",
    "Ganondorf": "Ganondorf.png",
    "Greninja": "Greninja.png",
    "Ike": "Ike.png",
    "Jigglypuff": "Jiggly.png",
    "King Dedede": "King-Dedede.png",
    "Kirby": "Kirby.png",
    "Link": "Link.png",
    "Little Mac": "Little-Mac.png",
    "Lucario": "Lucario.png",
    "Lucas": "Lucas.png",
    "Lucina": "Lucina.png",
    "Luigi": "Luigi.png",
    "Mario": "Mario.png",
    "Marth": "Marth.png",
    "Mega Man": "Megaman.png",
    "Meta Knight": "Meta-Knight.png",
    "Mewtwo": "Mewtwo.png",
    "Mii Brawler": "MiiBrawler.png",
    "Mii Gunner": "MiiGunner.png",
    "Mii Swordfighter": "MiiSwordfighter.png",
    "Mr. Game & Watch": "Game_Watch.png",
    "Ness": "Ness.png",
    "Olimar": "Olimar.png",
    "Pac-Man": "Pacman.png",
    "Palutena": "Palutena.png",
    "Peach": "Peach.png",
    "Pikachu": "Pikachu.png",
    "Pit": "Pit.png",
    "R.O.B.": "R.O.B.png",
    "Robin": "Robin.png",
    "Rosalina & Luma": "Rosalina.png",
    "Roy": "Roy.png",
    "Ryu": "Ryu.png",
    "Samus": "Samus.png",
    "Sheik": "Sheik.png",
    "Shulk": "Shulk.png",
    "Sonic": "Sonic.png",
    "Toon Link": "Toon-Link.png",
    "Villager": "Villager.png",
    "Wario": "Wario.png",
    "Wii Fit Trainer": "WiiFit.png",
    "Yoshi": "Yoshi.png",
    "Zelda": "Zelda.png",
    "Zero Suit Samus": "Zero-Suit-Samus.png"
    }
    if (character in char_dict):
        copy("images/" + directory + '/' + char_dict[character], 'p' + x + '-char.png')



def save_info():
    eventFile = open('event.txt', 'w')
    eventFile.write(Event_Entry.get())
    eventFile.close()
    roundFile = open('round.txt', 'w')
    roundFile.write(Round_Entry.get())
    roundFile.close()
    p1Name = open('p1.txt', 'w')
    p1Name.write(P1_Entry.get())
    p1Name.close()
    p1t = open('p1-social-media.txt', 'w')
    p1t.write(P1T_Entry.get())
    p1t.close()
    p1Char = open('p1Char.txt', 'w')
    p1Char.write(combobox1.get())
    p1Char.close()
    char_img('p1-characters', combobox1.get(), '1')
    p1Wins = open('p1Wins.txt', 'w')
    p1Wins.write(P1_Wins.get())
    p1Wins.close()
    p2Name = open('p2.txt', 'w')
    p2Name.write(P2_Entry.get())
    p2Name.close()
    p2t = open('p2-social-media.txt', 'w')
    p2t.write(P2T_Entry.get())
    p2t.close()
    p2Char = open('p2Char.txt', 'w')
    p2Char.write(combobox2.get())
    p2Char.close()
    char_img('p2-characters', combobox2.get(), '2')
    p2Wins = open('p2Wins.txt', 'w')
    p2Wins.write(P2_Wins.get())
    p2Wins.close()
    p3Name = open('p3.txt', 'w')
    p3Name.write(P3_Entry.get())
    p3Name.close()
    p3Char = open('p3Char.txt', 'w')
    p3Char.write(combobox3.get())
    p3Char.close()
    p3t = open('p3-social-media.txt', 'w')
    p3t.write(P3T_Entry.get())
    p3t.close()
    p4Name = open('p4.txt', 'w')
    p4Name.write(P4_Entry.get())
    p4Name.close()
    p4Char = open('p4Char.txt', 'w')
    p4Char.write(combobox4.get())
    p4Char.close()
    p4t = open('p1-social-media.txt', 'w')
    p4t.write(P4T_Entry.get())
    p4t.close()
    com1Name = open('comm1.txt', 'w')
    com1Name.write(Com1_Entry.get())
    com1Name.close()
    com2Name = open('comm2.txt', 'w')
    com2Name.write(Com2_Entry.get())
    com2Name.close()
    titleFile = open('title.txt', 'w')
    titleText = EventSH_Entry.get() + " [" + game.get() + "] - " + P1_Entry.get() + " (" + combobox1.get() + ") vs " + P2_Entry.get() + " (" + combobox2.get() + ") - " + Round_Entry.get()
    titleLen = len(titleText)
    print(titleText)
    if (titleLen > 99):
        titleText = titleText[:99]
        titleFile.write(titleText)
    else:
        titleFile.write(titleText)
    titleFile.close()



def start_recording():
    print("pressing f2")
    subprocess.Popen(['xdotool search --name "OBS 17*" key F2'], shell=True)
    #print('gui_support.start_recording')
    #sys.stdout.flush()

def stop_recording():
    f = open('title.txt', 'r')
    newTitle = f.read()
    newName = VIDEO_PATH + "/" + newTitle + ".flv"
    f.close()
    subprocess.Popen(['xdotool search --name "OBS 17*" key F3'], shell=True)
    time.sleep(3)
    onlyfiles = [f for f in os.listdir(VIDEO_PATH) if os.path.isfile(os.path.join(VIDEO_PATH, f))]
    mtimes = [os.path.getmtime(VIDEO_PATH + '/' + f) for f in onlyfiles ]
    combine_dict = dict(zip(mtimes, onlyfiles))
    videoFileName = VIDEO_PATH + "/" + str(combine_dict[(max(combine_dict))])
    os.rename(videoFileName, newName)
    print("Uploading Video to Youtube...")
    args = argparser.parse_args(['--file', newName, '--title', newTitle, '--description', youtube_description, '--keywords', youtube_keywords ])
    youtube = get_authenticated_service(args)
    initialize_upload(youtube, args)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()
