# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on tarkoitettu esimerkiksi kaupan allalle budjetin ja avainlukujen suunnitteluun. Sovellusta voi
käyttää monta eri myymälää samanaikaisesti ja niillä kaikilla on omat budjetit ja avainluvut.

## Käyttäjät
Ensimmäisessä näkymässä käyttäjä voi 
 - ✅ nähdä edellisen tuloskauden toteutuneen myynnin
 - ✅ lisätä vuosittaisen kasvutavoitteen ja sen mukaan laskea henkilöstöbudjetin prosentteina.  
 - ✅ muuttaa asettettuja tavoitteita tuloskauden aikana jos siihen on tarvetta.  
Käyttäjä (myymäläpäällikkö, franchise-yrittäjä) 
 - voi jakaa budjetin kuukausitasolle.  
 - ✅asettaa avainlukutavoitteet

## Käyttöliittymäluonnos
Sovellus koostuu 4 eri näkymästä. Sovellus aukeaa kirjautumisnäkymään, josta on mahdollisuus joko kirjautua sisään
olemassa olevilla tunnuksilla tai siirtyä rekisteröitymään palvelun käyttäjäksi.  
Onnistuneen kirjautumisen tai rekisteröitymisen jälkeen aukeaa näkymä josta näkyy oman myymälän tiedot ja jossa voi muokata vuositasolla myyntitavoitetta tai henkilöstöbudjetin suuruutta.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
 - ✅ Käyttäjä voi luoda itselleen käyttäjätunnuksen
 - ✅ Käyttätunnus on uniikki
 - ✅ Salasanassa täytyy olla vähintään 6 merkkiä, sekä kirjaimia että numeroita  
    
 - ✅ Käyttäjä voi kirjautua järjestelmään 
  -✅ Jos käyttäjää ei ole olemassa tai käyttäjätunnus tai salasana on väärin kirjoitettu, järjestelmä ilmoittaa siitä.
    
### Kirjautumisen jälkeen
- ✅ Käyttäjä näkee vuosibudjetin 
- ✅ Käyttäjä näkee kuluvan kuukauden budjetin 
- ✅Käyttäjä voi muokata avainlukutavotteita 
- ✅ Käyttäjä voi kirjautua ulos

- ✅ Sovellus käyttää tietokantaa jossa on syötettynä edellisen tuloskauden myynnit ja kävijät kuukausitasolla 

## Jatkokehitysideoita
- Sovelluksessa avautuisi erillinen näkymä jossa voisi syöttää edellisen tuloskauden tuloksia jos niitä ei ole vielä tietokannassa
- Sovellukseen olisi yhdistettynä henkilöstöbudjetti joka laskisi päivätasolla karkeasti kuinka monta työtuntia on käytettävissä
- Sovellukseen saisi päiväkohtaisesti merkittyä kyseisien päivän tehtävät jos niitä on
    - Tehtävät näkyisivät joko tekemättöminä tai ne voisi merkata tehdyiksi  
- Sovellukseen voisi yhdistää työvuorosuunnittelun
- Kiinteät- ja muuttuvat kulut näkyisivät kuukausitasolla
    

    
  
