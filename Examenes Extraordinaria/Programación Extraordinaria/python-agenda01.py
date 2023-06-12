#Programa Agenda por Rafa

agenda = [["nombre","telefono","email"]]

def miAgenda():
    print("Introduce el nuevo nombre en la agenda")
    nombre = input()
    print("Introduce el nuevo numero de telefono")
    telefono = input()
    print("Introduce el correo")
    correo = input()
    # antes de hacer nada mas, lo metemos en la lista, y sacamos la lista
    agenda.append([nombre,telefono,correo])
    print(agenda)
    miAgenda()

miAgenda()
          

