

class Room:
    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.guestlist =[]
        self.songlist = []
        self.price = price

    def check_into_room(self,guest):
        if guest.cash >= self.price:
            if len(self.guestlist) < self.capacity:
                 self.guestlist.append(guest)


    def check_out_of_room(self, guest):
        self.guestlist.remove(guest)

    def add_song(self,song):
        self.songlist.append(song)

    def fave_song(self, fave):
        for song in self.songlist:
            if song.title == fave:
                return "Whoo"
    
    

    
