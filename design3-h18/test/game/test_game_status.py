import unittest
import json
from atlas.game.game_status import GameStatus
from atlas.game.initial_game_status import STARTING_SCHEMA

A_KEY = "A key"
A_VALUE = "A value"


class GameStatusTest(unittest.TestCase):

    def setUp(self):
        self.gameStatus = GameStatus()

    def test_givenEmptyGameStatus_whenGettingJson_thenReturnInitialGameStatus(self):
        game_status = self.gameStatus.to_json()

        self.assertEqual(json.dumps(STARTING_SCHEMA), game_status)

    def test_whenSettingItem_thenItemIsAddedToContentDictionary(self):
        self.gameStatus[A_KEY] = A_VALUE

        self.assertEqual(A_VALUE, self.gameStatus.content[A_KEY])


if __name__ == '__main__':
    unittest.main()
