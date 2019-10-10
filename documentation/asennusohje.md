# Asennusohjeet

---------


## Paikallinen asennus

* Sovellus vaatii SQLite -tietokannan toimiakseen oikein paikallisesti.

  * Vaihtoehtoisesti muuttamalla tietokannan asetuksia \__init__.py -tiedostosta
  sovellusta voi käyttää myös PSQL -kannan kanssa.

* Asenna riippuvuudet:

  `pip3 install -r requirements.txt`

* Käynnistä sovellus:

  `cd polku/sovelluksen/juureen`

  `source venv/bin/activate`

  `python3 run.py`
----------

## Heroku

* Luo tunnukset ja lataa Heroku-CLI
* Työnnä sovellus Herokuun
  * Lisää Herokuun ympäristömuuttuja "Heroku": 1
  * Muuttujan avulla sovellus saadaan tuotantomoodiin