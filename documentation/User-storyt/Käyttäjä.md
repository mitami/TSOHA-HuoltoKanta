# Käyttäjät

Admin -käyttäjänä haluan nähdä listauksen kaikista järjestelmään kirjatuista työntekijöistä, tarkemmat tiedot jokaisesta yksittäisestä työntekijästä, sekä mahdollisuuden muokata yksittäisten työntekijän nimeä ja titteliä ja lisätä sekä poistaa työntekijöitä järjestelmästä.

Admin-käyttäjänä haluan muokata Kohteen Sijaintia sekä nimeä, poistaa Kohteita, ja lisätä Kohteita

Admin käyttäjänä haluan lisätä ja poistaa ja muokata Sijainteja

Käyttäjänä haluan pystyä vaihtamaan salasanani sekä tunnukseni

Käyttäjänä haluan nähdä listauksen kaikista Kohteista, joille toimenpiteitä/tehtäviä tehdään/voidaan tehdä
Käyttäjänä haluan tarkastella yksittäistä kohdetta, ja nähdä siihen liittyvät tiedot ja tehtävät listattuna

Käyttäjänä haluan nähdä listauksen kaikista tehtävistä, jotka on rekisteroity minulle
Käyttäjänä haluan merkitä oman tehtäväni tehdyksi
Käyttäjänä haluan luoda uusia tehtäviä, jotka liittyvät tiettyihin kohteisiin



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

#### Yksittäisen Tehtävän näkymä
Polku `/actions/id`

`SELECT action.id, action.name, action.desc, action.done, action.due, target.name, location.name, executor.name"`
                    `" FROM Action JOIN executor_action ON executor_action.action_id = action.id"`
                    `" JOIN Executor ON Executor.id = executor_action.executor_id"`
                    `" JOIN Target ON Target.id = action.target_id"`
                    `" JOIN Location ON Location.id = target.location_id"`
                    `" WHERE action.id = :id`
