class Posto:
    def __init__ (self, _numero, _fila, _occupato=False):
        self._numero = _numero
        self._fila = _fila
        self._occupato = _occupato
        
    def prenota(self):
        if self._occupato:
            return ("Non è possibile prenotare questo posto.")
        else:
            self._occupato = True
            return ("Il posto è libero, prenotazione effettuata.")

# posto = Posto(1, 'A')
# print(posto.prenota())  
# print(posto.prenota()) 
            
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