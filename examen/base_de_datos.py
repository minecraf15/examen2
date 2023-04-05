import mysql.connector  

class datos():

    def __init__(self):
        self.bd = mysql.connector.connect( host='localhost',
                                            database ='init', 
                                            user = 'root',
                                            port='3306',
                                            password ='')



    def inserta(self,proveedor,medicamentos,unidades,ingreso,estado,caducidad):
        curursor = self.bd.cursor()
        sentencia='''INSERT INTO articulos (proveedor,medicamentos,unidades,ingreso,estado,caducidad) VALUES ('{}','{}','{}','{}','{}','{}')'''.format(proveedor,medicamentos,unidades,ingreso,estado,caducidad)
        curursor.execute(sentencia)
        self.bd.commit()    
        curursor.close()

    def mostrar(self):
        cursor = self.bd.cursor()
        sentencia = "SELECT * FROM articulos " 
        cursor.execute(sentencia)
        registro = cursor.fetchall()
        return registro

    def mostrar_1(self, medicamentos):
        cur = self.bd.cursor()
        sentencia = "SELECT * FROM articulos WHERE medicamentos = {}".format(medicamentos)
        cur.execute(sentencia)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina(self,medicamentos):
        cur = self.bd.cursor()
        sentencia='''DELETE FROM articulos WHERE medicamentos = {}'''.format(medicamentos)
        cur.execute(sentencia)
        self.bd.commit()    
        cur.close()