import unittest
from services.votes import Votes


class TestVotes(unittest.TestCase):

    def test_remove_empty(self):
        votelist=[['1','2'],['0','0'],['2','1']]
        votes=Votes(votelist,1,2)
        votes._remove_empty()
        self.assertEqual(votes._votes, [['1','2'],['2','1']])

    def test_correct_winners(self):
        votelist=[]
        for i in range(26):
            votelist.append(['1','3','2'])
        for i in range(5):
            votelist.append(['1','2','3'])
        for i in range(9):
            votelist.append(['2','1','3'])
        for i in range(5):
            votelist.append(['3','1','2'])
        votes=Votes(votelist, 2, 3)
        winners = votes.stv_result().get_winners()
        self.assertEqual((winners[0].__str__(),winners[1].__str__()), ('1', '3'))
