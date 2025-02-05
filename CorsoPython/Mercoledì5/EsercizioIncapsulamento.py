class ContoBancario:
    def __init__(self):
        self.__titolare = "Andrea Aloi"
        self.__saldo = 5000.0
    
    # per poter vedere il titolare privato
    def get_titolare(self):
        return self.__titolare
    
    # per modificare il titolare
    def set_titolare(self, nuovo_titolare):
        if nuovo_titolare != "":
            self.__titolare = nuovo_titolare
    
    # per vedere il saldo privato  
    def get_saldo(self):
        return self.__saldo
    
    # per modificare il saldo  
    def set_saldo(self, aggiunta):
        self.__saldo += aggiunta
    
    #metodo per depositare    
    def deposita(self, importo):
        if importo > 0:
            self.set_saldo(+importo)
            print(f"{importo}€ versati con successo.")
        else:
            print("Errore: L'importo deve essere positivo.")
 
    #metodo per visualizzare
    def visualizza_saldo(self):
        return f"Saldo attuale: {self.get_saldo()}"        

    # metodo per prelevare
    def preleva(self, importo):
        if importo <= 0:
            print("Errore: L'importo del prelievo deve essere positivo.")
        elif importo > self.__saldo:
            print("Errore: Fondi insufficienti.")
        else:
            self.set_saldo(-importo)
            print(f"Prelievo di {importo}€ effettuato con successo.")
    
# TEST
conto = ContoBancario()
print(conto.get_titolare())
conto.set_titolare("Mario Rossi")
print(conto.get_titolare())
conto.deposita(120.5)
print(conto.visualizza_saldo())
conto.preleva(350.5)
conto.preleva(10000)
print(conto.visualizza_saldo())  
