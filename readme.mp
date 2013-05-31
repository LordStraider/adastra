Projekt Django - JqueryUI - TDDD27
Jonathan Karlsson - jonka293 - 890201-1991 30 maj 2013


Länk till screencast: http://www.youtube.com/watch?v=o1-Xxaq5Fsk


Detta projekt är skapat i django, jquery samt jquery ui

För att köra projektet krävs python med django installerat samt en browser med javascript aktiverat.
Kopiera koden med "git clone git@gitlab.ida.liu.se:jonka293/djangojquerycontroller.git"
Gå till stället där manage.py ligger och kör "python manage.py runserver" så startar servern.
Öppna en browser och skriv in addressen "localhost:8000" så kommer du till förstasidan.

Struktur:

templates:
Här ligger .html filerna, där skapas all html via javascript med innehåll från djangos databas (sqlite3)
Det finns två html filer som är av intresse, index.html som är den vanliga vyn som alla har tillgång till
samt adminindex.html som bara admins har tillgång till, där man kan göra mer saker som att modifera innehållet.

static:
Här ligger alla filer som används, i form av css, java och bilder. Bilder som användaren laddar upp hamnar i en 
egen kategori.

Server:
Här ligger filer för att hantera django.
settings.py där man gör alla inställningar, specificerar var template och static ligger, sätter upp databaslänkar,
lägger till applikationer till sidan osv.
I urls.py ligger de sidor som används av sidan med länkar till funktioner i min applikation.

dataManager:
Detta är den applikation jag skapat för hemsidan. Jag har lagt allt i denna eftersom jag inte riktigt visste
vad jag ville göra, egentligen vill man ju dela upp applikationerna för att få en snygg struktur samt att man
kan återanvända applikationerna senare i livet.


Strukturer:
Klienten gör requests till serverns olika funktioner via urls.py, svaret kommer i json objekt som klienten får 
iterera för att hämta ut relevant data. När klienten skickar data till servern för att göra en uppdatering av menyer 
eller innehåll på någon sida så sker detta genom ajax och json.

Lite olika strukturer för json-objekt:
	Menyer:	
		{"menu": "menyn", "subs": [{"sub": "dropdown1", "linked": "/fileLoader/dropdown1"}], "linked": "menyn"}

		Detta ger alltså en meny med en undermeny i form av ett album, hade inte 'fileLoader' varit med hade det 
		varit en vanlig sida.

	Album:
		[{"title": "rubrik"}, {"path": "länk till albumet"}, {"fileLoader": "namn på fil"}, {"fileLoader": ...

		Finns flera filer så läggs alltså flera 'fileLoaders' på, klienten kommer sedan att iterera alla dessa
		'fileLoaders' och lägga in dem i sin html kod.

		Album lagras i databasen på formen:
		Titel, beskrivning:bild.jpg, beskrivning:bild.jpg

	Sidor:
		{"admin": true, "siteContent": "text", "extra": "EXTRA"}'

		Det spännande här är det EXTRA som är i form av bilder och listor.
		Listor och bilder ser ut såhär i databasen,
		listor: _Extra_List_Linker_0:listElement_-_listElemen:listElement_-_listElement
		Bilder: _Extra_Image_Linker_2:static/images/contentImages/im1.jpg_-_234_-_529

		Alla element i listan separeras alltså av '_-_' eftersom jag använder ',' för att separera själva listorna
		och ':' för att separera det element jag använder för att länka listan till ett ställe i texten.
		De två sista siffrorna i bilden definierar höjd och bredd.



Kommentarer:

Tanken med denna sida är att vem som helst ska kunna titta runt på sidan, läsa all text och se på bildgallerier.
Har man ett facebookkonto så kan man logga in på sidan, då skapas ne ny användare i databasen. Har man fått högre
behörighet så kan man gå till localhost:8000/administrationpage och där få se en liknande vy som tidigare.

Här finns en "Manage menu" knapp där man ser alla menyer, man kan här ta bort menyer och undermenyer, lägga till 
nya menyer och undermenyer, samt genom att klicka och dra kan man flytta om menyerna. Man sparar sina förflyttningar
genom att trycka på "Submit re-ordering"

Går man till en annan sida så ser man ett textfält där man kan ändra den befintliga informationen på sidan. 
Även här så trycker man på "Submit" för att skicka in sina ändringar.

Övrigt:

Detta är första gången jag gör en såhär avancerad hemsida och har aldrig jobbat med django eller jquery tidigare. Jag 
är trots detta nöjd med resultatet och detta kommer att leda till en hemsida som ett företag kommer använda sig av. 
I framtiden kommer nyheter som skrivs in på sidan länkas till facebook och folk kommer att kunna kommentera saker på 
sidan via facebook, fler features kommer även att komma till.

Jag har lärt mig mycket under kursens gång om hur django fungerar i helhet så väl som jquery men framför allt hur man 
på ett korrekt sätt skapar hemsidor då jag tidigare bara tittat på php där man i princip tagit första bästa lösning, 
denna sida anser jag är både tydlig, trevlig och lätt att lägga till funktionalitet.
