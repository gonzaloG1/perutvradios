import tkinter as tk
from tkinter import *
from tkinter import ttk
import util.generic as utl
# from tkinter import messagebox
# from bdm import Datos

class FormLoginDesigner(Tk):
        
    def verificar(self):
        pass
    
    def userRegister(self):
        pass
    
    
    def __init__(self):
        # super().__init__(*args,**kwargs)
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        #self.ventana.iconbitmap("romani.ico")
        self.ventana.resizable(width=0, height=0)
        self.ventana.config(cursor="arrow")
        utl.centrar_ventana(self.ventana, 800, 500)

    
    #     #probar conexion
    # def crearDB(self):
    #     db=Datos()
    #     try:
    #         db.crear()
    #         messagebox.showinfo(title="Informacion",message="Se creo la base de datos correctamente")
    #     except:
    #         messagebox.showinfo(title="Informacion",message="La base de datos ya esta creada")
        # self.config(menu=menubar)

        logo = utl.leer_imagen("./imagenes/perutvradios.png", (200, 200))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300,
                              relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        # label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label = tk.Label(frame_logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill = tk.Frame(
            frame_form, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.login)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.login()))
        
        
        inicio = tk.Button(frame_form_fill, text="Registrar usuario", font=(
            'Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6", command=self.control2)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.control2()))
        
        # end frame_form_fill
        self.ventana.mainloop()
    
    # def crearDB(self):
    #     db=Datos()
    #     try:
    #         db.crear()
    #         messagebox.showinfo(title="Informacion",message="Se creo la base de datos correctamente")
    #     except:
    #         messagebox.showinfo(title="Informacion",message="La base de datos ya esta creada")

    # def menu(self):
    #     menubar=Menu()
    #     menudata=Menu(menubar,tearoff=0)
    #     menudata.add_command(label="Crear/conectar base de datos",command=self.crearDB)
    #     menubar.add_cascade(label="Inicio",menu=menudata)
    #     self.config(menu=menubar)
    # def crearDB(self):
    #     db=Datos()
    #     try:
    #         db.crear()
    #         messagebox.showinfo(title="Informacion",message="Se creo la base de datos correctamente")
    #     except:
    #         messagebox.showinfo(title="Informacion",message="La base de datos ya esta creada")

    # def menu(self):
    #     menubar=Menu()
    #     menudata=Menu(menubar,tearoff=0)
    #     menudata.add_command(label="Crear/conectar base de datos",command=self.crearDB)
    #     menubar.add_cascade(label="Inicio",menu=menudata)
    #     self.config(menu=menubar)