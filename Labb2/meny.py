import json
import sys
användare = []
lista = []


def meny():
    print("1. läs in fil")
    print("2. visa json data")
    print("3. lägg till ny person")
    print("4. ta bort person")
    print("5. spara fil")
    print("6. avsluta")
    menyVal = input()
    while True:
        if menyVal == "1":
            läsfil('personer.csv', 'text/')
            meny()
            break
        elif menyVal == "2":
            visaJson = läsJson('personer.json')
            print(visaJson)
            meny()
            break
        elif menyVal == "3":
            läsJson('personer.json')
            läggTillPerson()
            meny()      
            break
        elif menyVal == "4":
            läsJson('personer.json')
            tabortPerson()
            meny()
            break
        elif menyVal == "5":
            print("din fil är sparad")
            sparaPerson('personer.json')
            meny()
            break
        elif menyVal == "6":
            sys.exit
            break
        else:
            print("Du måste skriva in rätt värde i menyn")
            print("försök igen")
            meny()
            break

def läsfil(filename, path='text/'):
    global användare #global gör att jag kan modifiera listan användare utan att vara i själva listan
    fil = path + filename
    try: #jag försöker öppna filen går inte det så kommer den att gå till exept och skicka ut felmedelande
        with open(fil, encoding='utf-8') as helaFilen: #sparar ner filen samt att den blir encodad med utf-8
            for x in helaFilen: #göt en forloop för varje
                lista.append(x) # lista.append sparar ner allt som har skrivits i x i detta fal
    except FileNotFoundError as fel: #kollar om filen finns annars så kommer den att skicka ut att den inte finns
        print(fel)
        return None

    for x in lista: #gör en ny for loop som går igenom listan
        user = x.rstrip("\n").split(";") #den kommer spara ner till user samt ta bort \n i slutet av meningen samt splita 
        användare.append({"namn": user[0], #skriver in en ny lista för användare samt en ny dic för de olika sakerna samt
                          "efternamn": user[1], #att den delar user för varje split som görs och lägger in den i dictinonaryn
                          "användarnamn": user[2],
                          "email": user[3]})
    sparaPerson('personer.json')#kallar på metoden för att spara ner till json fil


def läsJson(filename): #läser in till en json fil
    global användare
    try: #för att kolla om det finns någon fil annars skicka till exept
        with open(filename, "r", encoding="utf-8") as läsa: #läser filen med utf-8
            användare = json.load(läsa) #json.load används för att läsa in data till en fil
            return användare
    except FileNotFoundError as fel:
        print(fel)
    sparaPerson('personer.json') #sparar ner filen när man har gått igenom funktionen


def läggTillPerson():
    global användare
    try:
        namn = input("skriv in namn: ") #tar input för varje fråga sedan skriver in det till dict och sedan sparar filen
        efternamn = input("skirv in efternamn: ")
        användarnamn = input("skriv in användarnamn: ")
        email = input("skriv in email: ")
        användare.append({
            "namn": namn,
            "efternamn": efternamn,
            "användarnamn": användarnamn,
            "email": email})
        sparaPerson('personer.json')
    except Exception as fel:
        print(fel)    


def sparaPerson(filename):
    global användare
    try:
        with open(filename, "w", encoding="utf-8") as spara: #anväder "W" för att skriva in i filen så varje gång man använder
            json.dump(användare, spara, ensure_ascii=False, indent=1)#fuktionen så skriver man till den nuvarande json filen
    except FileNotFoundError as fel:
        print(fel)


def tabortPerson():
    global användare
    läsJson('personer.json')
    try:
        räknare = 0 #en räknare som håller koll på vilken rad i json filen den är på
        user = input("skriv in användarnamnet på personen du vill ta bort: ")
        for x in användare:
            if user == x['användarnamn']: #kollar efter användarens input i listan som finns och om den fins så tar programet 
                användare.pop(räknare) #bort det som finns på den raden som räknaren kommer upp till för den ökas med en 
            räknare += 1 #för varje loop
    except ValueError as fel:
        print(fel)
    sparaPerson('personer.json')