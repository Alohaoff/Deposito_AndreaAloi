nome_utente = "Utente"
print("Premi 1 per aggiungere un elemento")
print("Premi 2 per modificare il testo")
print("Premi 3 per eliminare il testo")

scelta = int(input("Digita un numero"))

if scelta == 1 : 
   print("Hai selezionato aggiungere")
   elemento = input("inserisci la parte che vuoi aggiungere: ")
   print("Il tuo nuovo nome utente è:" + nome_utente + elemento)
elif scelta == 2 : 
   print("Hai selezionato modificare")
   elemento2 = input("scegli il tuo nuovo nome utente:")
   print("Il tuo nuovo nome utente è:" + elemento2)
elif scelta == 3 : 
   print("Hai eliminato il nome utente")
else : 
   print ("C'è un errore, riprova!")
   