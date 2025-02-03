class Ristorante:

    def __init__(self, nome_ristorante, cucina):
        self.nome_ristorante = nome_ristorante
        self.cucina = cucina
        self.aperto = False
        self.lista_piatti = []
        self.lista_prezzi = []
        
    def descrivi_ristorante(self):
        print("Il ristorante", self.nome_ristorante , "offre una cucina",  self.cucina, ".")

    def apertura(self):
        if self.aperto == False:
            print("Il ristrante è chiuso.")
        else:
            print("Il ristorante è aperto.") 
            
    def apri_ristorante(self):
        self.aperto = True
        print("Sto aprendo.")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print("Sto chiudendo.")
        
    def aggiunte_menu(self, piatto, prezzo):
        self.lista_piatti.append(piatto)
        self.lista_prezzi.append(prezzo)
        print(piatto, "è stato aggiunto al menu e costa", prezzo, "€.")
        
    def rimozione_menu(self, piatto):
        if piatto in self.lista_piatti:
            indice = self.lista_piatti.index(piatto)
            self.lista_piatti.pop(indice)
            self.lista_prezzi.pop(indice)
            print(piatto, "è stato rimosso dal menu.")
            
    def stampa_menu(self):
        print("Menu del ristorante:")
        for i in range(len(self.lista_piatti)):
            print("- ", self.lista_piatti[i], "        ", self.lista_prezzi[i], "€")
            
            
            
mioristo = Ristorante("Mangia Bonito", "spagnola")

# Test dei metodi
mioristo.descrivi_ristorante()
mioristo.apertura()
mioristo.apri_ristorante()
mioristo.apertura()

# Modifica del menu
mioristo.aggiunte_menu("Tortilla de papas", 6)
mioristo.aggiunte_menu("Patatas bravas", 8)
mioristo.aggiunte_menu("Paella", 15)
mioristo.stampa_menu()
mioristo.rimozione_menu("Patatas bravas")
mioristo.stampa_menu()

# Chiusura del ristorante
mioristo.apertura()
mioristo.chiudi_ristorante()
mioristo.apertura()
