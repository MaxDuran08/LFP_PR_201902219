#Menu

Menu=True
MenuLlave=[]
i=0
while i<2:
    Llave=False
    MenuLlave.append(Llave)
    i+=1

def StringMenu():
    print("**==========================**")
    print("|| 1. CARGAR DATA           ||")
    print("|| 2. CARGAR INSTRUCCIONES  ||")
    print("|| 3. ANALIZAR              ||")
    print("|| 4. GENERAR REPORTE       ||")
    print("|| 5. SALIR                 ||")
    print("**==========================**")
    print("|| SELECCIONE UNA OPCION    ||")
    print("**==========================**")

def ObtenerOpcion():
    while True:
        try:
            opcion=int(input())
            return opcion      
        except:
           print("ERROR: El dato ingresado no es un entero")
           StringMenu()

StringMenu()
opcion=ObtenerOpcion()

while Menu:
    if opcion==1:
        print("opcion1")

        MenuLlave[0]=True
    elif opcion==2:
        print("opcion2")

        MenuLlave[1]=True
    elif opcion==3:
        print("opcion3")
        if MenuLlave[0]==False or MenuLlave[1]==False:
            print("Fanltan datos por cargar")
        else:
            print("Analizando...")
    elif opcion==4:
        print("opcion4")
    elif opcion==5:
        print("SALIENDO...")
        Menu=False
    else:
        print("ERROR: La opcion no existe")
    if opcion!=5:
        StringMenu()
        opcion=ObtenerOpcion()