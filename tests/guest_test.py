import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):


    def setUp(self):
        self.guest1 = Guest("Ryan", 100.00, "Cole World")
        self.guest2 = Guest("Ibrahim", 200.00, "Without Me")
        self.guest3 = Guest("John", 70.00, "Raining Men")
        self.guest4 = Guest("Sarah", 20.00, "Sunshine")

   

    # def test_guest_checks_in_to_room(self):
    #     self.assertEqual("Ryan", self.room1)
