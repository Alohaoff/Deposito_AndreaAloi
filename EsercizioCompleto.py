while True:
    scelta_entrata = input("Vuoi entrare nel menu: "). strip().lower()
    if scelta_entrata == "si":
        break
    else:
        print("Uscita dal programma")

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
    print("4. Cambia il numero scelto")
    print("5. Esci")
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        sommapari = 0
        for x in range(1, numero+1):
            if x % 2 ==0:
                sommapari += x
        print("La somma dei numeri pari: ", sommapari)
    
    elif scelta == "2":
        listadispari =[]
        for y in range(1, numero+1):
            if y % 2 != 0:
                listadispari.append(y)
        print("I numeri dispari sono:", listadispari)
            
    elif scelta == "3":
        if numero < 2:
            print("Il numero scelto non è primo")
        else:
            primo = True
            for z in range(2, numero):
                if numero % z == 0:
                    primo = False
            if primo:
                print("Il numero scelto è primo")
            else:
                print("Il numero scelto non è un numero primo")
        
    elif scelta == "4":
        controllo = True       
        while controllo:
            numero= int(input("Inserisci un numero intero positivo: "))
            if numero <= 0:
                print("Spiacente, devi inserire un numero positivo!")
            else:
                break
    
    elif scelta =="5":
        print("Uscita dal programma")
    
    else:
        print("Scelta non valida")