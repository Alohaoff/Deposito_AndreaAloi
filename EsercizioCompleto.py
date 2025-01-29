while True:
    scelta1 = input("Vuoi entrare nel menu: "). strip().lower()
    if scelta1 == "si":
        break
    else:
        print("Uscita dal programma.")

controllo = True       
while controllo:
    numero= int(input("Inserisci un numero intero positivo: "))
    if numero <= 0:
        print("Spiacente, devi inserire un numero positivo!")
    else:
        break

while True:
    print("\nMenu:")
    print("1. Calcola la somma dei numeri pari da 1 al numero scelto")
    print("2. Stampa tutti i numeri dispari da 1 al numero scelto")
    print("3. Verifica se il numero scelto è primo")
    print("4. Esci")
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
            sommapari = 0
            for x in range(2, numero, 2):
                sommapari += x
            print("La somma dei numeri pari: ", sommapari)
        