import time
import os
import sys
import hashlib

tiempo_inicio = time.time()
os.system("hashcat -m 0 -a 0 -D 2 -o /crackeado/crack_1.txt /Hashes/archivo_1 /diccionarios/diccionario_1.dict /diccionarios/diccionario_2.dict --potfile-disable")
tiempo_termino = time.time()
tiempo_1= tiempo_termino - tiempo_inicio

tiempo_inicio = time.time()
os.system("hashcat -m 10 -a 0 -D 2 -o /crackeado/crack_2.txt /Hashes/archivo_2 /diccionarios/diccionario_1.dict /diccionarios/diccionario_2.dict --potfile-disable")
tiempo_termino = time.time()
tiempo_2= tiempo_termino - tiempo_inicio

tiempo_inicio = time.time()
os.system("hashcat -m 10 -a 0 -D 2 -o /crackeado/crack_3.txt /Hashes/archivo_3 /diccionarios/diccionario_1.dict /diccionarios/diccionario_2.dict --potfile-disable")
tiempo_termino = time.time()
tiempo_3= tiempo_termino - tiempo_inicio

tiempo_inicio = time.time()
os.system("hashcat -m 1000 -a 0 -D 2 -o /crackeado/crack_4.txt /Hashes/archivo_4 /diccionarios/diccionario_1.dict /diccionarios/diccionario_2.dict --potfile-disable")
tiempo_termino = time.time()
tiempo_4= tiempo_termino - tiempo_inicio

tiempo_inicio = time.time()
os.system("hashcat -m 1800 -a 0 -D 2 -o /crackeado/crack_5.txt /Hashes/archivo_5 /diccionarios/diccionario_1.dict /diccionarios/diccionario_2.dict --potfile-disable")
tiempo_termino = time.time()
tiempo_5= tiempo_termino - tiempo_inicio

print("\n***********")
print("Tiempo para archivo 1: " + str(tiempo_1))
print("Tiempo para archivo 2: " + str(tiempo_2))
print("Tiempo para archivo 3: " + str(tiempo_3))
print("Tiempo para archivo 4: " + str(tiempo_4))
print("Tiempo para archivo 5: " + str(tiempo_5))

## Leyendo claves archivo_1

file = open('/crackeado/crack_1.txt' ,'r')
lista_archivos_1 = list()
char = 0
aux = 0
contrasenia= ""
for x in file:
    while char < len(x):
        if (aux == 1):
            contrasenia += x[char]
        if(x[char] == ":"):
            aux += 1
        char += 1    

    lista_archivos_1.append(contrasenia[0: len(contrasenia)-1])
    contrasenia =""
    aux = 0
    char = 0

file.close()

## Leyendo claves archivo_2
file = open('/crackeado/crack_2.txt', 'r')
lista_archivos_2 = list()
char = 0
aux = 0 
contrasenia = ""
for x in file:
    while char < len(x):
        if (aux == 2):
            contrasenia += x[char]
        if (x[char] == ":"):
            aux += 1
        char += 1

    lista_archivos_2.append(contrasenia[0: len(contrasenia)-1])
    contrasenia = ""
    aux = 0
    char = 0

file.close()

## Leyendo claves archivo_3
file = open('/crackeado/crack_3.txt', 'r')
lista_archivos_3 = list()
char = 0
aux = 0 
contrasenia = ""
for x in file:
    while char < len(x):
        if (aux == 2):
            contrasenia += x[char]
        if (x[char] == ":"):
            aux += 1
        char += 1

    lista_archivos_3.append(contrasenia[0: len(contrasenia)-1])
    contrasenia = ""
    aux = 0
    char = 0

file.close()

## Leyendo claves archivo_4
file = open('/crackeado/crack_4.txt', 'r')
lista_archivos_4 = list()
char = 0
aux = 0 
contrasenia = ""
for x in file:
    while char < len(x):
        if (aux == 1):
            contrasenia += x[char]
        if (x[char] == ":"):
            aux += 1
        char += 1

    lista_archivos_4.append(contrasenia[0: len(contrasenia)-1])
    contrasenia = ""
    aux = 0
    char = 0

file.close()

## Leyendo claves archivo_5
file = open('/crackeado/crack_5.txt', 'r')
lista_archivos_5 = list()
char = 0
aux = 0 
contrasenia = ""
for x in file:
    while char < len(x):
        if (aux == 1):
            contrasenia += x[char]
        if (x[char] == ":"):
            aux += 1
        char += 1

    lista_archivos_5.append(contrasenia[0: len(contrasenia)-1])
    contrasenia = ""
    aux = 0
    char = 0

file.close()
print("\n***********")

print("El largo del archivo 1 es:", len(lista_archivos_1))
print("El largo del archivo 2 es:", len(lista_archivos_2))
print("El largo del archivo 3 es:", len(lista_archivos_3))
print("El largo del archivo 4 es:", len(lista_archivos_4))
print("El largo del archivo 5 es:", len(lista_archivos_5))



rehash_1 =  list()
tiempo_inicio=time.time()
for i in lista_archivos_1:
    hash_aux=hashlib.sha512(i.encode("utf-8") ).hexdigest()
    rehash_1.append(hash_aux)
tiempo_termino =time.time()
print("El tiempo para hashear con SHA-512 el archivo 1 es:", tiempo_termino - tiempo_inicio)

rehash_2 =  list()
tiempo_inicio=time.time()
for i in lista_archivos_2:
    hash_aux=hashlib.sha512(i.encode("utf-8") ).hexdigest()
    rehash_2.append(hash_aux)
tiempo_termino =time.time()
print("El tiempo para hashear con SHA-512 el archivo 2 es:", tiempo_termino - tiempo_inicio)

rehash_3 =  list()
tiempo_inicio=time.time()
for i in lista_archivos_3:
    hash_aux=hashlib.sha512(i.encode("utf-8") ).hexdigest()
    rehash_3.append(hash_aux)
tiempo_termino =time.time()
print("El tiempo para hashear con SHA-512 el archivo 3 es:", tiempo_termino - tiempo_inicio)

rehash_4 =  list()
tiempo_inicio=time.time()
for i in lista_archivos_4:
    hash_aux=hashlib.sha512(i.encode("utf-8") ).hexdigest()
    rehash_4.append(hash_aux)
tiempo_termino =time.time()
print("El tiempo para hashear con SHA-512 el archivo 4 es:", tiempo_termino - tiempo_inicio)

rehash_5 =  list()
tiempo_inicio=time.time()
for i in lista_archivos_5:
    hash_aux=hashlib.sha512(i.encode("utf-8") ).hexdigest()
    rehash_5.append(hash_aux)
tiempo_termino =time.time()
print("El tiempo para hashear con SHA-512 el archivo 5 es:", tiempo_termino - tiempo_inicio)








