class Prodotto:
    
    deposito_prodotti = []
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        Prodotto.deposito_prodotti.append(self)
    
    def calcola_profitto(self):
        return (self.prezzo_vendita - self.costo_produzione)
    
    def stampa_deposito():
        for prodotto in Prodotto.deposito_prodotti:
            print("Nome: ", prodotto.nome)
            print("Costo Produzione: ", str(prodotto.costo_produzione))
            print("Prezzo Vendita: " + str(prodotto.prezzo_vendita))
            print("Profitto: " + str(prodotto.calcola_profitto()))

class Elettronica:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, anni_garanzia):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.anni_garanzia = anni_garanzia 
    
    def dettagli_prodotto(self):
        print("Nome: ", self.nome)
        print("Garanzia: ", str(self.garanzia), " anni")
        
class Abbigliamento:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale 
    
    def dettagli_prodotto(self):
        print("Nome: ", self.nome)
        print("Materiale: ", self.materiale)
        
class Fabbrica:

    inventario = {}

    def aggiorna_inventario():
        for prodotto in Prodotto.deposito_prodotti:
                nome_prodotto = prodotto.nome
                if nome_prodotto in Fabbrica.inventario:
                    Fabbrica.inventario[nome_prodotto] += 1
                else:
                    Fabbrica.inventario[nome_prodotto] = 1
                    
#    il for scorre i prodotti nella lista creata all'inizio,
##   poi nome_prodotto prende il nome per usarlo come chiave
###  e con if e else decido se aggiungere solo un'unità o un nuovo prodotto
             
    def stampa_inventario():
        print("Inventario della Fabbrica:")
        for nome, quantita in Fabbrica.inventario.items():
            print(nome, ":", quantita, "unità")

        # da qui lo ha fatto mirko
            
    def aggiungi_prodotto(self, prodotto, quantita=1):
        # Recupera il nome del prodotto tramite il metodo get_nome (definito nelle classi specifiche)
        nome_prodotto = prodotto.get_nome()
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
        else:
            self.inventario[nome_prodotto] = {'prodotto': prodotto, 'quantita': quantita}
        print("Aggiunte " + str(quantita) + " unità di " + nome_prodotto + " all'inventario.")

    def vendi_prodotto(self, nome_prodotto, quantita=1):
        if nome_prodotto in self.inventario:
            record = self.inventario[nome_prodotto]
            if record['quantita'] >= quantita:
                record['quantita'] -= quantita
                profitto = quantita * record['prodotto'].calcola_profitto()
                print("Vendute " + str(quantita) + " unità di " + nome_prodotto + ". Profitto realizzato: " + str(profitto))
            else:
                print("Inventario insufficiente per vendere " + str(quantita) + " unità di " + nome_prodotto + ". Quantità disponibili: " + str(record['quantita']))
        else:
            print("Prodotto " + nome_prodotto + " non trovato in inventario.")

    def resi_prodotto(self, nome_prodotto, quantita=1):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
            print("Resi " + str(quantita) + " unità di " + nome_prodotto + ".")
        else:
            print("Prodotto " + nome_prodotto + " non trovato in inventario. Impossibile processare il reso.")


             ###TEST
# prod1 = Elettronica("Smartphone", 200, 350, 1)
# prod2 = Elettronica("PC", 400, 800, 2)
# prod3 = Abbigliamento("Pantalone", 10, 25, "Jeans")
# prod4 = Abbigliamento("Giubotto", 50, 120, "Piuma")

# Prodotto.stampa_deposito()
# print("-----------")
# Fabbrica.aggiorna_inventario()
# Fabbrica.stampa_inventario()



