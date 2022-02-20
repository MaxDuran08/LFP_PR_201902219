import re
class Lfp:
    def __init__(self):
        self.Contendio=None
        self.Nombre=None
        self.Grafica=None
        self.Titulo=None
        self.TituloX=None
        self.TituloY=None
        self.Existe=False
        self.GeneracionError=False
 
    def Contenido(self,Contenido):
        self.Contendio=Contenido

    def Separar(self):
        try:
            Contenido=self.Contendio
            II=re.findall(r"\s*\<\s*\¿(.*)\?\s*\>",Contenido,flags=re.DOTALL)
            #print(II)
            
            I=re.findall(r"([0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]+)\s*\:\s*\"([0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]+[\s*[0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]*]*)\"\s*\,*",II[0])
            #print(I)
            
            i=0
            while i<len(I):
                clave=str(I[i][0]).upper()
                valor=str(I[i][1])
                if str(I[i][0]).upper()==str("Nombre").upper():
                    #print("["+str(clave)+"]:"+str(valor))
                    self.Nombre=str(I[i][1])
                elif str(I[i][0]).upper()==str("Grafica").upper() or str(I[i][0]).upper()==str("Gráfica").upper():
                    #print("["+str(clave)+"]:"+str(valor))
                    self.Grafica=str(I[i][1])
                elif str(I[i][0]).upper()==str("Titulo").upper() or str(I[i][0]).upper()==str("Título").upper():
                    #print("["+str(clave)+"]:"+str(valor))
                    self.Titulo=str(I[i][1])
                elif str(I[i][0]).upper()==str("TituloX").upper() or str(I[i][0]).upper()==str("TítuloX").upper():
                    #print("["+str(clave)+"]:"+str(valor))
                    self.TituloX=str(I[i][1])
                elif str(I[i][0]).upper()==str("TituloY").upper() or str(I[i][0]).upper()==str("TítuloY").upper():
                    #print("["+str(clave)+"]:"+str(valor))
                    self.TituloY=str(I[i][1])
                i+=1
                
            if len(self.Nombre)>=1 and len(self.Grafica)>=1:
                self.Existe=True
                self.GeneracionError=False
            

        except:
            print("[ERROR-CARGA DE INSTRUCCIONES]: Error al guardar datos")
            self.GeneracionError=True
    
    def __str__(self):
        String="Nombre: "+str(self.Nombre)+" ,Grafica: "+str(self.Grafica)
        if self.Titulo!=None:
            String+=" ,Titulo: "+str(self.Titulo)
        if self.TituloX!=None:
            String+=" ,TituloX: "+str(self.TituloX)
        if self.TituloY!=None:
            String+=" ,TituloY: "+str(self.TituloY)
        String+="."
        return String