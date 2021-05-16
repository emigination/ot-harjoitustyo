# Käyttöohje

## Asennus
Lataa ensin projektin koodi sen uusimmasta releasesta.
Suorita sitten kansiossa harjoitustyo komento "poetry install" riippuvuksien asentamiseksi. Sen jälkeen ohjelman voi käynnistää komennolla "poetry run invoke start".

## Äänten syöttäminen
Anna ehdokkaiden ja äänestäjien määrä ja paina "Ok". Syötä siirtoäänivaaleissa annetut äänet kirjaamalla ruutuihin äänestettyjen ehdokkaiden numerot. Numeroiden tulee olla välillä 1–ehdokkaiden määrä. Tyhjät äänet voi jättää tyhjäksi tai merkitä 0:na. Anna myös valittavien ehdokkaiden määrä.

## Tulokset
Paina "Laske" ja sovellus kertoo voittaneet ehdokkaat. Jos syötetyissä äänissä on virheellisiä merkkejä tai tuplaääniä, sovellus ei laske tulosta, vaan antaa virheilmoituksen.

## Csv-tiedoston lukeminen
Paina "csv-tiedosto" ja sovellus tuo tiedostosta äänet. Tiedoston tulee sisältää vain ehdokasnumeroita pilkulla erotettuna.

## Äänten tallennus tietokantaan ja hakeminen sieltä
Voit myös tallentaa syöttämäsi äänet. Paina "Tallenna äänet..." ja anna äänille nimi, joka koostuu kirjaimista ja mahdollisesti numeroista. Ensimmäisen merkin tulee olla kirjain. Tallennettuja ääniä voit tarkastella painamalla aloitusnäkymässä "Tallennetut äänitaulukot". Valitse listasta taulukko ja sitten haluamasi toiminto. Taulukoita voi katsoa, poistaa tai viedä csv-tiedostoiksi.

## Äänten tallenus csv-tiedostona
Viedäksesi äänet csv-tiedostona tallenna ne ensin tietokantaan. Paina "Tallennetut äänitaulukot", valitse taulukko, josta haluat csv-tiedoston, ja paina "Vie csv-tiedostona". Valitse tiedostolle sijainti ja nimi. Sovellus kertoo, että tallennus onnistui.

## Tietokannan asetukset
Tietokannan tiedostosijaintai voi muuttaa muokkaamalla .env-tiedostoa, joka on kansiossa harjoitustyo. Oletuksena tiedostonimi on database.sqlite. Tietokanta luodaan data-kansioon automaattisesti, kun sitä tarvitaan.