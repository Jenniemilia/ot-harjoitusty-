# Ohjelmistotekniikka, harjoitustyö - Budjettisovellus #

Budjettisovellus on tarkoitettu työvälineeksi esimerkiksi kaupan alalle. Tietokannassa on edellisen tuloskauden toteutuneet myynnit ja avainluvut kuukausitasolla. Näiden pohjalta Admin-oikeuksilla pystytään muokaamaan tulevan tuloskauden tavoitteita myymäläkohtaisesti.
Myymälätunnuksilla näkee tulevan kuukauden tavoitteen sekä pystyy muokkaamaan avainlukutavoitteita sen mukaisesti, että budjetti saavutettaisiin. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/Jenniemilia/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/Jenniemilia/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/Jenniemilia/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Releaset
[Viikko 5](https://github.com/Jenniemilia/ot-harjoitustyo/releases/tag/v1.0.0)

[Viikko 6](https://github.com/Jenniemilia/ot-harjoitustyo/releases/tag/viikko6)

## Asennus
1. Asenna riippuvuudet komennolla: 
```bash
poetry install
```
2. Käynnistä sovellus komennolla:  
```bash
poetry run invoke start
```


## Komentorivitoiminnot
Ohjelman suorittaminen onnistuu komennolla: 
```bash
poetry run invoke start
```

Ohjelman testit suoritetaan komennolla: 
```bash
poetry run invoke test
```

Testikattavuuden voi generoida komennolla:  
```bash
poetry run invoke coverage-report 
```

Raportti löytyy tämän jälkeen: 
```bash
htmlcov-hakemistosta
```

Laatutarkastuksen voi suorittaa komennolla:  
```bash
poetry run invoke lint
