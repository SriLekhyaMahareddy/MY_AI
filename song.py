from pygame import mixer
mixer.init()
def play_song(path):

    mixer.music.load(path)
    mixer.music.play()
    mixer.music.set_volume(0.5)
    
def controller(inp):
    if(inp == "stop"):
        mixer.music.stop()
    elif(inp == "pause"):
        mixer.music.pause()
    elif(inp == "unpause"):
        mixer.music.unpause()
        #exit()
    elif(inp=="play"):
        mixer.music.play()
if __name__=="__main__":

    print("i am inside song.py")

if __name__ == "song":
    print("song is imported")

