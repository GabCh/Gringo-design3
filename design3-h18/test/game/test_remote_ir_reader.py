import unittest

from atlas.communication.remote.remote_ir_reader import RemoteIrReader


class RemoteIrReaderTest(unittest.TestCase):
    def setUp(self):
        self.remote_ir_reader = RemoteIrReader(None)

    def test_whenCalculatingMajorityVote_thenReturnMostFrequentEntry(self):
        codes = [0, 0, 0, 1, 0, 5]
        expected_majority = 0

        majority = self.remote_ir_reader._majority_vote(codes)

        self.assertEqual(expected_majority, majority)
