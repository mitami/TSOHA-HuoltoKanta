# Asennusohjeet

---------


## Paikallinen asennus

* Sovellus vaatii SQLite -tietokannan toimiakseen oikein paikallisesti.

  * Vaihtoehtoisesti muuttamalla tietokannan asetuksia \_\_init\_\_.py -tiedostosta
  sovellusta voi käyttää myös PSQL -kannan kanssa.

* Asenna riippuvuudet:

  `pip3 install -r requirements.txt`
  
  HUOM. WINDOWS:
   * Jos psycopg -paketin asennus ei onnistu, lisää PostgreSQL Windowsin PATH muuttujaan
   * 32-bit Python ei välttämättä toimi, asenna 64-bit

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
