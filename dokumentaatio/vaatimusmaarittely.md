# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on tarkoitettu esimerkiksi kaupan allalle budjetin ja avainlukujen suunnitteluun. Sovellusta voi
käyttää monta eri myymälää samanaikaisesti ja niillä kaikilla on omat budjetit ja avainluvut.

## Käyttäjät
Admin-oikeuksilla käyttäjä voi 
 - lisätä vuosittaisen kasvutavoitteen ja henkilöstöbudjetin prosentteina.  
 - muuttaa asettettuja tavoitteita tuloskauden aikana jos siihen on tarvetta.  
Käyttäjä (myymäläpäällikkö, franchise-yrittäjä) 
 - voi jakaa budjetin kuukausitasolle.  
 - asettaa avainlukutavoitteet
 - kasvattaa myyntiä kumulatiivisesti jolloin hän näkee ollaanko kuukausitasolla plussalla vai miinuksella.

## Käyttöliittymäluonnos
Sovellus koostuu 4 eri näkymästä. Sovellus aukeaa kirjautumisnäkymään, josta on mahdollisuus joko kirjautua sisään
olemassa olevilla tunnuksilla tai siirtyä rekisteröitymään palvelun käyttäjäksi.  
Onnistuneen kirjautumisen tai rekisteröitymisen jälkeen aukeaa näkymä josta näkyy oman myymälän tiedot.  
Admin-oikeuksilla aukeaa oma sivu jossa näkyy kaikki olemassa olevat myymälät.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
 - Käyttäjä voi luoda itselleen käyttäjätunnuksen
    - Käyttätunnus on uniikki
    - Siinä täytyy olla vähintään 6 merkkiä, sekä kirjaimia että numeroita  
    
 - Käyttäjä voi kirjautua järjestelmään 
    - Jos käyttäjää ei ole olemassa tai käyttäjätunnus tai salasana on väärin kirjoitettu, järjestelmä ilmoittaa siitä.
    
### Kirjautumisen jälkeen
- Käyttäjä näkee vuosibudjetin ja saavutetun myynnin kumulatiivisesti  
- Käyttäjä näkee kuluvan kuukauden budjetin ja toteutuman kumulatiivisesti  
    - Jos budejetista ollaan jäljessä, voi hän muokata loppukuukaudelle päiväkohtaisia tavoitteita  
- Käyttäjä voi muokata avainlukutavotteita 
- Käyttäjä voi kirjautua ulos

- Sovellus käyttää tietokantaa jossa on syötettynä edellisen tuloskauden myynnit ja kävijät kuukausitasolla 

## Jatkokehitysideoita
- Sovellukseen olisi yhdistettynä henkilöstöbudjetti joka laskisi päivätasolla karkeasti kuinka monta työtuntia on käytettävissä
- Sovellukseen saisi päiväkohtaisesti merkittyä kyseisien päivän tehtävät jos niitä on
    - Tehtävät näkyisivät joko tekemättöminä tai ne voisi merkata tehdyiksi  
- Sovellukseen voisi yhdistää työvuorosuunnittelun
- Kiinteät- ja muuttuvat kulut näkyisivät kuukausitasolla
    

    
  
