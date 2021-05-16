# Testausdokumentti

Ohjelmaa on testattu automaattisesti unittestilla sekä manuaalisesti.

## Yksikkö- ja integraatiotestaus

Jokaisella services-kansion luokalla on sitä vastaava testausluokka. Testeissä on sekä yksikkö- että integraatiotestejä. Tietokantatoimintojen ja csv-tiedostojen käsittelyn testauksessa käytetään väliaikaisia tiedostoja, jotka katoavat itsestään.

## Testikattavauus

Sovelluksen haarautumakattavuus käyttöliittymää lukuun ottamatta on 88 %.

![testikattavuus](https://github.com/emigination/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/testikattavuus.png)

Testaamatta jäivät funktiot, jotka avaavat tiedostoselaimen, ympäristömuuttujien käsittely sekä tietokantaoperaatiossa mahdollisesti tapahtuvien virheiden käsittely.

## Järjestelmätestaus

Järjestelmätestausta on tehty manuaalisesti. Kaikkia toimintoja on testattu, myös syöttämällä virheellisiä arvoja, esimerkiksi liian suuria ehdokasnumeroita.