studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}

print(studente)

studente["età"] = 21
print(studente)

studente["città"] = "Roma"
print(studente)

print(studente.keys()) 
print(studente.values())
print(studente.items())
print(studente.get("regione"))

#per unire due liste di cui la prima faccia da chiavi e la seconda da valori
# for x, y in lista_chiavi, lista_valori:
#     dizionario[x] = y