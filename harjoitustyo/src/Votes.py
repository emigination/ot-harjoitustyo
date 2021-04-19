from harjoitustyo.src.Candidate import Candidate
import math

class Votes:

    def __init__(self, votesList, seats):
        self.votesList=votesList
        self.seats=seats
        self.candidates=[]

    def _remove_invalid(self):
        invalid=[]
        for i in range(len(self.votesList)):
            if max(self.votesList[i])<=0:
                invalid.append(i)
        for i in invalid:
            self.votesList.pop(i)

    def stv_result(self):
        elected=0
        for i in range(self.seats):
            self.candidates.append(Candidate())
        self._remove_invalid()
        # print(self.votesList)
        droopQuota=math.floor(len(self.votesList)/(self.seats+1)+1)
        # print(droopQuota)
        for voter in self.votesList:
            vote=voter[0]
            candidate=self.candidates[vote]
            candidate.votes+=1
            if candidate.votes>=droopQuota:
                candidate.elected=True
                elected+=1
            while self.seats>elected:
                for candidate in self.candidates:
                    if candidate.selected:
                        candidate.surplus=(candidate.votes-droopQuota)/candidate.votes
                for i in range(self.candidates-1):
                    for voter in self.votesList:
                        if voter[i].elected:
                            voter[i+1]