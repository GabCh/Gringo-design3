import unittest

from atlas.game.Cube import CubeColour
import atlas.game.competitionFlagRepository as competitionFlagRepository


class CompetitionFlagRepositoryTest(unittest.TestCase):
    SOME_COUNTRY_CODE = 61

    def setUp(self):
        self.repository = competitionFlagRepository.CompetitionFlagRepository()

    def test_whenGettingFlag_thenFlagElementsAreCorrectlyMappedToEnum(self):
        expected_pattern = competitionFlagRepository.FLAGS[str(self.SOME_COUNTRY_CODE)]["pattern"]

        flag = self.repository.get_flag(self.SOME_COUNTRY_CODE)

        for i, row in enumerate(flag.pattern):
            self.assertEqual(expected_pattern[i],
                             [CubeColour.to_string(x) for x in row])

