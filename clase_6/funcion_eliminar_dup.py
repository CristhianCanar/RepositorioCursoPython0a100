def eliminar_duplicados(lista_nombres):
    # Tratamiento
    elim_dup = set(lista_nombres)
    conv_lista = list(elim_dup)
    ord_lista = sorted(conv_lista)
    return ord_lista

nombres = ['Ana', 'Luis', 'Marta', 'Luis', 'Ana', 'Pedro']

print(eliminar_duplicados(nombres))