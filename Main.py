import easygui
import os
from Data import Data
from Grafica import Grafica
from LFP import Lfp
from Reporte import Reporte
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

def ObtenerContenido(extensionN,Tipo):
    Contenido=None
    while True:
        try:
            ruta=easygui.fileopenbox(title="Abre el archivo tipo \""+extensionN+"\"")
            #ruta="C:\\Users\\Usuario\\Documents\\USAC\\Class\\LFP\\Lab\\Practica 1 Archivos de prueba\\salida.data"
            extension=os.path.splitext(ruta)
            if extension[1].upper()==extensionN.upper():
                print("["+Tipo+"]: La extension es correcta")
                try:
                    Archivo=open(ruta,"r",encoding='utf-8')
                    Contenido=Archivo.read()
                    Archivo.close()
                    break
                except:
                    print("[ERROR-"+Tipo+"]: Ocurrio un error al abrir el archivo")
            else:
                print("[ERROR-"+Tipo+"]: La extension del archivo es incorrecta")
        except:
            print("[ERROR-"+Tipo+"]: Ocurrio un error al abrir el archivo")
    return Contenido

D=Data()
L=Lfp()
StringMenu()
opcion=ObtenerOpcion()

while Menu:
    if opcion==1:
        print("[OPCION]: CARGAR DATA\n[CARGA DE DATA]: Ingrese la direccion del archivo")
        try:
            D.Contenido(ObtenerContenido(".data","CARGA DE DATA"))
            D.Separar()
            #print(D)
            if D.Existe==True and D.GeneracionError==False:
                print("[CARGA DE DATA]: Archivo cargado correctamente")
                MenuLlave[0]=True
            elif D.Existe==True and D.GeneracionError==True:
                print("[ERROR-CARGA DE DATA]: Se mantendran los datos ingresados anteriormente")
        except:
            print("[ERROR-CARGA DE DATA]: Error")
    elif opcion==2:
        print("[OPCION]: CARGAR INSTRUCCIONES\n[CARGA DE INSTRUCCIONES]: Ingrese la direccion del archivo")
        try:
            L.Contenido(ObtenerContenido(".lfp","CARGA DE INSTRUCCIONES"))
            L.Separar()
            if L.Existe==True and L.GeneracionError==False:
                print("[CARGA DE INSTRUCCIONES]: Archivo cargado correctamente")
                MenuLlave[1]=True
                #print(L)
            elif L.Existe==True and L.GeneracionError==True:
                print("[ERROR-CARGA DE INSTRUCCIONES]: Se mantendran los datos ingresados anteriormente")
        except:
            print("[ERROR-CARGA DE INSTRUCCIONES]: Error")
    elif opcion==3:
        print("[OPCION]: ANALIZAR")
        if MenuLlave[0]==False or MenuLlave[1]==False:
            print("[ERROR-ANALIZADOR]: Faltan datos por cargar")
        elif MenuLlave[0]==True and MenuLlave[1]==True:
            Grafica(L.Nombre,L.Grafica,L.Titulo,L.TituloX,L.TituloY,D.Productos,D.Mes,D.Año)
    elif opcion==4:
        print("[OPCION]: GENERAR REPORTE")
        if MenuLlave[0]==False or MenuLlave[1]==False:
            print("[ERROR-GENERACION DE REPORTE]: Faltan datos por cargar")
        elif MenuLlave[0]==True and MenuLlave[1]==True:
            Reporte(D.Mes,D.Año,D.Productos)
    elif opcion==5:
        print("SALIENDO...")
        Menu=False
    else:
        print("[ERROR]: La opcion no existe")
    if opcion!=5:
        StringMenu()
        opcion=ObtenerOpcion()