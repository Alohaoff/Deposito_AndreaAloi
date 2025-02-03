import random

def gioco_indovina_numero():
    numero_da_indovinare = random.randint(1, 100)
    return numero_da_indovinare 

numero_da_indovinare = gioco_indovina_numero()

while True:
    print("Prova ad indovinare il numero che sto pensando")
    scelta = input("Inserisci un numero (o scrivi 'exit' per uscire): ")

    if scelta.lower() == 'exit':
        print("Hai deciso di uscire dal gioco. Arrivederci!")
        break

    scelta = int(scelta)

    if scelta == numero_da_indovinare:
        print("Complimenti, hai indovinato!")
        break
    else:
        print("Mi dispiace, il numero non era questo")
