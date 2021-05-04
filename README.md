# Vaalituloslaskuri

Sovelluksella voi laskea siirtoäänivaalien tuloksen.

## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
* [Arkkitehtuuri](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kayttoohje.md)
* [Työaikakirjanpito](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)

## Asennus
1. Lataa sovellus [täältä](https://github.com/emigination/ot-harjoitustyo/releases/tag/viikko6)
2. Asenna riippuvuudet kansiossa "harjoitustyo" komennolla poetry install
3. Käynnistä sovellus samassa kansiossa komennolla poetry run invoke start

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:

poetry run invoke start

### Testaus
Testit suoritetaan komennolla:

poetry run invoke test

### Testikattavuus
Testikattavuusraportti generoidaan komennolla:

poetry run invoke coverage-report

### Pylint
Tiedoston .pylintrc määrittelemät tarkistukset suoritetaan komennolla:

poetry run invoke lint
