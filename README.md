# Vaalituloslaskuri

Sovelluksella voi laskea siirtoäänivaalien tuloksen.

## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuri](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/arkkitehtuuri.md)


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
