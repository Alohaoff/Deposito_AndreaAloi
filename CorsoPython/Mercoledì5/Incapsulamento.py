class Persona:
    __nome = "mirko"

    def get_nome(self):
       return self.__nome
        
    def set_nome(self,nomenuovo):
        self.__nome = nomenuovo        
        
mirko1 = Persona()
# print(mirko1.__nome)
print(mirko1.get_nome())
mirko1.set_nome("Andrea")
print(mirko1.get_nome())
