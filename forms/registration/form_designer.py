import tkinter as tk
from tkinter import ttk
import util.generic as utl
from tkinter import messagebox
from bdm import Datos
from tkinter import *


class FormRegisterDesigner():

    def register():
        pass

    def __init__(self):
        
        self.ventana = tk.Toplevel()
        self.ventana.title('Registro de usuario')        
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        self.ventana.config(cursor="arrow")
        #self.ventana.iconbitmap("forms/romani.ico")
        utl.centrar_ventana(self.ventana, 600, 450)

        logo = utl.leer_imagen("./imagenes/perutvradios.png", (150, 150))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg='#F87474')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#F87474')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        # frame_form

        # frame_form_top
        frame_form_top = tk.Frame(
            frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=(
            'Times', 30), fg="#666a88", bg='#fcfcfc', pady=30)
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
        
        # etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmar contraseña", font=(
        #     'Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        # etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
        # self.confirmation = ttk.Entry(frame_form_fill, font=('Times', 14))
        # self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        # self.confirmation.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Registrar", font=(
            'Times', 15), bg='#F87474', bd=0, fg="#fff", command=self.register)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.register()))
        
        

        # end frame_form_fill
        self.ventana.mainloop()

    def crearDB(self):
        db=Datos()
        try:
            db.crear()
            messagebox.showinfo(title="Informacion",message="Se creo la base de datos correctamente")
        except:
            messagebox.showinfo(title="Informacion",message="La base de datos ya esta creada")

    def menu(self):
        menubar=Menu()
        menudata=Menu(menubar,tearoff=0)
        menudata.add_command(label="Crear/conectar base de datos",command=self.crearDB)
        menubar.add_cascade(label="Inicio",menu=menudata)
        self.config(menu=menubar)