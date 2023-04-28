#Mensaje de bienvenida
print("\033[1m"+"\nBienvenid@ al programa."+"\033[0m")

# Bucle que pregunte al usuario si desea ejecutar el programa (si se ingresa un texto incorrecto le vuelve a preguntar.)
while True:
    # El usuario debe introducir desde teclado su desición.
    x = input("\n¿Desea ejecutar el programa? Si  o  No -> ").lower()

    if x == "si" or x == "no":
        break  
    else:
        print("\nPor favor ingrese algunas de las palbras claves 'Si' o 'No'")
        
# Función que contiene la logica del programa
def funcion():
    print("\033[1m"+"\nGracias por ejecutar el programa."+"\033[0m")

    # Variale con los nombres de los integrantes del grupo.
    nombres = ["Jeremy", "Karla", "Jonathan", "Bryan"]

    # datos generales de los integrantes del grupo:
    datos = ["Jeremy Odir.","Karla Patricia.","Bryan Alexis.","Jonathan Humberto.",
             "Fuentes Soriano.","Miranda Orellana.","Rauda Gómez.","Alas Landaverde.",
             "Masculino.","Femenino.",
             "17 años.","18 años.","19 años.",
             "Chalatenango.",
             "Concepción Quezaltepeque.","El Paraiso.",
             "Cantón Monte Redondo.","Barrio San José.","Cantón San José.","Barrio el centro."]

    print("\033[1m"+"\nMenú de integrantes\n"+"\033[0m")

    # Bucle for que muestra un menú de los integrantes del grupo.
    for i in nombres:
        print(i)

    # Contador para errores de eleccion en el menú.
    contador = 0
    
    # Bucle que pida al usuario que digite un nombre (si ingresa un nombre incorrecto le vuelve a pedir el nombre.)
    while True:
        
        # Petición de un nombre
        inte = input("\nIngrese un nombre de uno de los integrantes del menú anterior -> ").lower()

        # Condición que permita que el bulce se cierre cuando el usuario ingrese un dato correto o caso contrario que indique que se ha equivocado.
        if inte == "jeremy" or inte == "karla" or inte == "jonathan" or inte == "bryan":
            break

        else:
            # Cada vez que el usuario cometa un error se le sumará un valor al contador.
            contador += 1
            print("\nPor favor ingrese un nombre que esté en el menú.")

            if contador == 1:
                print("\033[1m"+f"\nSe ha equivocado {contador} vez."+"\033[0m")
            else:
                print("\033[1m"+f"\nSe ha equivocado {contador} veces."+"\033[0m")

    # Condición que muestre los datos del integrante de grupo indicaco por el usuario.
    # Integrante 1
    if inte == "jeremy":
        print(f'''
        Nombres: {datos[0]}
        Apellidos: {datos[4]}
        Sexo: {datos[8]}
        Edad: {datos[12]}
        Departamento: {datos[13]}
        Municipio: {datos[14]}
        Dirección: {datos[16]}''')
    # Integrante 2
    elif inte == "bryan":
        print(f'''
        Nombres: {datos[2]}
        Apellidos: {datos[6]}
        Sexo: {datos[8]}
        Edad: {datos[11]}
        Departamento: {datos[13]}
        Municipio: {datos[13]}
        Dirección: {datos[18]}''')
    # Integrante 3
    elif inte == "jonathan":
        print(f'''
        Nombres: {datos[3]}
        Apellidos: {datos[7]}
        Sexo: {datos[8]}
        Edad: {datos[10]}
        Departamento: {datos[13]}
        Municipio: {datos[15]}
        Dirección: {datos[19]}''')
    # Integrante 4   
    elif inte == "karla":
        print(f'''
        Nombres: {datos[1]}
        Apellidos: {datos[5]}
        Sexo: {datos[9]}
        Edad: {datos[10]}
        Departamento: {datos[13]}
        Municipio: {datos[13]}
        Dirección: {datos[17]}''')    

# Bucle que ejecute la funcion las veces que sea necesario.
while x == "si" or x == "s":

    # Condicion que permita romper el bulce cuando el usuario así lo desee
    if x == "no" or x == "n":
        break
        
    # Llamar la función.
    funcion()
    
    # Bucle que pregunte al usuario si desea volver a ejecutar el programa (si se ingresa un texto incorrecto le vuelve a preguntar.)
    while True:
        # Se le preguna al usuario si desea ejecutar el programa una vez mas.
        x = input("\n¿Desea volver a ejecutar el programa? Si  o  No -> ").lower()
        
        # Condicion que permita romper el bulce cuando el usuario ingrese un texto correcto (Si o NO)
        if x == "si" or x == "no":
            break
        else:
            print("\nPor favor ingrese algunas de las palbras claves 'Si' o 'No'")

# Mensaje que indique que el programa se dejo de ejecutar.     
print("\033[1m"+"\nLa ejecución del programa se finalizó.\n"+"\033[0m")