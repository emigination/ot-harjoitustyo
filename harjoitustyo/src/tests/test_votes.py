import unittest
from votes import Votes


class TestVotes(unittest.TestCase):

    def test_correct_winners(self):
        votelist=[]
        for i in range(26):
            votelist.append([1,3,2])
        for i in range(5):
            votelist.append([1,2,3])
        for i in range(9):
            votelist.append([2,1,3])
        for i in range(5):
            votelist.append([3,1,2])
        votes=Votes(votelist, 2, 3)
        winners = votes.stv_result().get_winners()
        self.assertEqual((winners[0].__str__(),winners[1].__str__()), ('3', '1'))
