nomeutente = "admin"
password = 1234

nomeutente_login = input("Inserisci il nome utente: ")
password_login = int(input("Inserrisci la password: "))

if nomeutente == nomeutente_login and password == password_login:
    print("Benvenuto,", nomeutente_login)
        
    modifica = int(input("Vuoi modificare nome utente o password? (1,2 o 3)"))
    print("1: Nome Utente")
    print("2: Password")
    print("3: Nessuna modifica")
    
    if modifica == 1:
        nu_modificato = input("Scegli il nuovo nome utente: ")
        print("Nome utente modificato.")
    elif modifica == 2:
        pw_modificato = input("Scegli la tua nuova password: ")
        print("Password modificata.")
    elif modifica == 3:
        print = ("Ok, non modifichiamo nulla")
    else:
        print("La tua scelta non è valida.")
        
            
    domanda = int(input("Ora devi impostare una domanda segreta: scegli la 1 o la 2?"))
    if domanda == 1:
        risposta = input("Inserisci il tuo colore preferito: ")
        print("Domanda segreta salvata.")
    elif domanda == 2:
        risposta = input("Inserisci il tuo animale preferito: ")
        print("Domanda segreta salvata.")    
    else:
        print("La tua scelta non è valida.")

else:
    print("Qualcosa non va, hai sbagliato il nome utente o la password.")    
