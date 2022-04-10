import imp
import unittest
from Vote import Vote

class TestVote(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestVote, self).__init__(*args, **kwargs)
        self.vote1 = Vote(1, 1)
        self.vote2 = Vote(-1, 1)
        self.vote3 = Vote(1, 0.5)
        self.vote4 = Vote(-1, 0.5)
    
    def testGetVote(self):
        self.assertEqual(self.vote1.getVote, 1)
        self.assertEqual(self.vote2.getVote, -1)

    def testGetCost(self):
        self.assertEqual(self.vote1.getVote, 1)
        self.assertEqual(self.vote3.getVote, 0.5)
        
    def testGetVoteCount(self):
        self.assertEqual(self.vote1.getVote, 1)
        self.assertEqual(self.vote2.getVote, -1)
        self.assertEqual(self.vote3.getVote, 0.5)

if __name__ == '__main__':
    unittest.main()