def mayor_edad(personas_dicc):
    mayores_lista = []
    for nombre, edad in personas_dicc.items():
        if (edad >= 18):
            mayores_lista.append(nombre)
        
    return mayores_lista

personas = {
    'Ana': 17,
    'Luis': 21,
    'Marta': 19,
    'Pedro': 18,
    'Lucía': 25
}
resul = mayor_edad(personas)
print(resul)
