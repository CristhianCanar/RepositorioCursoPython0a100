agenda = {}

def agregar_contacto(nombre, telefono):
    global agenda
    agenda[nombre] = telefono

def mostrar_agenda():
    for nombre, telefono in agenda.items():
        print(f"{nombre} → {telefono}")

agregar_contacto("Pedro", "31258888888")
agregar_contacto("Juan", "31258888888")
agregar_contacto("Alejo", "31258888888")
agregar_contacto("Maria", "31258888888")
agregar_contacto("Lu", "31258888888")

mostrar_agenda()
