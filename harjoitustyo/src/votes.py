import pyrankvote
from pyrankvote import Candidate, Ballot
from pyrankvote.helpers import CompareMethodIfEqual


class Votes:

    def __init__(self, votes, seats, ncandidates):
        self._votes = votes
        self._votes_list = []
        self._ncandidates = ncandidates
        self._seats = seats

    def check_validity(self):
        for i in range(len(self._votes)):
            self._votes_list.append([])
            for j in range(self._ncandidates):
                vote = self._votes[i][j]
                if vote == '':
                    vote = '0'
                if vote.isnumeric() and int(vote) >= 0 and int(vote) <= self._ncandidates:
                    self._votes_list[i].append(vote)
                else:
                    return False
        return True

    def _remove_empty(self):
        empty = []
        for i in range(len(self._votes_list)):
            if max(self._votes_list[i]) == 0:
                empty.append(i)
        number = 0
        for i in empty:
            self._votes_list.pop(i-number)
            number += 1

    def stv_result(self):
        candidates = []
        for i in range(self._ncandidates):
            candidates.append(Candidate(str(i+1)))
        ballots = []
        for i in range(len(self._votes_list)):
            lst = []
            for vote in self._votes_list[i]:
                if vote == '0':
                    continue
                lst.append(candidates[int(vote)-1])
            ballots.append(Ballot(ranked_candidates=lst))
        election_result = pyrankvote.single_transferable_vote(
            candidates,ballots, self._seats,
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
