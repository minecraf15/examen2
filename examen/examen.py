import tkinter as tk
from tkinter import Label,Frame,ttk,PhotoImage,Entry
from base_de_datos import *

 
var=""
def venta():
 def iniciar_sesion():
    global var
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admistrador" and contrasena == "1234":
     resultado.config(text="Inicio de sesión exitoso")
     var="si"
     root.destroy()
    elif usuario == "proveedor" and contrasena == "1982":
     resultado.config(text="inicio sesion exitasamente")
     var="no"  
     root.destroy()
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")  
 global var 
   
 root=tk.Tk()
 root.geometry("300x200")
 root.wm_title("titulo")
 resultadox = tk.Label(text="password ")
 resultadox.place(x=100,y=60)
 nombre_usuario = tk.Entry()
 nombre_usuario.place(x=100,y=40)
 resultadol=tk.Label(text="user")
 resultadol.place(x=100,y=20)
 contrasena_usuario = tk.Entry(show="*")
 contrasena_usuario.place(x=100,y=80)
         
 iniciar_sion = tk.Button(text="Iniciar sesión", command=iniciar_sesion)
 iniciar_sion.place(x=100,y=100)
 resultado=tk.Label()
 resultado.place(x=100,y=120)
 root.mainloop()     

ventana=tk.Tk()
ventana.geometry("600x500+10+10")
ventana.title(" FONDOS DE PANTALLA ")

imagen=PhotoImage(file="lol.png")
iblimagen=Label(ventana,image=imagen).place(x=0,y=0)
iniciar_sesion=tk.Button(text=" inicio de sesion ",command=ventana.destroy)
iniciar_sesion.place(x=400,y=410)

ventana.mainloop()

if ventana.destroy:
    venta()
class admi(tk.Frame):
    def __init__(self,master):
       super().__init__(master)
       self.base_datos=datos()
       self.wigets()
        
        
    
    
    def wigets(self):
        fra1=Frame()
        fra2=Frame()

        label1=Label(fra1,text="CUENTA\n  DE  \nADMINISTRACION")
        self.label2=ttk.Entry(fra1)
        boton=ttk.Button(fra1,text=" MOSTRAR",command=self.mostrarP)
        boton2=ttk.Button(fra1,text="  ELIMINAR  ",command=self.fila)
       
        
    



        #para visualisar en la ventana principal
        label1.place(x=20,y=5)
        boton.place(x=20,y=150)
        boton2.place(x=20,y=250)
        self.table = ttk.Treeview(fra2)

# Definir columnas
        self.table['columns'] = ('proveedor', 'medicamentos','unidad', 'ingreso', 'estado','caducidad')

# Formatear columnas
        self.table.column('#0', width=0,stretch=tk.NO)
        self.table.column('proveedor', anchor=tk.CENTER, width=60)
        self.table.column('medicamentos', anchor=tk.W, width=60)
        self.table.column('unidad', anchor=tk.W, width=60)
        self.table.column('ingreso', anchor=tk.CENTER, width=60)
        self.table.column('estado', anchor=tk.CENTER, width=60)
        self.table.column('caducidad', anchor=tk.CENTER, width=65)

# Agregar encabezado
        self.table.heading('#0', text='', anchor=tk.W)
        self.table.heading('proveedor', text='proveedor', anchor=tk.CENTER)
        self.table.heading('medicamentos', text='medicamentos', anchor=tk.W)
        self.table.heading('unidad', text='unidad', anchor=tk.W)
        self.table.heading('ingreso', text='ingreso', anchor=tk.CENTER)
        self.table.heading('estado', text='estado', anchor=tk.W)
        self.table.heading('caducidad', text='caducidad', anchor=tk.CENTER)
 # Ajustar tamaño de la tabla
        
        estilo = ttk.Style(fra2)
        estilo.theme_use('alt') 
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='green',  background='white')
        estilo.map('Treeview',background=[('selected', 'pink2')], foreground=[('selected','blue')] )
        
        
        self.table.bind("<<TreeviewSelect>>",self.obtener_fila)
        self.table.pack(expand=True, fill=tk.BOTH)
       
        fra1.config(width=150,height=500)
        fra2.config(width=350,height=500)
        fra1.place(x=0,y=0)
        fra2.place(x=150,y=0)
    def mostrarP(self):
        self.table.delete(*self.table.get_children())
        registro = self.base_datos.mostrar()
        i = -1
        for dato in registro:
            i= i+1                       
            self.table.insert('',i, text = registro[i][1:1], values=registro[i][0:6])
    
    def fila(self):
        fila = self.table.selection()
        if len(fila)!=0:        
            self.table.delete(fila)
            nombre = ("'"+ str(self.nombre_borrar) + "'")       
            self.base_datos.elimina(nombre)
    def obtener_fila(self,event):
        current_item=self.table.focus()
        if not current_item:
            return
        data=self.table.item(current_item)
        self.nombre_borrar=data['values'][1]
class proveedor(admi):
    def __init__(self, master):
        super(). __init__(master)
        self.wigets()
        self.base_datos=datos()
    def wigets(self):
        super().wigets()
        fra1=Frame()
        fra2=Frame()

        label1=Label(fra1,text="CUENTA\n  DE  \nPROVEEDORES")
        etiqueta=ttk.Label(fra1,text="PROVEEDOR")
        etiqueta2=ttk.Label(fra1,text="NOMBRES DEL MEDICAMENTOS\n                   O           \nDISPOSITIVO MEDICO ")
        etiqueta3=ttk.Label(fra1,text="UNIDADES")
        etiqueta4=ttk.Label(fra1,text="FECHA DE INGRESO")
        etiqueta6=ttk.Label(fra1,text="FECHA DE CADUCIDAD")
        etiqueta5=ttk.Label(fra1,text="ESTADO")
        self.buscador=ttk.Entry()
        self.buscador1=ttk.Entry()
        self.buscador2=ttk.Entry()
        self.buscador3=ttk.Entry()
        self.buscador4=ttk.Entry()
        self.buscador5=ttk.Entry()
        
    
        



        #para visualisar en la ventana principal
        label1.place(x=20,y=5)
        etiqueta.place( x=10,y=60)
        etiqueta2.place(x=10,y=100)
        etiqueta3.place(x=10,y=180)
        etiqueta4.place(x=10,y=240)
        etiqueta5.place(x=10,y=287)
        etiqueta6.place(x=10,y=340)
        self.buscador.place( x=10,y=80)
        self.buscador1.place(x=10,y=155)
        self.buscador2.place(x=10,y=210)
        self.buscador3.place(x=10,y=265)
        self.buscador4.place(x=10,y=310)
        self.buscador5.place(x=10,y=360)
        etiqueta7=ttk.Button(fra1,text="ingresar",command=self.ingresar)
        etiqueta8=ttk.Button(fra1,text="mostrar",command=self.mostrarP)     
        etiqueta7.place(x=10,y=400)
        etiqueta8.place(x=10,y=430)
        self.table = ttk.Treeview(fra2)

# Definir columnas

        self.table['columns'] = ('proveedor', 'medicamentos','unidad', 'ingreso', 'estado','caducidad')

# Formatear columnas
        self.table.column('#0', width=0,stretch=tk.NO)
        self.table.column('proveedor', anchor=tk.CENTER, width=60)
        self.table.column('medicamentos', anchor=tk.W, width=60)
        self.table.column('unidad', anchor=tk.W, width=60)
        self.table.column('ingreso', anchor=tk.CENTER, width=60)
        self.table.column('estado', anchor=tk.CENTER, width=60)
        self.table.column('caducidad', anchor=tk.CENTER, width=65)

# Agregar encabezado
        self.table.heading('#0', text='', anchor=tk.W)
        self.table.heading('proveedor', text='proveedor', anchor=tk.CENTER)
        self.table.heading('medicamentos', text='medicamentos', anchor=tk.W)
        self.table.heading('unidad', text='unidad', anchor=tk.W)
        self.table.heading('ingreso', text='ingreso', anchor=tk.CENTER)
        self.table.heading('estado', text='estado', anchor=tk.W)
        self.table.heading('caducidad', text='caducidad', anchor=tk.CENTER)
 # Ajustar tamaño de la tabla
        self.table.pack(expand=True, fill=tk.BOTH)
        fra1.config(width=200,height=500)
        fra2.config(width=350,height=500,bg="yellow")
        fra1.place(x=0,y=0)
        fra2.place(x=200,y=0)
        
    def ingresar(self):
        self.table.get_children()
        proveedor=self.buscador.get()
        medicamentos=self.buscador1.get()
        unidades=self.buscador2.get()
        ingreso=self.buscador3.get()
        estado=self.buscador4.get()
        caducidad=self.buscador5.get()
        datos=(medicamentos,unidades,ingreso,estado,caducidad)
        if proveedor and medicamentos and unidades and ingreso and estado and caducidad !=' ':
         self.table.insert('',0,text= proveedor,values=datos)
         self.base_datos.inserta(proveedor,medicamentos,unidades,ingreso,estado,caducidad)
        
         	
   
    def mostrarP(self):
        self.table.delete(*self.table.get_children())
        registro = self.base_datos.mostrar()
        i = -1
        for dato in registro:
            i= i+1                       
            self.table.insert('',i, text = registro[i][1:1], values=registro[i][0:6])
    
    

root=tk.Tk()
root.geometry("550x480")
root.wm_resizable(False,False)
root.title("......")
if var=="si":
    van=admi(root)
elif var=="no":
	van=proveedor(root) 
van.mainloop()

