nome = input("Inserisci il tuo nome: ")

while True:
    print("\nMenu:")
    print("1- Scegli un numero per scoprire se è primo")
    print("2- Esci")
    
    scelta = input("Fai la tua scelta: ")
    
    if scelta == "1":
        numero = int(input("Inserisci un numero: "))
        if numero <= 1:
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
        
    elif scelta == "2":
        print("Uscita dal programma")
        break