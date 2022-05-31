import vlc
import os
cwd = os.getcwd()
p = vlc.MediaPlayer(r"C:\Users\kayde\Downloads\natoriousthugs.mp3")
p.play()
print("Path at terminal when executing this file")
print(os.getcwd() + "\n")
while True:
    pass