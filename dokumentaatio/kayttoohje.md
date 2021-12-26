## Käyttöohje

#### Sovelluksen käynnistäminen:

Ennen ohjelman ensimmäistä käynnistämistä, asenna riippuvuudet komennolla:  
poetry install

Suorita sitten alustustoimet komennolla:  
poetry run invoke build

Ohjelman voi lopuksi käynnistää komennolle:  
poetry run invoke start

#### Kirjautuminen 

Sovellus avautuu kirjautumisnäkymään. Kirjautuminen onnistuu syöttämällä olemassa oleva myymälätunnus ja salasana syötekenttiin ja painamalla login painiketta.

#### Uuden myymälätunnuksen luominen:

Jos käyttäjä ei ole rekisteröitynyt vielä, hän voi siirtyä kirjautumisnäkymästä 'register' painikkeella uuteen ikkunaan. Siellä hän voi syöttää myymälänumeron, salasanan
sekä salasanan vahvistuksen syötekenttiin.  
Salasanan tulee olla vähintään kahdeksan merkin pituinen ja sisältää sekä kirjaimia että numeroita.
Vain ensimmäisenä luodulle uudelle myymälälle löytyy edellisen vuoden toteutuneet luvut tietokannasta. Jos rekisteröityy toisen kerran uutena käyttäjänä, voi tällä hetkellä laskea vain kuvitteellisen vuositavoitteen ja henkilöstöbudjetin.

#### Budjetin ja henkilöstökustannusten tavoitteiden asettaminen:

Kirjautumisen jälkeen avautuu ensimmäinen myymälänäkymä. Siinä näkyy myymälän edellisen tuloskauden koko myynti. Käyttäjä voi kokeilla eri kasvutavoitteita joiden mukaan
laskuri laskee tämän tuloskauden myyntitavoitteen. Kasvutavoite annetaan prosenttilukuna.  
Kun kasvutavoite on annetta, voidaan tuloskauden budjetista laskea henkilöstökuluihin käytettävä summa. Käyttäjä voi taas kokeilla eri lukuja ja näytölle tallentuu
aina viimeisin luku euroina. Henkilöstökuluihin menevä osuus syötetään prosenttilukuna.  

Jos siis edellisen tuloskauden myynti on ollut 1 457 020€ ja henkilö laittaa vuotuisaksi kasvutavoitteeksi 5%, tulee tulevan vuoden tavoitteeksi 1 529 871€.
Tästä tavoitteesta käyttäjä suunnittelee, että voisi käyttää henkilöstökustannuksiin 12% ja syöttää luvun syötekenttään. 
Henkilöstöbudjetiksi tulostuu tällöin 183 585€.

#### Avainlukujen laskeminen: 

Kun käyttäjä on asettanut myyntitavoitteet, voi hän siirtyä seuraan näkymään painikkeella Move to Kpi. Tässä näkymässä näkyy koko tuloskauden budjetti annetun kasvutavoitteen mukaisesti. Tällä hetkellä tavoite on karkeasti jaettu kuukausitasolle vain jakamalla koko vuoden tavoite 12. Jatkossa tähän voisi käyttää algoritmiä joka osaa laskea tavoitteen sesonkien mukaisesti. Näkymässä näkyy myös edellisen vuoden vastaavan kuukauden myynti sekä sen erotus tavoitteeseen prosentuaalisesti.  
Seuraavana on listattuna edellisen tuloskauden vastaavan kuukauden avainlukutavoitteet. Näiden perusteella käyttäjä voi laskea tavoitteita kuluvalle tuloskaudelle. Kun kaikki uudet avainlukutavoitteet on syötetty kenttiin ja vahvistettu confirm painikkeella, käyttäjä voi laskea niiden perusteella toteutuvan myynnin. Jotta tämän vuoden budjetti toteutuisi, voi käyttäjä kokeilla useita eri kasvutavotteita ja laskea toteutuvan kuukausimyynnin aina uudestaan.  
Käyttäjä voi siirtyä edelliselle sivulle jos hän haluaa uudestaan muokata koko vuoden kasvutavoitetta, mutta silloin avainluvut eivät tallennu tietokantaan.
Käyttäjä voi milloin vain kirjautua ulos log out painikkeella.

