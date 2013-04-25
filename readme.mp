Projektspecifikation - TDDD27
Jonathan Karlsson - jonka293 - 890201-1991 16 april 2013

Projektförslag
En hemsida där vanliga användare ser en helt vanlig vacker hemsida med text och menysystem samt ett galleri, men där 
en administratör skall kunna ändra samtliga texter och även lägga till nya flikar i menyn. I bildgalleriet skall 
administratören kunna ta bort och lägga till bilder efter behag. Det skall även finnas funktionalitet för mejl så 
vanliga användare kan kommentera och skicka frågor på saker. Resultatet kommer bli en dynamisk sida som kan anpassas 
till många syften med en galleri av bilder.

Krav
prio 1  Server skall vara skriven i Django
prio 1  Klient skall vara skriven i JQuery
prio 1  Kommunikation mellan server och klient ska ske med json objekt innehållande ren data Klienten skapar HTML-koden
prio 1  Inloggade admins skall kunna modifiera all relevant text på sidan, samt lägga till nya flikar samt lägga till 
        bilder i galleriet
prio 1  Sidan ska känna av när mobiler och surfplattor ansluter och anpassa sidan efter detta
prio 1  All text och bilder skall länkas till en sqlite3 databas för att enkelt kunna mappa var texten finnes på hemsidan
prio 2  Besökare ska kunna kommentera sidan, varpå mejl skall skickas till sidansvariga prio 2 Avancerade JQuery menyer, 
        slide funktionalitet till mobiler
prio 3  Sidan skall vara estetiskt tilltalande, enligt mitt tycke

