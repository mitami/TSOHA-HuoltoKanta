# Käyttöohjeet

---------

### Kirjautuminen

Sovellukseen kirjautuminen jakautuu kahteen skenaarioon:
#### 1. Tietokannassa ei ole yhtään käyttäjää
* Sovellukseen ei voi kirjautua, vaan on ensin luotava uusi käyttäjä. Tämä tapahtuu seuraavasti:

  * Klikkaa yläpalkin "Käyttäjät" -linkistä. Avautuu näkymä, joka listaa kaikki käyttäjät.

  * Näkymän vasemman yläkulman läheisyydessä on nappi: "Lisää uusi". Paina nappia.

  * Syötä tiedot ja paina "Submit"

Ensimmäinen käyttäjä on nyt luotu, ja sille on myönnetty Admin -oikeudet automaattisesti.
Lisäkäyttäjien luominen vaatii nyt luodulla käyttäjällä kirjautumisen.

* Kirjautuminen
  * Paina yläpalkin "Login" -nappia

  * Täytä olemassaolevan käyttäjän nimi ja salasana

  * Paina "Submit" -nappia


#### 2. Tietokannassa on ainakin yksi käyttäjä

* Kirjautuminen
  * Paina yläpalkin "Login" -nappia

  * Täytä olemassaolevan käyttäjän nimi ja salasana

  * Paina "Submit" -nappia

---------


### Uuden käyttäjän luominen

Uuden käyttäjän luominen jakautuu myös kahteen skenaarioon:
#### 1. Tietokannassa ei ole yhtään käyttäjää
* Voit luoda käyttäjän [Kirjautuminen 1.](#kirjautuminen) mukaan

#### 2. Tietokannassa on ainakin yksi käyttäjä
* Luodakseen lisää käyttäjiä, on ensin [kirjauduttava](#2-tietokannassa-on-ainakin-yksi-käyttäjä) Admin -oikeudet omaavalla käyttäjätunnuksella

  * Klikkaa yläpalkin "Käyttäjät" -linkkiä.

  * Klikkaa "Lisää uusi"

  * Täytä tiedot ja paina "Submit"
    (huom. tällä hetkellä vain ensimmäisenä luotu käyttäjä on Admin, ja kaikki
    sen jälkeen luodut ovat "normaaleja" käyttäjiä)


-------

### Kohteiden, Tehtävien ja Sijaintien lisääminen

Näiden lisääminen on mahdollista vain kirjautuneena, ja jokaisella on oma linkkinsä
yläpalkissa: "Kohteet", "Sijainnit" yms.
Näistä klikkaamalla pääsee listausnäkymään joka näyttää kaikki kyseiset oliot,
ja jossa on vasemmassa yläkylmassa "Lisää uusi" -nappi, joka johtaa lomakenäkymään,
missä uuden olion tiedot voidaan syöttää ja lähettää palvelimelle.


----------

### Yksittäisten olioiden tarkastelu ja muokkaus

Navigoimalla ensin [oikeaan listausnäkymään](#kohteiden,-tehtävien-ja-sijaintien-lisääminen)
ja sitten klikkaamalla listalta haluamansa kohteen riviä, ohjautuu käyttäjä klikkaamansa kohteen
näkymään.
Näkymässä on selkeät napit, jotka tarjoavat toiminnallisuuden olion muokkaamiseen, sekä poistamiseen.

* Tehtävän muokkauksessa/luomisessa on syytä huomata, että toistaiseksi käytössä olevan HTML:n suoraan tarjoaman
"monivalintalistan" käyttö ei ole kovin käyttäjäystävällistä.

  * Valitaksesi yhden käyttäjän, klikkaa jostakin käyttäjän nimesetä listassa

  * Valitaksesi useita käyttäjiä, pidä CTRL pohjassa ja klikkaa haluamistasi nimistä

  * Lista on tarkoitus vaihtaa käyttäjäystävällisempään, kunhan tärkeämmät toiminnallisuudet on saatu valmiiksi
