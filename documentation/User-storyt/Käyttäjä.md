# Käyttäjät

Admin -käyttäjänä haluan nähdä listauksen kaikista järjestelmään kirjatuista Työntekijöistä, tarkemmat tiedot jokaisesta yksittäisestä Työntekijästä, sekä mahdollisuuden muokata yksittäisten Työntekijän nimeä ja titteliä ja lisätä sekä poistaa Työntekijöitä järjestelmästä.

Admin-käyttäjänä haluan muokata Kohteen Sijaintia sekä nimeä, poistaa Kohteita, ja lisätä Kohteita

Admin käyttäjänä haluan lisätä ja poistaa ja muokata Sijainteja

Admin-käyttäjänä haluan CRUD -mahdollisuuden kaikkiin Tehtäviin

Käyttäjänä haluan pystyä vaihtamaan salasanani sekä tunnukseni

Käyttäjänä haluan nähdä listauksen kaikista Kohteista, joille Toimenpiteitä/tehtäviä tehdään/voidaan tehdä
Käyttäjänä haluan tarkastella yksittäistä Kohdetta, ja nähdä siihen liittyvät tiedot ja Tehtävät listattuna

Käyttäjänä haluan nähdä listauksen kaikista Tehtävistä, jotka on rekisteroity minulle
Käyttäjänä haluan merkitä oman Tehtäväni tehdyksi
Käyttäjänä haluan luoda uusia aikataulutettuja Tehtäviä, jotka liittyvät tiettyihin Kohteisiin
Käyttäjänä haluan merkitä Tehtävän tehdyksi (tai ei-tehdyksi)



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


Käyttäjän Tehtävät:
`SELECT action.id, action.name, action.desc, action.done, action.due, target.name, location.name, executor.name"`
                    `" FROM Action JOIN executor_action ON executor_action.action_id = action.id"`
                    `" JOIN Executor ON Executor.id = executor_action.executor_id"`
                    `" JOIN Target ON Target.id = action.target_id"`
                    `" JOIN Location ON Location.id = target.location_id"`
                    `" WHERE action.id = :id`

Käyttäjän tekemättömien Tehtävien määrä:
`SELECT COUNT(*)`
`FROM executor_action`
`LEFT JOIN Action`
`ON Action.id = executor_action.action_id`
`WHERE Action.done = :boolean`
`AND executor_action.executor_id = :id`

Käyttäjän tehtyjen Tehtävien määrä:
`SELECT COUNT(*)`
`FROM executor_action`
`LEFT JOIN Action`
`ON Action.id = executor_action.action_id`
`WHERE Action.done = :boolean`
`AND executor_action.executor_id = :id`

Ylläolevissa "boolean" -parametri johtuu SQLiten ja PSQL eroista Boolean -tyypin
käsittelyssä. Ohjelma tarkistaa ensin ollaanko tuotannossa vai kehitysympäristössä,
ja sen perusteella valitsee käytetäänkö TRUE/FALSE vai 0/1