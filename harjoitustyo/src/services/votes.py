import pyrankvote
from pyrankvote import Candidate, Ballot
from pyrankvote.helpers import CompareMethodIfEqual


class Votes:

    def __init__(self, votes, seats, ncandidates):
        self._votes = votes
        self._ncandidates = ncandidates
        self._seats = seats

    def _check_correct_characters(self):
        for vote in self._votes:
            for choice in vote:
                if choice=='':
                    continue
                if not choice.isnumeric() or int(choice)<0:
                    self._errors.append("Syötetty valinta ei ole positiivinen kokonaisluku")
                    return

    def _check_correct_numbers(self):
        for vote in self._votes:
            for choice in vote:
                if choice.isnumeric() and int(choice)>self._ncandidates:
                    self._errors.append("Syötetty numero ei vastaa ketään ehdokasta")
                    return

    def _check_all_different(self):
        for vote in self._votes:
            numbers=set()
            for number in vote:
                if number.isnumeric() and number in numbers:
                    self._errors.append("Sama ehdokas kaksi kertaa yhdessä äänessä")
                    return
                numbers.add(number)

    def _check_seats_number(self):
        if not self._seats.isnumeric() or int(self._seats)<=0:
            self._errors.append("Valittavien määrä ei ole positiivinen kokonaisluku")
            return
        elif int(self._seats)>self._ncandidates:
            self._errors.append("Valittavien määrä on suurempi tai yhtä suuri kuin ehdokkaiden")

    def check_validity(self):
        self._errors=[]
        self._check_correct_characters()
        self._check_correct_numbers()
        self._check_all_different()
        self._check_seats_number()
        return self._errors

    def _remove_empty(self):
        empty = []
        for i in range(len(self._votes)):
            isEmpty=True
            for choice in self._votes[i]:
                if choice!='' and choice!='0':
                    isEmpty=False
                    break
            if isEmpty:
                empty.append(i)
        number=0
        for i in empty:
            self._votes.pop(i-number)
            number += 1

    def stv_result(self):
        self._remove_empty()
        candidates = []
        for i in range(self._ncandidates):
            candidates.append(Candidate(str(i+1)))
        ballots = []
        for i in range(len(self._votes)):
            lst = []
            for vote in self._votes[i]:
                if vote == '0':
                    continue
                lst.append(candidates[int(vote)-1])
            ballots.append(Ballot(ranked_candidates=lst))
        election_result = pyrankvote.single_transferable_vote(
            candidates,ballots,int(self._seats),
            compare_method_if_equal=CompareMethodIfEqual.MostSecondChoiceVotes,
            pick_random_if_blank=False
        )
        return election_result

    #     elected=0
    #     for i in range(self.seats):
    #         self.ncandidates.append(Candidate())
    #     self._remove_empty()
    #     droopQuota=math.floor(len(self.votes_list)/(self.seats+1)+1)
    #     for voter in self.votes_list:
    #         vote=voter[0]
    #         candidate=self.ncandidates[vote]
    #         candidate.votes+=1
    #         if candidate.votes>=droopQuota:
    #             candidate.elected=True
    #             elected+=1
    #         while self.seats>elected:
    #             for candidate in self.ncandidates:
    #                 if candidate.selected:
    #                     candidate.surplus=(candidate.votes-droopQuota)/candidate.votes
    #             for i in range(self.ncandidates-1):
    #                 for voter in self.votes_list:
    #                     if voter[i].elected:
    #                         voter[i+1]
