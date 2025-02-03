class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = int(pagine)
    
    def stampa_info(self):
         print("Il libro", self.titolo,"è stato scritto da", self.autore, "ed ha", self.pagine, "pagine")
         
libro1 = Libro("Fra Codice", "Barney Stinson", 1000)

libro1.stampa_info()