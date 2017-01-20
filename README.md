DEPENDENCIES
----

Python 3.x
python3-tk
ffmpeg
pip3 install --upgrade google-api-python-client ffmpy

Though not technically a requirement, you'll need OBS for this to be worth anything

INSTRUCTIONS
----

The absolute worse part of setting this up is getting your client_secrets.json file setup correctly. 
Scroll down to AUTHORIZATION for setting that up.

By default, POC expects F2 and F3 to be your start recording/stop recording keys respectively. You can edit the key in gui_support.py (just seach for F2 and F3)

Edit gui_support.py's VIDEO_PATH variable to be the same as your recording path in OBS (it's the second line)

Put your images for the characters in poc/images/p1-characters and poc/images/p2-characters

By default, the program expects the images to be named the following:

| Image Name|
|------------|
|Bayonetta.png|
|Bowser-Jr.png|
|Bowser.png|
|Captain-Falcon.png|
|Charizard.png|
|Cloud.png|
|Corrin.png|
|Dark-Pit.png|
|Diddy-Kong.png|
|Doctor-Mario.png|
|Donkey-Kong.png|
|Duck-Hunt.png|
|Falco.png|
|Fox.png|
|Game_Watch.png|
|Ganondorf.png|
|Greninja.png|
|Ike.png|
|Jiggly.png|
|King-Dedede.png|
|Kirby.png|
|Link.png|
|Little-Mac.png|
|Lucario.png|
|Lucas.png|
|Lucina.png|
|Luigi.png|
|Mario.png|
|Marth.png|
|Megaman.png|
|Meta-Knight.png|
|Mewtwo.png|
|MiiBrawler.png|
|MiiGunner.png|
|MiiSwordfighter.png|
|Ness.png|
|Olimar.png|
|Pacman.png|
|Palutena.png|
|Peach.png|
|Pikachu.png|
|Pit.png|
|Robin.png|
|R.O.B.png|
|Rosalina.png|
|Roy.png|
|Ryu.png|
|Samus.png|
|Sheik.png|
|Shulk.png|
|Sonic.png|
|Toon-Link.png|
|Villager.png|
|Wario.png|
|WiiFit.png|
|Yoshi.png|
|Zelda.png|
|Zero-Suit-Samus.png|

You can edit these names in gui_support.py if you'd like.

AUTHORIZATION
----

The package includes a default client_secrets.json file. If you plan to make a heavy use of the script, please create and use your own OAuth 2.0 file, it's a free service. Steps:

IMPORTANT
======
**If ANYONE gets your client_secrets.json file they can upload anything they want to your channel!**

1. Go to the Google console.
2. Create project.
3. Side menu: APIs & auth -> APIs
4. Top menu: Enabled API(s): Enable Youtube data APIs.
5. Side menu: APIs & auth -> Credentials.
6. Create a Client ID: Add credentials -> OAuth 2.0 Client ID -> Other -> Name: potassium-obs-controller -> Create -> OK
7. Edit the client_secrets-sample.json file for your client_id and client_secret
8. Rename the client_secrets-sample.json file to client_secrets.json

Note:

The first time you run the program, a browser will pop up informing you that you're trying to authorize Potassium OBS Controller to access your youtube. Just follow the prompts and make sure you choose the correct account that you want the program to upload too.

