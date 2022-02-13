import easygui
import os

class Read():
    def __init__(self):
        self.data=None
        self.lfp=None
    
    def LeerData():

        return True
    
    def LeerLFP():
        return True
    
    def ObtenerRuta():
        ruta=easygui.fileopenbox()
        return ruta
    
    def ObtenerDatosDocumento(extensionN,ruta,Tipo):
        while True:
            try:
                #ruta=easygui.fileopenbox()
                #ruta="C:\\Users\\Usuario\\Documents\\USAC\\Class\\LFP\\Lab\\Practica 1 Archivos de prueba\\salida.data"
                extension=os.path.splitext(ruta)
                if extension[1].upper()==extensionN.upper():
                    print("["+Tipo+"]La extension es correcta")
                    try:
                        Archivo=open(ruta,"r")
                        Contenido=Archivo.read()
                        Archivo.close()
                        print(Contenido)
                        break
                    except:
                        print("[ERROR]: Ocurrio un error al abrir el archivo")
                else:
                    print("[ERROR]: La extension del archivo es incorrecta")
            except:
                print("[ERROR]: Ocurrio un error al abrir el archivo")