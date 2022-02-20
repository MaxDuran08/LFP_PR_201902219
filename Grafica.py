import matplotlib.pyplot as G
class Grafica:
    def __init__(self,Nombre,Grafica,Titulo,TituloX,TituloY,Contenido,Mes,Año):
        self.Nombre=Nombre
        self.Grafica=Grafica
        self.Titulo=Titulo
        self.TituloX=TituloX
        self.TituloY=TituloY
        self.Contenido=Contenido
        self.Mes=Mes
        self.Año=Año
        self.Crear()
    
    def Crear(self):
        """""
        String="Nombre: "+str(self.Nombre)+" ,Grafica: "+str(self.Grafica)
        if self.Titulo!=None:
            String+=" ,Titulo: "+str(self.Titulo)
        if self.TituloX!=None:
            String+=" ,TituloX: "+str(self.TituloX)
        if self.TituloY!=None:
            String+=" ,TituloY: "+str(self.TituloY)
        String+="."
        print(String+"\n"+str(self.Contenido))
        """
        
        GraficaTipo=str(self.Grafica).upper()
        ListaNombres=[]
        ListaGanancias=[]
        
        for producto in self.Contenido:
            ListaNombres.append(producto[0])
            #print(producto[0])
            Ganancia=float(producto[1])*float(producto[2])
            Ganancia=round(Ganancia,2)
            ListaGanancias.append(Ganancia)
        
        for recorrido in range(1,len(ListaGanancias)):
            for posicion in range(len(ListaGanancias)-recorrido):
                if ListaGanancias[posicion]<ListaGanancias[posicion+1]:
                    temp1=ListaGanancias[posicion]
                    temp2=ListaNombres[posicion]
                    ListaGanancias[posicion]=ListaGanancias[posicion+1]
                    ListaNombres[posicion]=ListaNombres[posicion+1]
                    ListaGanancias[posicion+1]=temp1
                    ListaNombres[posicion+1]=temp2
        """""
        for x in range(len(ListaGanancias)):
            print("[\""+ListaNombres[x]+"\",\""+str(ListaGanancias[x])+"\"]")
        """
        if self.Titulo==None or self.Titulo=="":
            self.Titulo="Reporte de Ventas "+str(self.Mes).upper()+" - "+str(self.Año)
        Guardado=str(self.Nombre)+".png"
        
        if GraficaTipo==str("Lineas").upper() or GraficaTipo==str("Líneas").upper():
            """""
            ListaNombresLineas=[]
            ListaGananciasLineas=[]
            for x in range(len(ListaGanancias)):
                if ListaNombres[x] not in ListaNombresLineas:
                    ListaNombresLineas.append(ListaNombres[x])
                    ListaGananciasLineas.append(ListaGanancias[x])
            """
            G.figure(figsize=(10,5))
            G.plot(ListaNombres,ListaGanancias)
            G.title(self.Titulo,size=16)
            if self.TituloX!=None or self.TituloX!="":
                G.xlabel(self.TituloX,size=16)
            if self.TituloY!=None or self.TituloY!="":
                G.ylabel(self.TituloY,size=16)
            G.savefig(Guardado)
            print("[ANALIZAR]: Se guardo la grafica de tipo:\""+GraficaTipo+"\", bajo el nombre: \""+Guardado+"\"")
            G.show()
        elif GraficaTipo==str("Barras").upper():
            G.figure(figsize=(10,5))
            G.bar(ListaNombres,ListaGanancias)
            G.title(self.Titulo,size=16)
            if self.TituloX!=None or self.TituloX!="":
                G.xlabel(self.TituloX,size=16)
            if self.TituloY!=None or self.TituloY!="":
                G.ylabel(self.TituloY,size=16)
            G.savefig(Guardado)
            print("[ANALIZAR]: Se guardo la grafica de tipo:\""+GraficaTipo+"\", bajo el nombre: \""+Guardado+"\"")
            G.show()
        elif GraficaTipo==str("Pie").upper() or GraficaTipo.upper==str("Píe").upper():
            G.figure(figsize=(10,5))
            G.pie(ListaGanancias,labels=ListaNombres)
            G.title(self.Titulo,size=16)
            G.savefig(Guardado)
            print("[ANALIZAR]: Se guardo la grafica de tipo:\""+GraficaTipo+"\", bajo el nombre: \""+Guardado+"\"")
            G.show()
            
        