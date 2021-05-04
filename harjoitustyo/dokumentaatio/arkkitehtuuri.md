# Arkkitehtuuri

## Rakenne

Ohjelman koodi on ainakin toistaiseksi jaettu käyttöliittymään ja palveluihin luokkakaavion mukaisesti:

![luokkakaavio](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/luokkakaavio.svg)

## Sovelluslogiikka

Votes-luokka vastaa syötettyjen äänten kelvollisuuden tarkastamisesta, niiden muokkaamisesta laskettavaan muotoon ja itse tulosten laskennasta pyrankvote-kirjaston avulla. Database-luokka vastaa tietokantatoiminnoista eli äänitaulukoiden tallentamisesta, hakemisesta ja poistamisesta sieltä. Taulukoita tietokantaan tallennettaessa Votes kutsuu Databasen tallennusfunktiota. FileReader-luokka lukee äänet csv-taulukosta ja FileWriter vastaavasti vie tietokantaan tallennetut äänet csv-tiedostoon.

## Sekvenssikaavio

![sekvenssikaavio](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/sekvenssikaavio.svg)
