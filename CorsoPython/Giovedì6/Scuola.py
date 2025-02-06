import EsercizioIncapsulamento

class Scuola:
    def __init__(self, nome=""):
        self.nome = nome
        self.studenti = []  
        self.professori = [] 
    
    def imposta_nome(self, nome):
        self.nome = nome
            
    def aggiungi_studente(self, studente: EsercizioIncapsulamento.Studente):
        self.studenti.append(studente)
        
    def aggiungi_professore(self, professore: EsercizioIncapsulamento.Professore):
        if len(self.professori) < 4:
            self.professori.append(professore)
        else:
            print("Non è possibile aggiungere più di 4 professori.")
    #ho scelto di poter aggiungere solo quattro professori
    #perchè ho dato come possibilità di inserire solo quattro voti per alunno
            
    def mostra_studenti(self):
        for studente in self.studenti:
            print(studente.presentazione())
    
    def mostra_professori(self):
        for professore in self.professori:
            print(professore.presentazione())



scuola = Scuola() #istanza necessaria perchè le funzioni aggiunta dipendono dall'istanza
    
while True:
    print("\nMenu Scuola:")
    print("(Per prima cosa, scegli il nome della scuola)")
    print("1. Imposta Nome Scuola")
    print("2. Aggiungi Studente")
    print("3. Aggiungi Professore")
    print("4. Mostra Studenti")
    print("5. Mostra Professori")
    print("6. Esci")
    scelta = input("Seleziona un'opzione: ")
#per ogni if ho aggiunto la clausola di aggiunta del nome perchè ho bisogno che l'istanza abbia un valore
    
    if scelta == "1":
        nome_scuola = input("Inserisci il nome della scuola: ")
        scuola.imposta_nome(nome_scuola)
        print(f"Nome impostato: {scuola.nome}")
    
    elif scelta == "2":
        if not scuola.nome:
            print("Devi prima impostare il nome della scuola!")
            continue
        nome = input("Inserisci il nome dello studente: ")
        eta = int(input("Inserisci l'età dello studente: "))
        voto_italiano = int(input("Inserisci il voto di Italiano: "))
        voto_matematica = int(input("Inserisci il voto di Matematica: "))
        voto_storia = int(input("Inserisci il voto di Storia: "))
        voto_scienze = int(input("Inserisci il voto di Scienze: "))
        studente = EsercizioIncapsulamento.Studente(nome, eta, voto_italiano, voto_matematica, voto_storia, voto_scienze)
        scuola.aggiungi_studente(studente)
    
    elif scelta == "3":
        if not scuola.nome:
            print("Devi prima impostare il nome della scuola!")
            continue
        nome = input("Inserisci il nome del professore: ")
        eta = int(input("Inserisci l'età del professore: "))
        materia = input("Inserisci la materia insegnata: ")
        professore = EsercizioIncapsulamento.Professore(nome, eta, materia)
        scuola.aggiungi_professore(professore)
    
    elif scelta == "4":
        if not scuola.nome:
            print("Devi prima impostare il nome della scuola!")
            continue
        print("Studenti:")
        scuola.mostra_studenti()
    
    elif scelta == "5":
        if not scuola.nome:
            print("Devi prima impostare il nome della scuola!")
            continue
        print("Professori:")
        scuola.mostra_professori()
    
    elif scelta == "6":
        print("Uscita dal programma.")
        break
    
    else:
        print("Opzione non valida, riprova.")