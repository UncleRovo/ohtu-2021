import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
        
    def test_search(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        
    def test_tyhjapelaaja(self):
        player = self.statistics.search("Turri")
        self.assertEqual(player, None)
        
    def test_haetiiminnimella(self):
        playerlist = self.statistics.team("EDM")
        self.assertTrue(len(playerlist) == 3)
        
    def test_topscoretesti(self):
        parhaat = self.statistics.top_scorers(2)
        self.assertTrue(parhaat[0].name == "Gretzky")
