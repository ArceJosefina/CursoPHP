#creando una lista (se puede modificar)
lista = ['Josefina Arce','Santa Fe','True',1.62,1.62]

#creando una tupla (no se puede modificar)
tupla = ('Josefina Arce','Santa Fe','True',1.62,1.62)

#esto cambia
lista[1] = 'coronda'

#esto no es valido
#tupla[2] = 'maquinola'

#creando un conjunto (set) no se accede a elementos por indice y no almacena datos duplicados

conjunto = ['Josefina Arce','Santa Fe','True',1.62,1.62]
#print(conjunto[0]) no puede acceder al elemento

#CREANDO UN DICCIONARIO

diccionario = {
    'nombre' : 'josefina arce',
    'apellido' : 'santafe',
    'mayor de edad': 'True',
    'dato_duplicado': '1.62',
}
print (diccionario['nombre'])

