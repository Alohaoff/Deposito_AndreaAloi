# numeri = [1,2,3,4,5]
# nomi = ["Andrea", "Mario", "Giulia"]
# misto = ["Andrea", 1, True, 0.16]

# print(misto)
# print(numeri[4])

# numeri[2] = 16
# print(numeri)

# print(len(numeri))

# numeri.append(6)
# print(numeri)

# numeri.insert(2, 9)
# print(numeri)

# numeri.remove(5)
# print(numeri)

# numeri.sort()
# print(numeri)

# cap= int(input("Inserisci il cap:"))
# misto.append(cap)
# print(misto)


# lista_utente = []
# id = 0

# while(len(lista_utente) <=3):
#     utente=[]
#     nome = input ("inserisci il tuo nome")
#     utente.append(nome)
#     password = input ("Inserisci la password")
#     utente.append(password)
#     id +=1
#     utente.append(id)

#     lista_utente.append(utente)
#     print(utente)
#     print(lista_utente)

#creare un sistema di if che al rispetto di certe condizioni
##predefinite aggiunga i valori corrispondenti ad una lista, in ordine crescente

lista_valori = []

valore1 = int(input("Aggiungi un valore numerico"))
valore2 = int(input("Aggiungi un valore numerico"))
valore3 = int(input("Aggiungi un valore numerico"))

if valore1 > 0 and valore2 > 0 and valore3 > 0 :
    lista_valori.append(valore3)
    lista_valori.append(valore1)
    lista_valori.append(valore2)
    
    if len(lista_valori) > 0:
        lista_valori.sort()
        
numeroValori = int(input("quanti valori vuoi aggiungere?"))
lista_valori2 = []

while len(lista_valori)<=numeroValori:
    valore = int(input("quale valore vuoi aggiungere?"))
    lista_valori2.append(valore)
    print(lista_valori2)
    
lista_valori2.sort()
lista_valori2.reverse()
print(lista_valori2)

###problemino