# TSOHA-HuoltoKanta

[Heroku -linkki](https://tsoha-konekanta.herokuapp.com/)

---------------------------

### Heroku -testitunnukset:

tunnus | salasana |
---- | ----
admin | admin
test | testi


------------------------

Tietokantasovellus tehtäväkirjanpitoa varten.

Tietokannan tarkoituksena on pitää kirjaa kohteille jo suoritetuista toimista, tulevista aikataulutetuista toimista, toimenpiteiden suorittajista, sekä kohteista itsestään sekä niiden sijainnista.

Järjestelmässä on käyttäjiä, jotka luokitellaan joko Admin -oikeuksien haltijoiksi, tai "normaaleiksi" käyttäjiksi.
Admin -oikeuksilla käyttäjä pääsee käsiksi kaikkeen sovelluksessa toteutettuun toiminnallisuuteen, eli käytännössä kaikkien taulujen CRUD -oikeudet kaikkiin näkymiin pääsyn lisäksi.

"Normaalin" -käyttäjän ei ole valmiissa sovelluksessa tarkoitus pystyä poistamaan eikä muokkaamaan tietokannassa mitään, mitä ei ole itse sinne lisännyt. Normaali käyttäjä ei myöskään pysty rekisteröimään uusia käyttäjiä, vaan ainoastaan Admin voi sen tehdä, paitsi silloin kun tietokannassa ei ole yhtään käyttäjää, voi ensimmäisen käyttäjän luoda kuka vain, ja tämä käyttäjä automaattiseti saa Admin -oikeudet. Tämän käyttäjän luomisen jälkeen täytyy siis kirjautua sillä, jos haluaa luoda lisää käyttäjiä.

[Tietokantakaavio](../master/documentation/Kaaviot/TSOHA-HuoltoKanta-TietokantaKaavio-smaller.png)


--------------------------


### Linkkejä

[Asennusohjeet](../master/documentation/asennusohje.md)

[Tarkempi käyttöohje](../master/documentation/käyttöohje.md)

[Käyttäjä -storyt](../master/documentation/User-storyt/Käyttäjä.md)

