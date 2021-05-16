# Arkkitehtuuri

## Rakenne

Ohjelman koodi on jaettu käyttöliittymään ja palveluihin luokkakaavion mukaisesti:

![luokkakaavio](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/luokkakaavio.svg)

## Sovelluslogiikka

Votes-luokka vastaa syötettyjen äänten kelvollisuuden tarkastamisesta, niiden muokkaamisesta laskettavaan muotoon ja itse tulosten laskennasta pyrankvote-kirjaston avulla. Database-luokka vastaa tietokantatoiminnoista eli äänitaulukoiden tallentamisesta, hakemisesta ja poistamisesta sieltä. Taulukoita tietokantaan tallennettaessa Votes kutsuu Databasen tallennusfunktiota. FileReader-luokka lukee äänet csv-taulukosta ja FileWriter vastaavasti vie tietokantaan tallennetut äänet csv-tiedostoon.

## Käyttöliittymä

Näkymiä on kolme erilaista: aloitus-/tietojensyöttönäkymä, tulosnäkymä ja tallennettujen taulukoiden tarkastelunäkymä. Aloitusnäkymästä voi liikkua kumpaankin muuhun näkymään ja niistä voi palata aloitusnäkymään. Kukin näkymä on oma luokkansa. Aloitusnäkymässä on koko ajan näkyvissä kolme framea, joista votes_frame on toteutettu erillisenä luokkana. Tallennus-frame tulee näkyviin vain tarvittaessa. Aloitusnäkymä käyttää lisäksi ScrollableFrame-luokan framea, jonka sisässä muut framet ovat ja jota voi vierittää vierityspalkeilla, jos ikkuna on pienempi kuin näytettävä sisältö. Kun käyttäjä tuo äänet csv-tiedostosta tai avaa tietokantaan tallennetun taulukon, äänet näytetään aloitusnäkymässä samalla tavalla kuin jos käyttäjä olisi ne syöttänyt.

Kun käyttäjä poistaa tallennetun taulukon, taulukkovalikko luodaan uudelleen pyytäen Database-oliolta ajantasaisen listan olemassa olevista taulukoista, niin etteivät poistetut taulukot jää näkyviin.

## Toiminnallisuudet

### Äänestyksen tulosten lasku

Kun käyttäjä on syöttänyt äänet tai ne on luettu csv-tiedostosta, Votes-olio tarkistaa äänten kelvollisuuden, eli että kaikki numerot ovat kokonaislukuja ja vastaavat jotain ehdokasta, sama äänestäjä ei äänestää samaa ehdokasta useaa kertaa ja valittavien määrä on pienempi kuin ehdokkaiden. Votes palauttaa listan virheistä. Jos niitä on, näytetään virheviesti. Jos lista on tyhjä, näkymä vaihtuu tulosnäkymään ja Votes laskee tulokset. Voittajat näytetään käyttäjälle.

![sekvenssikaavio_tulostenlasku](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/sekvenssikaavio_tulostenlasku.svg)

### Äänten tallennus tietokantaan

Halutessaan tallentaa äänet, käyttäjä klikkaa "Tallenna" ja antaa nimen äänitaulukolle. Jos taulukon nimi on kelvollinen, eli koostuu alfanumeerisista merkeistä, luodaan Votes-olio, joka tarkistaa äänten kelvollisuuden samaan tapaan kuin tulosten laskun yhteydessä. Jos kaikki on hyvin, Votes pyytää Database-oliota tallentamaan äänet käyttäjän valitsemalla nimellä tietokantaan. Jos se onnistuu, käyttäjälle näytetään viesti, että tallennus onnistui, ja frame, johon taulukon nimi annetaan, katoaa.

![sekvenssikaavio_tallennus](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/sekvenssikaavio_tallennus.svg)

### Äänten tallennus csv-tiedostona

Käyttäjä valitsee pudotusvalikosta tietokantaan tallennetun äänitaulukon nimen ja klikkaa "Vie csv-tiedostona". Aukeaa tiedostoselain, jolla käyttäjä antaa tiedoston nimen ja sijainnin. FileWriter-olio pyytää Database-oliolta kyseisen taulukon ja saa sen kaksiulotteisena taulukkolistana. FileWriter tallentaa taulukon csv:nä, ja käyttäjälle ilmoitetaan, että tiedosto on tallennettu.

![sekvenssikaavio_vieminen](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/sekvenssikaavio_vieminen.svg)

### Tietokantaan tallennetujen äänten tarkastelu

Kuten ylemmässä kohdassa, käyttäjä valitsee haluamansa taulukon nimen pudotusvalikosta. Kun käyttäjä klikkaa "Näytä", Database-oliolta pyydetään haluttu taulukko, ja sen sisältö näytetään samassa näkymässä, johon käyttäjä voi itse syöttää ääniä.

### Csv-tiedoston lukeminen

Kun käyttäjä klikkaa "csv-tiedosto", aukeaa tiedostoselain, josta käyttäjä valitsee haluamansa csv-tiedoston. FileReader-olio lukee csv:n ja tekee siitä kaksiulotteisen taulukkolistan, jonka sisältö näytetään aloitusnäkymässä.

### Äänitaulukoiden poistaminen tietokannasta

Käyttäjä voi valita tallenetun taulukon samasta pudostusvalikosta kuin taulukkoja katsellessa tai viedessä ja klikata "Poista", jolloin Database-olio poistaa kyseisen taulun tietokannasta.

## Tiedon pysyväistallennus

Database-luokan avulla äänitaulukoita voi tallentaa SQLite-tietokantaan. Tietokannan nimi on vakio, mutta käyttäjä päättää kunkin taulukon nimen. Käyttäjä voi myös poistaa taulukoita.

FileWriter-luokalla tietokantaan tallennettuja äänitaulukoita voi tallentaa CSV-tiedostoina. Äänet tallennetaan samantyyppiesti kuin miten ne syötetään; yhdelle riville tallenetaan yhden äänestäjän äänet. Numerot erotetaan toisistaan pilkulla.