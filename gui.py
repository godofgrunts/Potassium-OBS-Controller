#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.6
# In conjunction with Tcl version 8.6
#    Jan 17, 2017 02:32:10 PM
import sys

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

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    gui_support.set_Tk_var()
    top = Potassium_OBS_Controller (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Potassium_OBS_Controller(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    gui_support.set_Tk_var()
    top = Potassium_OBS_Controller (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Potassium_OBS_Controller():
    global w
    w.destroy()
    w = None


class Potassium_OBS_Controller:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self._bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        self._fgcolor = '#000000'  # X11 color: 'black'
        self._compcolor = '#d9d9d9' # X11 color: 'gray85'
        self._ana1color = '#d9d9d9' # X11 color: 'gray85'
        self._ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=self._bgcolor)
        self.style.configure('.',foreground=self._fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', self._compcolor), ('active',self._ana2color)])

        top.geometry("683x450+778+100")
        top.title("Potassium OBS Controller")
        top.configure(highlightcolor="black")


        self.Player1_Name = Entry(top)
        self.Player1_Name.place(relx=0.03, rely=0.18, relheight=0.04, relwidth=0.21)
        self.Player1_Name.configure(background="white")
        self.Player1_Name.configure(font="TkFixedFont")
        self.Player1_Name.configure(selectbackground="#c4c4c4")
        self.Player1_Name.configure(textvariable=gui_support.P1_Entry)

        self.Player1_T = Entry(top)
        self.Player1_T.place(relx=0.03, rely=0.24, relheight=0.04, relwidth=0.21)
        self.Player1_T.configure(background="#AFEFFF")
        self.Player1_T.configure(font="TkFixedFont")
        self.Player1_T.configure(selectbackground="#c4c4c4")
        self.Player1_T.configure(textvariable=gui_support.P1T_Entry)

        self.Player1_Character = ttk.Combobox(top)
        self.Player1_Character.place(relx=0.03, rely=0.30, relheight=0.04
                , relwidth=0.22)
        self.value_list = ["","Bayonetta","Bowser","Bowser Jr.","Captain Falcon","Charizard","Cloud","Corrin","Dark Pit","Diddy Kong","Donkey Kong","Dr. Mario","Duck Hunt","Falco","Fox","Ganondorf","Greninja","Ike","Jigglypuff","King Dedede","Kirby","Link","Little Mac","Lucario","Lucas","Lucina","Luigi","Mario","Marth","Mega Man","Meta Knight","Mewtwo","Mii Brawler","Mii Gunner","Mii Swordfighter","Mr. Game & Watch","Ness","Olimar","Pac-Man","Palutena","Peach","Pikachu","Pit","R.O.B.","Robin","Rosalina & Luma","Roy","Ryu","Samus","Sheik","Shulk","Sonic","Toon Link","Villager","Wario","Wii Fit Trainer","Yoshi","Zelda","Zero Suit Samus"]
        self.Player1_Character.configure(values=self.value_list)
        self.Player1_Character.configure(textvariable=gui_support.combobox1)
        self.Player1_Character.configure(takefocus="")

        self.Player2_Name = Entry(top)
        self.Player2_Name.place(relx=0.26, rely=0.18, relheight=0.04, relwidth=0.21)
        self.Player2_Name.configure(background="white")
        self.Player2_Name.configure(font="TkFixedFont")
        self.Player2_Name.configure(selectbackground="#c4c4c4")
        self.Player2_Name.configure(textvariable=gui_support.P2_Entry)

        self.Player2_T = Entry(top)
        self.Player2_T.place(relx=0.26, rely=0.24, relheight=0.04, relwidth=0.21)
        self.Player2_T.configure(background="#AFEFFF")
        self.Player2_T.configure(font="TkFixedFont")
        self.Player2_T.configure(selectbackground="#c4c4c4")
        self.Player2_T.configure(textvariable=gui_support.P2T_Entry)

        self.Player2_Character = ttk.Combobox(top)
        self.Player2_Character.place(relx=0.26, rely=0.30, relheight=0.04
                , relwidth=0.22)
        #self.value_list = ["","Bayonetta","Bowser","Bowser Jr.","Captain Falcon","Charizard","Cloud","Corrin","Dark Pit","Diddy Kong","Donkey Kong","Dr. Mario","Duck Hunt","Falco","Fox","Ganondorf","Greninja","Ike","Jigglypuff","King Dedede","Kirby","Link","Little Mac","Lucario","Lucas","Lucina","Luigi","Mario","Marth","Mega Man","Meta Knight","Mewtwo","Mii Brawler","Mii Gunner","Mii Swordfighter","Mr. Game & Watch","Ness","Olimar","Pac-Man","Palutena","Peach","Pikachu","Pit","R.O.B.","Robin","Rosalina & Luma","Roy","Ryu","Samus","Sheik","Shulk","Sonic","Toon Link","Villager","Wario","Wii Fit Trainer","Yoshi","Zelda","Zero Suit Samus"]
        self.Player2_Character.configure(values=self.value_list)
        self.Player2_Character.configure(textvariable=gui_support.combobox2)
        self.Player2_Character.configure(takefocus="")

        self.Player3_Name = Entry(top)
        self.Player3_Name.place(relx=0.5, rely=0.18, relheight=0.04, relwidth=0.21)
        self.Player3_Name.configure(background="white")
        self.Player3_Name.configure(font="TkFixedFont")
        self.Player3_Name.configure(selectbackground="#c4c4c4")
        self.Player3_Name.configure(textvariable=gui_support.P3_Entry)

        self.Player3_T = Entry(top)
        self.Player3_T.place(relx=0.5, rely=0.24, relheight=0.04, relwidth=0.21)
        self.Player3_T.configure(background="#AFEFFF")
        self.Player3_T.configure(font="TkFixedFont")
        self.Player3_T.configure(selectbackground="#c4c4c4")
        self.Player3_T.configure(textvariable=gui_support.P3T_Entry)

        self.Player3_Character = ttk.Combobox(top)
        self.Player3_Character.place(relx=0.5, rely=0.30, relheight=0.04
                , relwidth=0.22)
        #self.value_list = ["","Bayonetta","Bowser","Bowser Jr.","Captain Falcon","Charizard","Cloud","Corrin","Dark Pit","Diddy Kong","Donkey Kong","Dr. Mario","Duck Hunt","Falco","Fox","Ganondorf","Greninja","Ike","Jigglypuff","King Dedede","Kirby","Link","Little Mac","Lucario","Lucas","Lucina","Luigi","Mario","Marth","Mega Man","Meta Knight","Mewtwo","Mii Brawler","Mii Gunner","Mii Swordfighter","Mr. Game & Watch","Ness","Olimar","Pac-Man","Palutena","Peach","Pikachu","Pit","R.O.B.","Robin","Rosalina & Luma","Roy","Ryu","Samus","Sheik","Shulk","Sonic","Toon Link","Villager","Wario","Wii Fit Trainer","Yoshi","Zelda","Zero Suit Samus"]
        self.Player3_Character.configure(values=self.value_list)
        self.Player3_Character.configure(textvariable=gui_support.combobox3)
        self.Player3_Character.configure(takefocus="")

        self.Player4_Name = Entry(top)
        self.Player4_Name.place(relx=0.75, rely=0.18, relheight=0.04, relwidth=0.21)
        self.Player4_Name.configure(background="white")
        self.Player4_Name.configure(font="TkFixedFont")
        self.Player4_Name.configure(selectbackground="#c4c4c4")
        self.Player4_Name.configure(textvariable=gui_support.P4_Entry)

        self.Player4_T = Entry(top)
        self.Player4_T.place(relx=0.75, rely=0.24, relheight=0.04, relwidth=0.21)
        self.Player4_T.configure(background="#AFEFFF")
        self.Player4_T.configure(font="TkFixedFont")
        self.Player4_T.configure(selectbackground="#c4c4c4")
        self.Player4_T.configure(textvariable=gui_support.P4T_Entry)

        self.Player4_Character = ttk.Combobox(top)
        self.Player4_Character.place(relx=0.75, rely=0.30, relheight=0.04
                , relwidth=0.22)
        #self.value_list = ["","Bayonetta","Bowser","Bowser Jr.","Captain Falcon","Charizard","Cloud","Corrin","Dark Pit","Diddy Kong","Donkey Kong","Dr. Mario","Duck Hunt","Falco","Fox","Ganondorf","Greninja","Ike","Jigglypuff","King Dedede","Kirby","Link","Little Mac","Lucario","Lucas","Lucina","Luigi","Mario","Marth","Mega Man","Meta Knight","Mewtwo","Mii Brawler","Mii Gunner","Mii Swordfighter","Mr. Game & Watch","Ness","Olimar","Pac-Man","Palutena","Peach","Pikachu","Pit","R.O.B.","Robin","Rosalina & Luma","Roy","Ryu","Samus","Sheik","Shulk","Sonic","Toon Link","Villager","Wario","Wii Fit Trainer","Yoshi","Zelda","Zero Suit Samus"]
        self.Player4_Character.configure(values=self.value_list)
        self.Player4_Character.configure(textvariable=gui_support.combobox4)
        self.Player4_Character.configure(takefocus="")

        self.Player1_Wins = Spinbox(top, from_=0.0, to=100.0)
        self.Player1_Wins.place(relx=0.15, rely=0.4, relheight=0.06
                , relwidth=0.21)
        self.Player1_Wins.configure(activebackground="#f9f9f9")
        self.Player1_Wins.configure(background="white")
        self.Player1_Wins.configure(from_="0.0")
        self.Player1_Wins.configure(highlightbackground="black")
        self.Player1_Wins.configure(selectbackground="#c4c4c4")
        self.Player1_Wins.configure(textvariable=gui_support.P1_Wins)
        self.Player1_Wins.configure(to="100.0")
        self.Player1_Wins.configure(width=98)

        self.Player2_Wins = Spinbox(top, from_=0.0, to=100.0)
        self.Player2_Wins.place(relx=0.63, rely=0.4, relheight=0.06
                , relwidth=0.21)
        self.Player2_Wins.configure(activebackground="#f9f9f9")
        self.Player2_Wins.configure(background="white")
        self.Player2_Wins.configure(from_="0.0")
        self.Player2_Wins.configure(highlightbackground="black")
        self.Player2_Wins.configure(selectbackground="#c4c4c4")
        self.Player2_Wins.configure(textvariable=gui_support.P2_Wins)
        self.Player2_Wins.configure(to="100.0")
        self.Player2_Wins.configure(width=98)

        self.Com1 = Entry(top)
        self.Com1.place(relx=0.15, rely=0.53, relheight=0.04, relwidth=0.21)
        self.Com1.configure(background="white")
        self.Com1.configure(font="TkFixedFont")
        self.Com1.configure(selectbackground="#c4c4c4")
        self.Com1.configure(textvariable=gui_support.Com1_Entry)

        self.Com1T = Entry(top)
        self.Com1T.place(relx=0.15, rely=0.59, relheight=0.04, relwidth=0.21)
        self.Com1T.configure(background="#AFEFFF")
        self.Com1T.configure(font="TkFixedFont")
        self.Com1T.configure(selectbackground="#c4c4c4")
        self.Com1T.configure(textvariable=gui_support.Com1T_Entry)

        self.Com2 = Entry(top)
        self.Com2.place(relx=0.63, rely=0.53, relheight=0.04, relwidth=0.21)
        self.Com2.configure(background="white")
        self.Com2.configure(font="TkFixedFont")
        self.Com2.configure(selectbackground="#c4c4c4")
        self.Com2.configure(textvariable=gui_support.Com2_Entry)

        self.Com2T = Entry(top)
        self.Com2T.place(relx=0.63, rely=0.59, relheight=0.04, relwidth=0.21)
        self.Com2T.configure(background="#AFEFFF")
        self.Com2T.configure(font="TkFixedFont")
        self.Com2T.configure(selectbackground="#c4c4c4")
        self.Com2T.configure(textvariable=gui_support.Com2T_Entry)

        self.Save = Button(top)
        self.Save.place(relx=0.04, rely=0.67, height=26, width=121)
        self.Save.configure(activebackground="#d9d9d9")
        self.Save.configure(command=gui_support.save_info)
        self.Save.configure(text='''Save''')

        self.Start = Button(top)
        self.Start.place(relx=0.04, rely=0.75, height=26, width=121)
        self.Start.configure(activebackground="#d9d9d9")
        self.Start.configure(command=gui_support.start_recording)
        self.Start.configure(text='''Start Recording''')

        self.Stop = Button(top)
        self.Stop.place(relx=0.79, rely=0.75, height=26, width=119)
        self.Stop.configure(activebackground="#d9d9d9")
        self.Stop.configure(command=gui_support.stop_recording)
        self.Stop.configure(text='''Stop Recording''')

        self.Event_Text = Entry(top)
        self.Event_Text.place(relx=0.03, rely=0.07, relheight=0.04
                , relwidth=0.21)
        self.Event_Text.configure(background="white")
        self.Event_Text.configure(font="TkFixedFont")
        self.Event_Text.configure(selectbackground="#c4c4c4")
        self.Event_Text.configure(textvariable=gui_support.Event_Entry)

        self.EventSH_Text = Entry(top)
        self.EventSH_Text.place(relx=0.26, rely=0.07, relheight=0.04
                , relwidth=0.21)
        self.EventSH_Text.configure(background="white")
        self.EventSH_Text.configure(font="TkFixedFont")
        self.EventSH_Text.configure(selectbackground="#c4c4c4")
        self.EventSH_Text.configure(textvariable=gui_support.EventSH_Entry)

        self.Round = Entry(top)
        self.Round.place(relx=0.5, rely=0.07, relheight=0.04, relwidth=0.21)
        self.Round.configure(background="white")
        self.Round.configure(font="TkFixedFont")
        self.Round.configure(selectbackground="#c4c4c4")
        self.Round.configure(textvariable=gui_support.Round_Entry)

        self.Game_Box = ttk.Combobox(top)
        self.Game_Box.place(relx=0.75, rely=0.07, relheight=0.04
                , relwidth=0.22)
        self.game_list = ["64", "Melee", "Brawl", "PM", "Wii U", "Other"]
        self.Game_Box.configure(values=self.game_list)
        self.Game_Box.configure(textvariable=gui_support.game)
        self.Game_Box.configure(takefocus="")

###############################################################################
################## Above this is the order for tabbing ########################
###############################################################################

        self.Player1 = Label(top)
        self.Player1.place(relx=0.1, rely=0.13, height=18, width=52)
        self.Player1.configure(activebackground="#f9f9f9")
        self.Player1.configure(text='''Player 1''')

        self.Player2 = Label(top)
        self.Player2.place(relx=0.34, rely=0.13, height=18, width=52)
        self.Player2.configure(activebackground="#f9f9f9")
        self.Player2.configure(text='''Player 2''')

        self.Player_3 = Label(top)
        self.Player_3.place(relx=0.57, rely=0.13, height=18, width=52)
        self.Player_3.configure(activebackground="#f9f9f9")
        self.Player_3.configure(text='''Player 3''')

        self.Player4 = Label(top)
        self.Player4.place(relx=0.82, rely=0.13, height=18, width=52)
        self.Player4.configure(activebackground="#f9f9f9")
        self.Player4.configure(text='''Player 4''')

        self.Event1 = Label(top)
        self.Event1.place(relx=0.087, rely=0.02, height=18, width=78)
        self.Event1.configure(activebackground="#f9f9f9")
        self.Event1.configure(text='''Event Name''')

        self.EventSH1 = Label(top)
        self.EventSH1.place(relx=0.32, rely=0.02, height=18, width=63)
        self.EventSH1.configure(activebackground="#f9f9f9")
        self.EventSH1.configure(text='''Shorthand''')

        self.Round1 = Label(top)
        self.Round1.place(relx=0.575, rely=0.02, height=18, width=43)
        self.Round1.configure(activebackground="#f9f9f9")
        self.Round1.configure(text='''Round''')

        self.Game1 = Label(top)
        self.Game1.place(relx=0.82, rely=0.02, height=18, width=43)
        self.Game1.configure(activebackground="#f9f9f9")
        self.Game1.configure(text='''Game''')

        self.P1_Wins = Label(top)
        self.P1_Wins.place(relx=0.165, rely=0.36, height=18, width=122)
        self.P1_Wins.configure(activebackground="#f9f9f9")
        self.P1_Wins.configure(text='''Player/Team 1 Wins''')

        self.P2_Wins = Label(top)
        self.P2_Wins.place(relx=0.645, rely=0.36, height=18, width=122)
        self.P2_Wins.configure(activebackground="#f9f9f9")
        self.P2_Wins.configure(text='''Player/Team 2 Wins''')

        self.Com1_Label = Label(top)
        self.Com1_Label.place(relx=0.18, rely=0.48, height=18, width=99)
        self.Com1_Label.configure(activebackground="#f9f9f9")
        self.Com1_Label.configure(text='''Commentator 1''')

        self.Com2_Label = Label(top)
        self.Com2_Label.place(relx=0.66, rely=0.48, height=18, width=99)
        self.Com2_Label.configure(activebackground="#f9f9f9")
        self.Com2_Label.configure(text='''Commentator 2''')






if __name__ == '__main__':
    vp_start_gui()
