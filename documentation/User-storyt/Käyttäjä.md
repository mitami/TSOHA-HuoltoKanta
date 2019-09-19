# Käyttäjät

Admin -käyttäjänä haluan nähdä listauksen kaikista järjestelmään kirjatuista työntekijöistä, tarkemmat tiedot jokaisesta yksittäisestä työntekijästä, sekä mahdollisuuden muokata yksittäisten työntekijän nimeä ja titteliä ja lisätä sekä poistaa työntekijöitä järjestelmästä.

Käyttäjänä haluan pystyä vaihtamaan salasanani sekä tunnukseni

Käyttäjänä haluan nähdä listauksen kaikista Kohteista, joille toimenpiteitä tehdään/voidaan tehdä

Käyttäjänä haluan nähdä listauksen kaikista toimenpiteistä, jotka on rekisteroity minulle
Käyttäjänä haluan merkitä oman toimenpiteeni tehdyksi
Käyttäjänä haluan luoda uusia toimenpiteitä, jotka liittyvät tiettyihin kohteisiin

Käyttäjänä haluan tarkastella yksittäistä kohdetaa, ja nähdä siihen liittyvät tiedot ja toimenpiteet listattuna


------------------------------------------------

#### Listaus kaikista käyttäjistä/työntekijöistä/toimeenpanijoista(executor)
Polku: `/executors`

`SELECT * FROM Huoltomiehet` 

#### Yksittäisen työntekijän lisäys
Polku: `/executors/new`

`INSERT INTO Huoltomiehet VALUES ('nimi', 'titteli')`

#### Yksittäinen työntekijä
Polku: `/executor/id`

`SELECT * FROM Huoltomiehet WHERE id = X`

#### Työntekijän tietojen muokkaus
Polku: `/executor/id/update`

`UPDATE Huoltomiehet SET name = 'uusi nimi', title = 'uusi title' WHERE id = X`

#### Työntekijän poistaminen
Polku: `/executor/id/delete`

`DELETE FROM Huoltomiehet WHERE id = X`
