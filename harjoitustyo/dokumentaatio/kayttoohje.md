# Käyttöohje

## Asennus

Lataa ensin projektin koodi sen uusimmasta releasesta.
Suorita sitten kansiossa harjoitustyo komento "poetry install" riippuvuksien asentamiseksi. Sen jälkeen ohjelman voi käynnistää komennolla "poetry run invoke start".

## Äänten syöttäminen
Anna ehdokkaiden ja äänestäjien määrä ja paina "Ok". Syötä siirtoäänivaaleissa annetut äänet kirjaamalla ruutuihin äänestettyjen ehdokkaiden numerot. Numeroiden tulee olla 1–ehdokkaiden määrä. Tyhjät äänet voi jättää tyhjäksi tai merkitä 0:na. Anna myös valittavien ehdokkaiden määrä.

## Tulokset
Paina "Laske" ja sovellus kertoo voittaneet ehdokkaat. Jos syötetyissä äänissä on virheellisiä merkkejä tai tuplaääniä, sovellus ei laske tulosta, vaan antaa virheilmoituksen.

## Csv-tiedoston lukeminen
Paina "csv-tiedosto" ja sovellus tuo tiedostosta äänet. Tiedoston tulee sisältää vain ehdokasnumeroita pilkulla erotettuna.

## Äänten tallennus
Voit myös tallentaa syöttämäsi äänet. Paina "Tallenna äänet..." ja anna äänille nimi, joka koostuu kirjaimista ja mahdollisesti numeroista. Tallennettuja ääniä voit tarkastella painamalla aloitusnäkymässä "Tallennetut äänitaulukot". Valitse listasta taulukko ja sitten haluamasi toiminto. Taulukoita voi katsoa, poistaa tai viedä csv-tiedostoiksi.