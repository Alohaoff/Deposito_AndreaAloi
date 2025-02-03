# class Automobile:
#     numero_di_ruote = 4
#     def __init__(self, marca, modello):    #__init__ = costruttore
#         self.marca = marca
#         self.modello = modello
#     def stampa_info(self):
#         print("L'automobile è una", self.marca, self.modello)
        
# auto1 = Automobile("Ferrari", "F40")
# auto2 = Automobile("Alfa Romeo", "Giulia")

# auto1.stampa_info()
# auto2.stampa_info()

class Pippo:
    aumento = 0
    
    def saluta():
        print("ciao Mirko")
        
    @classmethod
    def aumenta():
        Pippo.aumento += 1
        print(Pippo.aumento)
        
    @staticmethod
    def somma(a,b):
        return a + b
    
p = Pippo()

p.saluta()

p.aumenta()
Pippo.aumenta()

x = Pippo.somma(2,4)
