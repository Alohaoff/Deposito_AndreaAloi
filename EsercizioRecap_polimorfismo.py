class Posto:
    def __init__ (self, _numero, _fila, _occupato = False):
        self._numero = _numero
        self._fila = _fila
        self._occupato = _occupato
        
    def prenota(self):
        if self._occupato:
            return ("Non è possibile prenotare questo posto.")
        else:
            self._occupato = True
            return ("Il posto è libero, prenotazione effettuata.")
            
    def libera_posto(self):
        if self._occupato:
            self._occupato = False
            return "Adesso il posto è libero."
        else:
            return "Il posto è già libero"
        
    def get_numro(self):
        return self._numero
    
    def get_fila(self):
        return self._fila
    
    def get_occupato(self):
        return self._occupato
    
class PostoVIP(Posto):
    def __init__(self, _numero, _fila, _occupato = False, _lounge=False, _cameriere=False):
        super().__init__(_numero, _fila, _occupato)
        self._lounge = _lounge
        self._cameriere = _cameriere
        
    def prenota(self):
        risultato = super().prenota()  
        
        if risultato == "Il posto è occupato.":
            return "Non è possibile prenotare questo posto"
        
        self._lounge = True
        self._cameriere = True
        return "Prenotazione effettuata. Servizi VIP attivati: Lounge e Cameriere privato."
    
class PostoStandard(Posto):
    def __init__(self, _numero, _fila, _costo, _occupato = False):
        super().__init__(_numero, _fila, _occupato)
        self._costo = _costo
        
    def prenota(self):
        risultato2 = super().prenota()  
        
        if risultato2 == "Il posto è occupato.":
            return "Non è possibile prenotare questo posto"
        
        return f"Prenotazione effettuata. Il costo del biglietto è {self._costo}€ più commissioni."    
    
class Teatro:
    numeri_disp = range(1, 11)
    file_disp = ["A", "B", "C", "D"]
    
    def __init__(self):
        self._posti = []  
        self._posti_prenotati = []

#aggiungo Teatro. a numeri_disp e file_disp perchè sono attributi della classe      
    def aggiungi_posto(self, numero, fila):
        if numero in Teatro.numeri_disp and fila in Teatro.file_disp:
            posto = (numero, fila)
            if posto not in self._posti:
                self._posti.append(posto)
        
    def prenota_posto(self, numero, fila):
        posto = (numero, fila)
        for p in self._posti:
            if p == posto:
                break
        for p in self._posti_prenotati:
            if p == posto:
                return "Il posto è già stato prenotato."
        self._posti_prenotati.append(posto)
        return "Prenotazione effettuata."
            
    def stampa_posti_occupati(self):
        if self._posti_prenotati:
            print("Posti prenotati:")
            for numero, fila in self._posti_prenotati:
                print(f"Fila {fila}, Numero {numero}")
        else:
            print("Nessun posto prenotato.")

########## TEST
teatro = Teatro()

# posti disponibili
teatro.aggiungi_posto(1, "A")
teatro.aggiungi_posto(2, "B")
teatro.aggiungi_posto(3, "C")
teatro.aggiungi_posto(4, "D")
teatro.aggiungi_posto(1, "A")  
teatro.aggiungi_posto(11, "D")  

# prenotazioni
print(teatro.prenota_posto(1, "A"))  
print(teatro.prenota_posto(2, "B"))  
print(teatro.prenota_posto(1, "A"))  
print(teatro.prenota_posto(10, "Z")) # Problema

# lista posti occupati
teatro.stampa_posti_occupati()
