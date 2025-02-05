class MembroSquadra:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
        
    def __str__(self):
        return f"{self.nome}, {self.età} anni."

class Giocatore(MembroSquadra):
    
    def __init__(self, nome, età, ruolo, numero_maglia):
        MembroSquadra.__init__(self, nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
    def titolare (self):
        return f"{self.nome} giocherà titolare domenica con la maglia numero {self.numero_maglia}."
    
class Allenatore(MembroSquadra):
    
    def __init__(self, nome, età, modulo):
        MembroSquadra.__init__(self, nome, età)
        self.modulo = modulo
        
        
    def tattica (self):
        return f"{self.nome} usa spesso il {self.modulo}."

class Assistente(MembroSquadra):
    
    def __init__(self, nome, età, specializzazione):
        MembroSquadra.__init__(self, nome, età)
        self.specializzazione = specializzazione
        
    def aiuto (self):
        return f"{self.nome}, assistente della squadra, ha il ruolo di {self.specializzazione}."
        
#### TEST        
# giocatore = Giocatore("Lukaku", 30, "attaccante", 9)
# allenatore = Allenatore("Antonio Conte", 55, "4-3-3")
# assistente = Assistente("Cristian Stellini", 52, "Allenatore in seconda")

# print(giocatore)
# print(allenatore)
# print(assistente)
# print(giocatore.titolare())
# print(allenatore.tattica())
# print(assistente.aiuto())