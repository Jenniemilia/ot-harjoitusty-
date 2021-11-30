# Ohjelmistotekniikka, harjoitustyö - Budjettisovellus #

Budjettisovellus on tarkoitettu työvälineeksi esimerkiksi kaupan alalle. Tietokannassa on edellisen tuloskauden toteutuneet myynnit ja avainluvut kuukausitasolla. Näiden pohjalta Admin-oikeuksilla pystytään muokaamaan tulevan tuloskauden tavoitteita myymäläkohtaisesti.
Myymälätunnuksilla näkee tulevan kuukauden tavoitteen sekä pystyy muokkaamaan avainlukutavoitteita sen mukaisesti, että budjetti saavutettaisiin. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/Jenniemilia/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/Jenniemilia/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus
1. Asenna riippuvuudet komennolla: poetry install
2. Käynnistä sovellus komennolla poetry run invoke start

## Komentorivitoiminnot
Ohjelman suorittaminen onnistuu komennolla: poetry run invoke start

Ohjelman testit suoritetaan komennolla: poetry run invoke test

Testikattavuuden voi generoida komennolla: poetry run invoke coverage-report  
Raportti löytyy tämän jälkeen htmlcov-hakemistosta

Laatutarkastuksen voi suorittaa komennolla: poetry run invoke lint
