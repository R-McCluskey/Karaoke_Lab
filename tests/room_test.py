
import unittest

from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("dance", 3, 15)
        self.room2 = Room("jazz", 15, 25)
        self.room3 = Room("hiphop", 25, 7)
        self.room4 = Room("80s", 40, 20)
        self.guest1 = Guest("Ryan", 100.00, "Cole World")
        self.guest2 = Guest("Ibriahim", 200.00, "Without Me")
        self.guest3 = Guest("John", 70.00, "Dancing Queen")
        self.guest4 = Guest("Sarah", 15.00, "Sunshine")


    def test_guest_checks_in_to_room(self):
        self.room1.check_into_room(self.guest1)
        self.assertEqual("Ryan", self.room1.guestlist[0].name)

    def test_guest_checks_out_of_room(self):
        self.room1.check_into_room(self.guest1)
        self.room1.check_out_of_room(self.guest1)
        self.assertEqual(0, len(self.room1.guestlist))

    def test_if_room_is_full_and_guest_tries_to_join(self):
        self.room1.check_into_room(self.guest1)
        self.room1.check_into_room(self.guest2)
        self.room1.check_into_room(self.guest3)
        self.room1.check_into_room(self.guest4)
        self.assertEqual(3, len(self.room1.guestlist))

    def test_if_guess_has_enough_cash_to_join_a_room(self):
        self.room2.check_into_room(self.guest4)
        self.assertEqual(0, len(self.room2.guestlist))

    def test_guest_fave_song_in_room(self):
        self.room3.add_song("Without Me")
        self.assertEqual(self.guest2.fave, self.room3.songlist[0])




