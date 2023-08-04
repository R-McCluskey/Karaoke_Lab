import unittest
from src.song import Song
from src.room import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Eminem", "Without Me")
        self.song2 = Song("Hardwell", "Spaceman")
        self.song3 = Song("ABBA", "Dancing Queen")
        self.song4 = Song("RP", "Boogie nights")
        self.songlist = []
        self.room3 = Room("hiphop", 25, 7)

    def test_song_added(self):
        self.room3.add_song(self.song1)
        self.assertEqual("Without Me", self.room3.songlist[0].title)