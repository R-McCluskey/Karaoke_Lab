
class Guest:
    def __init__(self, name, cash, fave):
        self.name = name
        self.cash = cash
        self.fave = fave
        self.songlist = "Without Me"

    def room_has_favourite(self):
        if self.fave.equals(self.songlist):
            return "Whoo"



    