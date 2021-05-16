import pyrankvote
from pyrankvote import Candidate, Ballot
from pyrankvote.helpers import CompareMethodIfEqual
from .database import Database


class Votes:
    """Luokka, joka laskee tulokset annetuista äänistä ja tarkistaa äänteen kelvollisuuden.

    Attributes:
        votes: Äänet kaksiulotteisena taulukkona, jossa rivi vastaa yhtä äänestäjää ja
            alkiot ovat ehdokkaiden numeroita äänestäjän haluamassa järjestyksessä.
        seats: Valittavien määrä.
        ncandidates: Ehdokkaiden määrä.
        errors: Lista virheistä äänissä.
    """

    def __init__(self, votes, seats, ncandidates):
        """Luokan konstruktori.

        Args:
            votes: Äänet kaksiulotteisena taulukkona, jossa rivi vastaa yhtä äänestäjää ja
            alkiot ovat ehdokkaiden numeroita äänestäjän haluamassa järjestyksessä.
            seats: Valittavien määrä.
            ncandidates: Ehdokkaiden määrä.
        """
        self._votes = votes
        self._seats = seats
        self._ncandidates = ncandidates
        self._errors = []

    def _check_correct_characters(self):
        """Tarkistaa, että syötetyt merkit ovat positiivisia kokonaislukuja. Jos kaikki
            eivät ole, virhelistaan lisätään tieto siitä.
        """
        for vote in self._votes:
            for choice in vote:
                if choice == '':
                    continue
                if not choice.isnumeric() or int(choice) < 0:
                    self._errors.append(
                        "Syötetty valinta ei ole positiivinen kokonaisluku")
                    return

    def _check_correct_numbers(self):
        """Tarkistaa, että syötetyt numerot vastaavat ehdokkaita. Jos niin ei ole,
            virhelistaan lisätään tieto siitä.
        """
        for vote in self._votes:
            for choice in vote:
                if choice.isnumeric() and int(choice) > self._ncandidates:
                    self._errors.append(
                        "Syötetty numero ei vastaa ketään ehdokasta")
                    return

    def _check_all_different(self):
        """Tarkistaa, ettei kukaan äänestäjä ole äänestänyt samaa ehdokasta
            useita kertoja. Jos on, virhelistaan lisätään tieto siitä.
        """
        for vote in self._votes:
            numbers = set()
            for number in vote:
                if number.isnumeric() and number in numbers:
                    self._errors.append(
                        "Sama ehdokas kaksi kertaa yhdessä äänessä")
                    return
                numbers.add(number)

    def _check_seats_number(self):
        """Tarkistaa, että valittavien lukumäärä on kelvollinen. Jos ei
            ole, virhelistaan lisätään tieto siitä.
        """
        if not self._seats.isnumeric() or int(self._seats) <= 0:
            self._errors.append(
                "Valittavien määrä ei ole positiivinen kokonaisluku")
        elif int(self._seats) >= self._ncandidates:
            self._errors.append(
                "Valittavien määrä on suurempi tai yhtä suuri kuin ehdokkaiden")

    def check_validity(self):
        """Kutsuu kaikkia tarkistusfunktioita.

        Returns:
            Lista virheistä riippumatta onko niitä.
        """
        self._errors = []
        self._check_correct_characters()
        self._check_correct_numbers()
        self._check_all_different()
        self._check_seats_number()
        return self._errors

    def _remove_empty(self):
        """Poistaa kokonaan tyhjät äänet, eli sellaiset, joissa äänestäjä on jättänyt
            kaikki kohdat tyhjiksi.
        """
        empty = []
        for i in range(len(self._votes)):
            is_empty = True
            for choice in self._votes[i]:
                if choice not in ('0', ''):
                    is_empty = False
                    break
            if is_empty:
                empty.append(i)
        number = 0
        for i in empty:
            self._votes.pop(i-number)
            number += 1

    def save(self, name):
        """Tallentaa äänet nimellä tietokantaan.

        Args:
            name: Tietokantaan luotavan (tai siellä olevan) taulun nimi.

        Returns:
            True, jos tallennus onnistuu, muuten False.
        """
        database = Database()
        if database.save_table(self._votes, name):
            return True
        return False

    def stv_result(self):
        """Laskee siirtoäänivaalin tuloksen.

        Returns:
            Tulosolion, joka kertoo vaalien voittajat.
        """
        self._remove_empty()
        candidates = []
        for i in range(self._ncandidates):
            candidates.append(Candidate(str(i+1)))
        ballots = []
        for i in range(len(self._votes)):
            lst = []
            for vote in self._votes[i]:
                if vote not in ('0', ''):
                    lst.append(candidates[int(vote)-1])
            ballots.append(Ballot(ranked_candidates=lst))
        election_result = pyrankvote.single_transferable_vote(
            candidates, ballots, int(self._seats),
            compare_method_if_equal=CompareMethodIfEqual.MostSecondChoiceVotes,
            pick_random_if_blank=False
        )
        return election_result
