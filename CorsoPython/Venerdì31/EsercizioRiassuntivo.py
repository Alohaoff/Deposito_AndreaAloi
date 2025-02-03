utenti=[]

while True:
    print("\nBenvenuto!")
    print("1. Registrati")
    print("2. Accedi")
    print("3. Esci")
    scelta = input("Scegli un'opzione: ")
        
    if scelta == "1":
        nuovoutente = input("Inserisci un nuovo username: ")
        nuovapass = input("Inserisci una nuova password: ")
        utenti.append((nuovoutente, nuovapass))
        print("Registrazione completata con successo!")  
          
    elif scelta == "2":
        for tentativi in range(3, 0, -1):
            user_accesso = input("Inserisci username: ")
            pass_accesso = input("Inserisci password: ")
        
            if (user_accesso, pass_accesso) in utenti:
                print("Accesso effettuato con successo!")
                #quiz()
            else:
                print("Errore: Username o password errati.") 
        else:
            print("Troppi tentativi falliti, la prossima volta scriviti le credenziali!.")
                    
    elif scelta == "3":
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida, riprova.")