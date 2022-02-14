import re
class Data:
    def __init__(self):
        self.Contendio=None
        self.Mes=None
        self.Año=None
        self.Productos=[]
        self.Existe=False
        self.GeneracionError=False
    
    def Separar(self):
        try:
            Listacabecera=re.findall(r"\s*([0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]+)\s*\:\s*([\d]+)\s*\=\s*\(\s*(.*)\s*\)",self.Contendio,flags=re.DOTALL)
            #print("1")
            ListaFinal=re.findall(r"\s*\[\"([0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]+[\s*[0-9a-zA-ZñÑáéíóúÁÉÍÓÚ]*]*)\"\s*\,\s*([\d]+\.?[\d]*)\s*\,\s*([\d]+)\s*\]\;?",Listacabecera[0][2])
            #print("2")
            self.Mes=Listacabecera[0][0]
            #print("3")
            self.Año=Listacabecera[0][1]
            #print("4")
            self.Productos=ListaFinal

            if len(self.Mes)>=1 and len(self.Año)>=1 and len(self.Productos)>=1:
                self.Existe=True
                self.GeneracionError=False
        except:
            print("[ERROR-DATA]: Error al guardar datos")
            self.GeneracionError=True
                

    
    def Contenido(self,Contenido):
        self.Contendio=Contenido
    
    def __str__(self):
        String="Mes: "+self.Mes+" , Año: "+self.Año+".\n"+str(self.Productos)
        return String