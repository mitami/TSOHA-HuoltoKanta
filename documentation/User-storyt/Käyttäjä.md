# Käyttäjät

(Admin -)käyttäjänä haluan nähdä listauksen kaikista järjestelmään kirjatuista työntekijöistä, tarkemmat tiedot jokaisesta yksittäisestä työntekijästä, sekä mahdollisuuden muokata yksittäisten työntekijän nimeä ja titteliä tai poistaa työntekijöitä järjestelmästä.

------------------------------------------------

#### Listaus kaikista työntekijöistä/toimeenpanijoista(executor)
Polku: `/executors`

`SELECT * FROM Huoltomiehet` 


#### Yksittäinen käyttäjä
Polku: `executor/id`

`SELECT * FROM Huoltomiehet WHERE id = X`

#### Käyttäjän tietojen muokkaus
Polku: `executor/id/edit`

`UPDATE Huoltomiehet SET name = 'uusi nimi', title = 'uusi title' WHERE id = X`
