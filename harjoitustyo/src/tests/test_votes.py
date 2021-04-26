import unittest
from services.votes import Votes


class TestVotes(unittest.TestCase):

    def test_remove_empty(self):
        votelist = [['1', '2'], ['', ''], ['2', '1']]
        votes = Votes(votelist, '1', 2)
        votes._remove_empty()
        self.assertEqual(votes._votes, [['1', '2'], ['2', '1']])

    def test_find_nonnumber_characters_in_votes(self):
        votelist = [['1', '2'], ['1', 'w']]
        votes = Votes(votelist, '1', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Syötetty valinta ei ole positiivinen kokonaisluku")

    def test_find_negative_numbers_in_votes(self):
        votelist = [['1', '-1'], ['1', '2']]
        votes = Votes(votelist, '1', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Syötetty valinta ei ole positiivinen kokonaisluku")

    def test_ignore_empty_choices_in_validity_check(self):
        votelist = [['1', ''], ['1', '2']]
        votes = Votes(votelist, '1', 2)
        votes.check_validity()
        self.assertEqual(
            len(votes._errors), 0)

    def test_find_nonexistent_numbers(self):
        votelist = [['1', '3'], ['1', '2']]
        votes = Votes(votelist, '1', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Syötetty numero ei vastaa ketään ehdokasta")

    def test_find_double_votes(self):
        votelist = [['1', '1'], ['1', '2']]
        votes = Votes(votelist, '1', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Sama ehdokas kaksi kertaa yhdessä äänessä")

    def test_find_nonnumber_seatsnumber(self):
        votelist = [['2', '1'], ['1', '2']]
        votes = Votes(votelist, 'x', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Valittavien määrä ei ole positiivinen kokonaisluku")

    def test_find_too_large_seatsnumber(self):
        votelist = [['2', '1'], ['1', '2']]
        votes = Votes(votelist, '2', 2)
        votes.check_validity()
        self.assertEqual(
            votes._errors[0], "Valittavien määrä on suurempi tai yhtä suuri kuin ehdokkaiden")

    def test_stv_ignors_empty(self):
        votelist = [['', '2'], ['1', ''], ['1', '2']]
        votes = Votes(votelist, '1', 2)
        winners = votes.stv_result().get_winners()
        self.assertEqual(winners[0].__str__(), '1')

    def test_correct_winners(self):
        votelist = []
        for i in range(26):
            votelist.append(['1', '3', '2'])
        for i in range(5):
            votelist.append(['1', '2', '3'])
        for i in range(9):
            votelist.append(['2', '1', '3'])
        for i in range(5):
            votelist.append(['3', '1', '2'])
        votes = Votes(votelist, '2', 3)
        winners = votes.stv_result().get_winners()
        self.assertEqual(
            (winners[0].__str__(), winners[1].__str__()), ('1', '3'))
