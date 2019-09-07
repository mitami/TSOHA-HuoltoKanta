# Käyttäjät

(Admin -)käyttäjänä haluan nähdä listauksen kaikista järjestelmään kirjatuista työntekijöistä, tarkemmat tiedot jokaisesta yksittäisestä työntekijästä, sekä mahdollisuuden muokata yksittäisten työntekijän nimeä ja titteliä tai poistaa työntekijöitä järjestelmästä.

------------------------------------------------

#### Listaus kaikista käyttäjistä
`SELECT * FROM Huoltomiehet` 


#### Yksittäinen käyttäjä
`SELECT * FROM Huoltomiehet WHERE id = X`

#### Käyttäjän tietojen muokkaus
`UPDATE Huoltomiehet SET name = 'uusi nimi', title = 'uusi title' WHERE id = X`
