import ClassiEsercizioSquadra

class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.membri_squadra = []

    def aggiungi_membro(self, membro):
        self.membri_squadra.append(membro)
        
    def stampa_squadra(self):
        return self.membri_squadra
    
    
squadra = Squadra(input("Inserisci il nome della squadra che vuoi creare: "))

while True:
    print("COSTRUIAMO LA SQUADRA!")
    print("1 - Aggiungi un Giocatore")
    print("2 - Aggiungi un Allenatore")
    print("3 - Aggiungi un Assistente")
    print("4 - Mostra la squadra")
    print("5 - Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        nome = input("Nome del giocatore: ")
        età = int(input("Età del giocatore: "))
        ruolo = input("Ruolo: ")
        numero_maglia = int(input("Numero di maglia: "))
        giocatore = ClassiEsercizioSquadra.Giocatore(nome, età, ruolo, numero_maglia)
        squadra.aggiungi_membro(giocatore)
        print(giocatore.titolare())

    elif scelta == "2":
        nome = input("Nome dell'allenatore: ")
        età = int(input("Età dell'allenatore: "))
        modulo = input("Modulo di gioco preferito: ")
        allenatore = ClassiEsercizioSquadra.Allenatore(nome, età, modulo)
        squadra.aggiungi_membro(allenatore)
        print(allenatore.tattica())

    elif scelta == "3":
        nome = input("Nome dell'assistente: ")
        età = int(input("Età dell'assistente: "))
        specializzazione = input("Specializzazione: ")
        assistente = ClassiEsercizioSquadra.Assistente(nome, età, specializzazione)
        squadra.aggiungi_membro(assistente)
        print(assistente.aiuto())

    elif scelta == "4":
        membri = squadra.stampa_squadra() 
        if membri:
            print("Squadra:", squadra.nome)
            for membro in membri:
                print(membro)
        else:
            print("La squadra è vuota!")

    elif scelta == "5":
        print("Squadra creata con successo! Arrivederci!")
        break

    else:
        print("Scelta non valida, riprova.")
