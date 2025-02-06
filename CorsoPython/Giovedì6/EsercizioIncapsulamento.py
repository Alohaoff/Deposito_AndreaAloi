class Persona:
    def __init__(self, nome: str, eta: int):
        self.__nome = nome
        self.__eta = eta
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, cambia_nome):
        self.__nome = cambia_nome
    
    def get_eta(self):
        return self.__eta
    
    def set_eta(self, cambia_eta):
        self.__eta = cambia_eta
    
    def presentazione(self):
        return f"Mi chiamo {self.__nome}, ho {self.__eta} anni."
    
class Studente(Persona):
    def __init__(self, nome, eta, voto_italiano, voto_matematica, voto_storia, voto_scienze):
        super().__init__(nome, eta)
        self.voti = [voto_italiano, voto_matematica, voto_storia, voto_scienze]
    
    def calcola_media(self):
        return sum(self.voti) / 4
    
    def presentazione(self):
        return f"{super().presentazione()} Sono uno studente e la mia media voti è {self.calcola_media()}."

class Professore(Persona):
    def __init__ (self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia
        
    def presentazione(self):
        return f"{super().presentazione()} Sono l'insegnante di {self.materia}."


stud1 = Studente("Andrea", 15, 6, 9, 7, 7)
print(stud1.presentazione())    
prof1 = Professore("Mario", 40, "Matematica") 
print(prof1.presentazione())


