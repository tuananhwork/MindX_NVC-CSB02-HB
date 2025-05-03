class MP3Player:
    def __init__(self):
        self.music_queue = []
        self.current_song = None

    def add_song(self, song):
        self.music_queue.append(song)
        print(f'Added {song} to the queue')

    def play_next_song(self):
        if self.music_queue:
            self.current_song = self.music_queue.pop(0)
            print(f'Now playing: {self.current_song}')
        else:
            print('No more songs in the queue')
            
    def skip_song(self):
        if self.music_queue:
            self.current_song = self.music_queue.pop(0)
            print(f'Skipping to: {self.current_song}')
        else:
            print('No more songs in the queue')
            
mp3player = MP3Player()
mp3player.add_song('Am tham ben em')
mp3player.add_song('See you again')
mp3player.add_song('Em khong phai la ai')
mp3player.play_next_song()
mp3player.skip_song()
mp3player.play_next_song()
            
