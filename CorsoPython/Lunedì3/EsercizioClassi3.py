class Libro:
    titolo = ""
    autore = ""
    pagine = 0
   
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = int(pagine)
        
    def stampa_info(self):
        print("Il libro", self.titolo,"è stato scritto da", self.autore, "ed ha", self.pagine, "pagine")   

class Biblioteca:
    
    lista_libri=[]
    
    def crea_libro(self):
        
        titolo = input("Titolo: ")
        autore=input("Nome Autore: ")
        pagine= int(input("Numero Pagine: "))
        
        aggiunta= Libro(titolo, autore, pagine)
        self.lista_libri.append(aggiunta)
        
    def stampa_libro(self):
        for x in self.lista_libri:
            x.stampa_info()   
             
biblio = Biblioteca()

while True:
    
    biblio.crea_libro()
    biblio.stampa_libro()
    
    scelta= input("Vuoi continuare? si/no")
    if scelta == "no":
        break