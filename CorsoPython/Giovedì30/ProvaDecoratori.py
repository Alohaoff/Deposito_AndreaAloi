# def decoratore(funzione):
#     def wrapper():
#         print("Prima dell'esecuzione della funzione")
#         funzione()
#         print("Dopo l'esecuzione della funzione")    
#     return wrapper

# @decoratore
# def saluta():
#     print("Ciao!")
    
# saluta()


# def decoratore_con_argomenti(funzione):
#     def wrapper(*args, **kwargs):     #così posso inserire argomenti infiniti alla funzione successiva al decoratore
#         print("Prima")
#         risultato = funzione(*args, **kwargs)
#         print("Dopo")
#         return risultato
#     return wrapper

# @decoratore_con_argomenti
# def somma(a, b):
#     return a + b

# print(somma(3, 4))

# def decoratore_con_argomento_singolo(funzione2):
#     def wrapper(*args):         #così posso inserire un solo argomento alla funzione successiva al decoratore
#         print("Prima")
#         risultato = funzione2(*args)
#         print("Dopo")
#         return risultato
#     return wrapper

# @decoratore_con_argomento_singolo
# def quadrato(a):
#     return a**2

# print(quadrato(2))


# def logger(funzione):
#     def wrapper(*args, **kwargs):
#         print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
#         risultato = funzione(*args, **kwargs)
#         print(f"Risultato di {funzione.__name__}: {risultato}")
#         return risultato
#     return wrapper

# @logger
# def moltiplica(a, b):
#     return a * b

# # Chiamata alla funzione decorata
# moltiplica(3, 4)