nome_utente = "SuperMario"
password = "Andrea"
id_utente = 0

if nome_utente == "SuperMario" and password == "Andrea" and id_utente == 0:
   nome_utente = input("inserisci nome utente: ")
   password = input("seleziona la tua password: ")
   id_utente +=1
  
  #aggiungo questo if per essere certo di cadere nell'else
   if nome_utente == "SuperMario" and password == "Andrea" and id_utente == 0: 
       print("C'è stato un errore")
   else:
       print("Ti sei registrato! Benvenuto", nome_utente)
