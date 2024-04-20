class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song (self):
        for line in range(0, len((self.lyrics))):
            print(self.lyrics[line])

def main():
    stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
    stairway.sing_me_a_song()

if __name__=="__main__":
    main()