#Programa Agenda por Rafa

agenda = [["nombre","telefono","email"]]

# cargar registros
archivo = open("agenda.txt",'r')
for i in range(1,10):
    nuevalinea = archivo.readline().split(",")
    agenda.append(nuevalinea)

# estado de la agenda
print(agenda)

def miAgenda():
    # Menu Inicial
    print("Escoge tu opcion")
    print("1.-Introduce Nuevo Registro")
    print("2.-Listar Registros")
    print("3.-Buscar Registro")
    opcion = input()
    if opcion == "1":
        print("Introduce el nuevo nombre en la agenda")
        nombre = input()
        print("Introduce el nuevo numero de telefono")
        telefono = input()
        print("Introduce el correo")
        correo = input()
        # antes de hacer nada mas, lo metemos en la lista, y sacamos la lista
        agenda.append([nombre,telefono,correo])
        print(agenda)
        # Guardo en archivo
        archivo = open("agenda.txt",'a')
        longaniza = nombre+","+telefono+","+correo+"\n"
        archivo.write(str(longaniza))
        archivo.close()
    if opcion == "2":
        for i in range(1,len(agenda)):
            print(agenda[i])
    # Ejecucion Recursiva
    miAgenda()

miAgenda()
