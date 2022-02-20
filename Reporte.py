import os
import webbrowser
class Reporte:
    def __init__(self,Mes,Año,Productos):
        self.Mes=Mes
        self.Año=Año
        self.Productos=Productos
        self.n=""
        self.Crear()
    
    def Crear(self):
        Ruta=self.Calcular()
        Lista=[]
        
        for producto in self.Productos:
            Ganancia=float(producto[1])*float(producto[2])
            Ganancia=round(Ganancia,2)
            temp=[producto[0],producto[1],producto[2],Ganancia]
            Lista.append(temp)
        
        for recorrido in range(1,len(Lista)):
            for posicion in range(len(Lista)-recorrido):
                if Lista[posicion][3]<Lista[posicion+1][3]:
                    temp=Lista[posicion]
                    Lista[posicion]=Lista[posicion+1]
                    Lista[posicion+1]=temp

        html=   """
        <html>
        <title>
        Reporte """+str(self.n)+"""
        </title>
        <head>
        <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
        </head>
        <body style="background-color: #E7FAF8;">

        <font face="nunito,arial,verdana">

        <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
        <tbody style="border: hidden;">
        <tr style="border: hidden; height: 104px;">
        <td style="height: 90px; width: 8%; text-align: left;"><img src="https://i.ibb.co/xhT1W0r/escudo10.png" alt="Usac" width="100" height="100" border="0" /></td>
        <td style="height: 90px; width: 92%;">
        <h2><strong>Nombre: Max Rodrigo Dur&aacute;n Canteo</strong></h2>
        <h2><strong>RA: 201902219</strong></h2>
        </td>
        </tr>
        </tbody>
        </table>
        <h3 style="text-align: center;">PRODUCTOS VENDIDOS EL MES DE """+str(self.Mes).upper()+""" DEL A&Ntilde;O """+str(self.Año).upper()+"""</h3>
        <table style="height: 54px; width: 100%; border-collapse: collapse; margin-left: auto; margin-right: auto; border: black 3px solid;">
        <tbody>
        <tr style="height: 36px;background-color: #13b6a7">
        <td style="width: 25%; height: 36px; text-align: center; border: black 3px solid;">NOMBRE</td>
        <td style="width: 25%; height: 36px; text-align: center; border: black 3px solid;">PRECIO UNITARIO</td>
        <td style="width: 25%; height: 36px; text-align: center; border: black 3px solid;">UNIDADES VENDIDAS</td>
        <td style="width: 25%; height: 36px; text-align: center; border: black 3px solid;">GANANCIAS</td>
        </tr>
                """
        for p in Lista:
            html+="""
            <tr style="height: 18px;background-color: #FFFFFF">
            <td style="width: 25%; height: 18px; text-align: center; border: black 2px solid;">"""+str(p[0])+"""</td>
            <td style="width: 25%; height: 18px; text-align: center; border: black 2px solid;">"""+str(p[1])+"""</td>
            <td style="width: 25%; height: 18px; text-align: center; border: black 2px solid;">"""+str(p[2])+"""</td>
            <td style="width: 25%; height: 18px; text-align: center; border: black 2px solid;">"""+str(p[3])+"""</td>
            </tr>
            """
            
        for recorrido in range(1,len(Lista)):
            for posicion in range(len(Lista)-recorrido):
                if int(Lista[posicion][2])<int(Lista[posicion+1][2]):
                    temp=Lista[posicion]
                    Lista[posicion]=Lista[posicion+1]
                    Lista[posicion+1]=temp
        ProductoMax=Lista[0]
        ProductoMin=Lista[len(Lista)-1]
        

        html+="""
        </tbody>
        </table>
        <h3 style="text-align: center;">PRODUCTO MAS VENDIDO</h3>
        <p>El producto mas vendido fue:"""+str(ProductoMax[0]).lower()+""", con """+str(ProductoMax[2])+""" unidades vendidas generando una ganancia de """+str(ProductoMax[3])+""" Q.</p>
        <h3 style="text-align: center;">PRODUCTO MENOS VENDIDO</h3>
        <p>El producto menos vendido fue:"""+str(ProductoMin[0]).lower()+""", con """+str(ProductoMin[2])+""" unidades vendidas generando una ganancia de """+str(ProductoMin[3])+""" Q.</p>
        </font>
        </body>
        </html>
            """
        try:
            Reporte=open(Ruta,"w")
            Reporte.write(html)
            Reporte.close
            print("[GENERAR REPORTE]: Se guardo el archivo con el nombre: "+str(Ruta))
            try:
                Archivo="file:///"+os.getcwd()+"/"+Ruta
                webbrowser.open_new_tab(Archivo)
            except:
                print("[ERROR-GENERAR REPORTE]: Problema al abrir el archivo en el navegador")
        except:
            print("[ERROR-GENERAR REPORTE]: Problema al generar el reporte")
    
    def Calcular(self):
        n=None
        if self.n=="":
            n=0
            self.n=0
        else:
            n=self.n
        
        while True:
            ruta="Reporte"+str(n)+".html"
            Existe=os.path.exists(ruta)
            if Existe==True:
                n+=1
            else:
                self.n=n
                return ruta
        
        