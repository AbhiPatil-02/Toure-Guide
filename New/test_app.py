import unittest
from data_manager import add_place, fetch_place

class TestDataManager(unittest.TestCase):
    def test_add_and_fetch(self):
        add_place("testcity", "Testland", "abc", "xyz hotel", "desc", "img.png")
        place = fetch_place("testcity")
        self.assertIsNotNone(place)
        self.assertEqual(place[1], "testcity")
