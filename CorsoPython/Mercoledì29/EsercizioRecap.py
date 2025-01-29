# # Esercizio 1

# numero = int(input("Inserisci un numero: "))

#   if (numero%2 == 0):
#       print("Il numero  è pari")
#   else:
#       print("Il numero è dispari")

    
# # Esercizio 2
# counter = True

# while counter:
#     numero2=int(input("Inserisci un numero positivo: "))
#     for rovescio in range (numero2, -1, -1):
#         print(rovescio)
#     if numero2 < 0:
#         print("Il numero non è valido")
#     scelta = input("Vuoi fermare il programma?")
#     if scelta == "si" :
#       counter = False
        
# Esercizio 3
# listanumeri = []
# controllo_lung = int(input("Quanto vuoi che sia lunga la lista? "))
# while len(listanumeri) < controllo_lung:
#     numero3 = int(input("Inserisci un numero: "))
#     listanumeri.append(numero3 **2)
#     print(listanumeri)

# Esercizio 4
listanumeri2 = []

while len(listanumeri2) < 5:
    numero4 = int(input("Inserisci un numero: "))
    listanumeri2.append(numero4)
    print(listanumeri2)

for num in range(1):
    max_numero4 = max(listanumeri2)
    
contatorenumeri = 0
while contatorenumeri< len(listanumeri2):
    contatorenumeri +=1
    
if len(listanumeri2) == 0:
    print("La lista è vuota")
else:
    print("Il numero più alto presente in lista è:", max_numero4)
    print("I numeri presenti nella lista sono:", contatorenumeri)