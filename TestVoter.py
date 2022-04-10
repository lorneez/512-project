import unittest

from Voter import Voter
from Vote import Vote

class TestVoter(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestVoter, self).__init__(*args, **kwargs)
        self.normalYes = Voter("Normal-Yes")
        self.normalNo = Voter("Normal-No")
        self.badYes = Voter("Bad-Yes")
        self.badNo = Voter("Bad-No")

    def testGetType(self):
        self.assertEqual(self.normalYes.getType, "Normal-Yes")
        self.assertEqual(self.normalNo.getType, "Normal-No")
        self.assertEqual(self.badYes.getType, "Bad-Yes")
        self.assertEqual(self.badNo.getType, "Bad-No")

    def testGetVotes(self):
        self.assertEqual(self.normalYes.getVotes, Vote(1,1))
        self.assertEqual(self.normalNo.getVotes, Vote(-1,1))
        self.assertEqual(self.badYes.getVotes, Vote(1,1))
        self.assertEqual(self.badNo.getVotes, Vote(-1,1))


if __name__ == '__main__':
    unittest.main()