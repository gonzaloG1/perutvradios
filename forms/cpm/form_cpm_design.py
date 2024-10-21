import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import locale
from tkinter import PhotoImage


class FormCpmDesign(tk.Toplevel):  
    

    def __init__(self,master):
        super().__init__(master)
        self.title('Generación de PDF de Datos PCM')
        # title_label=tk.Label(self.ventana,text='Generación de PDF de Datos PCM',
        #                     font=('Times',20),bg='blue',fg='white')
        # title_label.pack(side='top', fill=tk.x, pady=10)
        self.geometry('1000x500')
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0)
        self.config(cursor="arrow")

        logo_icon=r"D:\2024\Tesis\software\perutvradios\app escritorio python\logo.png"
        icon = PhotoImage(file=logo_icon)
        self.iconphoto(False, icon)

        #centrar la ventana en la pantalla principal
        self.update_idletasks()
        width=self.winfo_width()
        height=self.winfo_height()
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        x=(screen_width//2)-(width//2)
        y=(screen_height//2)-(height//2)
        self.geometry(f'{width}x{height}+{x}+{y}')

        self.transient(master)
        self.grab_set() #bloquea interacciones con la ventana principal hasta que se cierre la ventana
        self.protocol('WM_DELETE_WINDOW',self.alcerrar)

        self.c = tk.Canvas(self, bg="white")
        self.c.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_form_1 = tk.Frame(self.c,bd=0,
                              relief=tk.SOLID, bg='#fcfcfc')
        
        #barras
        self.v_scrollbar=tk.Scrollbar(self, orient='vertical', command=self.c.yview)
        self.h_scrollbar=tk.Scrollbar(self, orient='horizontal',command=self.c.xview)

        self.c.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        #empaquetar canvas y barra de herramientas
        self.c.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        #empaquetar el frame dentro de canvas
        self.c.create_window((0, 0),window=self.frame_form_1, anchor='nw')
        self.frame_form_1.bind('<Configure>',self.configurar_frame)
        
        #asociar el evento de cerrar con una función
        self.protocol('WM_DELETE_WINDOW',self.alcerrar)

        # self.lblinputImage.pack()
        def my_upper(*args):
            str1.set(str1.get().upper())
        str1=tk.StringVar()
        str1.trace('w',my_upper)
        

        # frame_form_top
        frame_form_top = tk.Frame(
            self.frame_form_1, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=None,expand=False)
        title = tk.Label(frame_form_top, text="Generación de PDF de Datos PCM", font=(
            'Times', 20), fg="#000000", bg='#25ccb8', pady=25)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill_0_1 = tk.Frame(
            self.frame_form_1, height=52,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_0_1.pack(fill=tk.BOTH)
        self.frame_form_fill_0 = tk.Frame(
            self.frame_form_1, height=51,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_0.pack(fill=tk.BOTH)
        frame_form_fill = tk.Frame(
            self.frame_form_1, height=50,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(fill=tk.BOTH)
        frame_form_fill_1 = tk.Frame(
            self.frame_form_1, height=49,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_1.pack(fill=tk.BOTH)
        frame_form_fill_2 = tk.Frame(
            self.frame_form_1, height=48,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_2.pack(fill=tk.BOTH)
        frame_form_fill_3 = tk.Frame(
            self.frame_form_1, height=47,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_3.pack(fill=tk.BOTH)
        frame_form_fill_4 = tk.Frame(
            self.frame_form_1, height=46,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_4.pack(fill=tk.BOTH)
        frame_form_fill_5 = tk.Frame(
            self.frame_form_1, height=45,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_5.pack(fill=tk.BOTH)
        frame_form_fill_6 = tk.Frame(
            self.frame_form_1, height=44,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_6.pack(fill=tk.BOTH)
        frame_form_fill_7 = tk.Frame(
            self.frame_form_1, height=43,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_7.pack(fill=tk.BOTH)
        frame_form_fill_8 = tk.Frame(
            self.frame_form_1, height=42,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_8.pack(fill=tk.BOTH)
        frame_form_fill_9 = tk.Frame(
            self.frame_form_1, height=41,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_9.pack(fill=tk.BOTH)
        frame_form_fill_10 = tk.Frame(
            self.frame_form_1, height=40,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_10.pack(fill=tk.BOTH)
        frame_form_fill_11 = tk.Frame(
            self.frame_form_1, height=39,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_11.pack(fill=tk.BOTH)
        self.frame_form_fill_12 = tk.Frame(
            self.frame_form_1, height=38,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_12.pack(fill=tk.BOTH)
        self.frame_form_fill_13 = tk.Frame(
            self.frame_form_1, height=37,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_13.pack(fill=tk.BOTH)
        self.frame_form_fill_14 = tk.Frame(
            self.frame_form_1, height=36,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_14.pack(fill=tk.BOTH)
        self.frame_form_fill_15 = tk.Frame(
            self.frame_form_1, height=35,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_15.pack(fill=tk.BOTH)
        self.frame_form_fill_16 = tk.Frame(
            self.frame_form_1, height=34,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_16.pack(fill=tk.BOTH)
        self.frame_form_fill_17 = tk.Frame(
            self.frame_form_1, height=33,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_17.pack(fill=tk.BOTH)
        self.frame_form_fill_18 = tk.Frame(
            self.frame_form_1, height=32,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_18.pack(fill=tk.BOTH)
        self.frame_form_fill_19 = tk.Frame(
            self.frame_form_1, height=31,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_19.pack(fill=tk.BOTH)
        self.frame_form_fill_20 = tk.Frame(
            self.frame_form_1, height=30,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_20.pack(fill=tk.BOTH)
        self.frame_form_fill_21 = tk.Frame(
            self.frame_form_1, height=29,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_21.pack(fill=tk.BOTH)
        self.frame_form_fill_22 = tk.Frame(
            self.frame_form_1, height=28,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_22.pack(fill=tk.BOTH)
        self.frame_form_fill_23 = tk.Frame(
            self.frame_form_1, height=27,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_23.pack(fill=tk.BOTH)
        self.frame_form_fill_24 = tk.Frame(
            self.frame_form_1, height=26,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_24.pack(fill=tk.BOTH)
        frame_form_fill_25 = tk.Frame(
            self.frame_form_1, height=25,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_25.pack(fill=tk.BOTH)
        self.frame_form_fill_26 = tk.Frame(
            self.frame_form_1, height=24,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_26.pack(fill=tk.BOTH)
        self.frame_form_fill_27 = tk.Frame(
            self.frame_form_1, height=23,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_27.pack(fill=tk.BOTH)
        self.frame_form_fill_28 = tk.Frame(
            self.frame_form_1, height=22,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_28.pack(fill=tk.BOTH)
        self.frame_form_fill_29 = tk.Frame(
            self.frame_form_1, height=21,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_29.pack(fill=tk.BOTH)
        self.frame_form_fill_30 = tk.Frame(
            self.frame_form_1, height=20,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_30.pack(fill=tk.BOTH)
        self.frame_form_fill_31 = tk.Frame(
            self.frame_form_1, height=19,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_31.pack(fill=tk.BOTH)
        self.frame_form_fill_32 = tk.Frame(
            self.frame_form_1, height=18,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_32.pack(fill=tk.BOTH)
        self.frame_form_fill_33 = tk.Frame(
            self.frame_form_1, height=17,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_33.pack(fill=tk.BOTH)
        self.frame_form_fill_34 = tk.Frame(
            self.frame_form_1, height=16,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_34.pack(fill=tk.BOTH)
        self.frame_form_fill_35 = tk.Frame(
            self.frame_form_1, height=15,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_35.pack(fill=tk.BOTH)
        self.frame_form_fill_36 = tk.Frame(
            self.frame_form_1, height=14,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_36.pack(fill=tk.BOTH)
        self.frame_form_fill_37 = tk.Frame(
            self.frame_form_1, height=13,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_37.pack(fill=tk.BOTH)
        self.frame_form_fill_38 = tk.Frame(
            self.frame_form_1, height=12,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_38.pack(fill=tk.BOTH)
        self.frame_form_fill_39 = tk.Frame(
            self.frame_form_1, height=11,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_39.pack(fill=tk.BOTH)

        self.InputImage = tk.Label( self.frame_form_fill_0, font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.InputImage.pack(fill=tk.X,expand=False,side="right")  

        self.InputFirma = tk.Label( self.frame_form_fill_13, font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.InputFirma.pack(fill=tk.X,expand=False,side="right")

        self.logo1 = tk.Label(self.frame_form_fill_0, text="Logo superior:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.logo1.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.logo_e = tk.Button(self.frame_form_fill_0, font=('Times', 10),width=25,text='Elimina logo superior',command=self.eliminar_imagen)
        self.logo_e.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.logo_e.bind("<Return>", (lambda event: self.eliminar_imagen()))
        self.logo = tk.Button(self.frame_form_fill_0, font=('Times', 10),width=25,text='Selecciona logo superior',command=self.elegir_imagen)
        self.logo.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.logo.bind("<Return>", (lambda event: self.elegir_imagen()))
        self.instruccion = tk.Label(self.frame_form_fill_0, text="Solo escoja un logo y elimine cuando no necesite", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.instruccion.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        

        fecha = tk.Label(frame_form_fill_0_1, text="Fecha de creación:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        fecha.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        #llama a calendario del mismo tkinter
        self.mostrarfecha_hoy_l()
        self.cal=Calendar(frame_form_fill_0_1, text="Fecha:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w",selectmode='day',year=int(self.formato_l[6:10]), month=int(self.formato_l[3:5]), day=int(self.formato_l[0:2]))
        self.cal.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        self.cal.bind("<<CalendarSelected>>", self.mostrarfecha_cal_l)

        nombre_comercial = tk.Label(frame_form_fill, text="Nombre comercial:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        nombre_comercial.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.nombre_comercial = ttk.Entry(frame_form_fill, textvariable=str1,font=('Times', 10))
        self.nombre_comercial.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        # nombre_comercial_lol = tk.Label(frame_form_fill, text="Nombre", font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # nombre_comercial_lol.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        excel = tk.Button(frame_form_fill,width=35, text="Cargar datos desde Hoja de cálculo(Excel) ", font=(
            'Times', 10), bg='#3a7ff6', fg="#fff", command=self.abrir_archivo)
        excel.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        excel.bind("<Return>", (lambda event: self.abrir_archivo()))
        

        mcsdc = tk.Label(frame_form_fill_1, text="MC o SDC:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        mcsdc.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.mcsdc = ttk.Label(frame_form_fill_1, font=('Times', 10))
        self.mcsdc.grid(row=0, column=1, padx=(83,20), pady=10)

        medio = tk.Label(frame_form_fill_2, text="Medio de prensa:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        medio.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.medio = ttk.Label(frame_form_fill_2, font=('Times', 10))
        self.medio.grid(row=0, column=1, padx=(51,20), pady=10)

        compra = tk.Label(frame_form_fill_3, text="Tipo de compra:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        compra.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.compra= ttk.Label(frame_form_fill_3, font=('Times', 10))
        self.compra.grid(row=0, column=1, padx=(58,20), pady=10)

        nro = tk.Label(frame_form_fill_4, text="Nro de avisos pagados:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        nro.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.nro = ttk.Label(frame_form_fill_4, font=('Times', 10))
        self.nro.grid(row=0, column=1, padx=(18,20), pady=10)

        bonificacion = tk.Label(frame_form_fill_5, text="Bonificaciones:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        bonificacion.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.bonificacion = ttk.Label(frame_form_fill_5, font=('Times', 10))
        self.bonificacion.grid(row=0, column=1, padx=(62,20), pady=10)

        preciou = tk.Label(frame_form_fill_6, text="Precio unitario:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        preciou.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.preciou = ttk.Label(frame_form_fill_6, font=('Times', 10))
        self.preciou.grid(row=0, column=1, padx=(64,20), pady=10)

        preciot = tk.Label(frame_form_fill_7, text="Precio Total(s/):", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        preciot.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.preciot = ttk.Label(frame_form_fill_7, font=('Times', 10))
        self.preciot.grid(row=0, column=1, padx=(59,20), pady=10)

        igv = tk.Label(frame_form_fill_8, text="IGV:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        igv.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.igv = ttk.Label(frame_form_fill_8, font=('Times', 10))
        self.igv.grid(row=0, column=1, padx=(121,20), pady=10)

        letra = tk.Label(frame_form_fill_9, text="Precio en letras:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        letra.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.letra = ttk.Label(frame_form_fill_9, font=('Times', 10))
        self.letra.grid(row=0, column=1, padx=(60,20), pady=10)

        representante = tk.Label(frame_form_fill_10, text="Representante:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        representante.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.representante = ttk.Label(frame_form_fill_10, font=('Times', 10))
        self.representante.grid(row=0, column=1, padx=(64,20), pady=10)

        cargo= tk.Label(frame_form_fill_11, text="Cargo:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        cargo.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.cargo = ttk.Label(frame_form_fill_11, font=('Times', 10))
        self.cargo.grid(row=0, column=1, padx=(109,20), pady=10)


        amazonia = tk.Label(self.frame_form_fill_12, text="Ley de la Amazonía:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        amazonia.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.amazonia = ttk.Label(self.frame_form_fill_12, font=('Times', 10))
        self.amazonia.grid(row=0, column=1, padx=(37,20), pady=10)

        firma = tk.Label(self.frame_form_fill_13, text="Firma de representante legal:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        firma.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        des = tk.Label(self.frame_form_fill_13, text="Elija una firma y elimine cuando deje de usar", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        des.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.firma_e = tk.Button(self.frame_form_fill_13, font=('Times', 10),width=30,text='Elimina firma de representante legal',command=self.eliminar_firma)
        self.firma_e.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.firma_e.bind("<Return>", (lambda event: self.elegir_firma()))
        self.firma = tk.Button(self.frame_form_fill_13, font=('Times', 10),width=30,text='Selecciona firma de representante legal',command=self.elegir_firma)
        self.firma.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.firma.bind("<Return>", (lambda event: self.elegir_firma()))

        domicilio = tk.Label(self.frame_form_fill_14, text="Dirección principal:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        domicilio.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.domicilio = ttk.Label(self.frame_form_fill_14,font=('Times', 10))
        self.domicilio.grid(row=0, column=1, padx=(41,20), pady=10)

        departamento = tk.Label(self.frame_form_fill_15, text="Departamento:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        departamento.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.departamento = ttk.Label(self.frame_form_fill_15,font=('Times', 10))
        self.departamento.grid(row=0, column=1, padx=(67,20), pady=10)

        provincia = tk.Label(self.frame_form_fill_16, text="Provincia:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        provincia.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.provincia = ttk.Label(self.frame_form_fill_16,font=('Times', 10))
        self.provincia.grid(row=0, column=1, padx=(92,20), pady=10)

        distrito= tk.Label(self.frame_form_fill_17, text="Distrito:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        distrito.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.distrito = ttk.Label(self.frame_form_fill_17,font=('Times', 10))
        self.distrito.grid(row=0, column=1, padx=(102,20), pady=10)

        telefono = tk.Label(self.frame_form_fill_18, text="Teléfono:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        telefono.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.telefono = ttk.Label(self.frame_form_fill_18,font=('Times', 10))
        self.telefono.grid(row=0, column=1, padx=(95,20), pady=10)

        contacto = tk.Label(self.frame_form_fill_19, text="Persona a contactar:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        contacto.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.contacto  = ttk.Label(self.frame_form_fill_19,font=('Times', 10),anchor='w')
        self.contacto.grid(row=0, column=1, padx=(38,20), pady=10)

        correo = tk.Label(self.frame_form_fill_20, text="Email:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        correo.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.correo = ttk.Label(self.frame_form_fill_20,font=('Times', 10),anchor='w')
        self.correo.grid(row=0, column=1, padx=(115,20), pady=10)

        registro = tk.Label(self.frame_form_fill_21, text="Registro mercantil:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        registro.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.registro = ttk.Label(self.frame_form_fill_21,font=('Times', 10),anchor='w')
        self.registro.grid(row=0, column=1, padx=(47,20), pady=10)

        dni = tk.Label(self.frame_form_fill_22, text="Documento de identidad:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        dni.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.dni = ttk.Label(self.frame_form_fill_22,font=('Times', 10),anchor='w')
        self.dni.grid(row=0, column=1, padx=(12,20), pady=10)

        cuenta = tk.Label(self.frame_form_fill_23, text="Cuenta Bancaria BBVA:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        cuenta.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.cuenta = ttk.Label(self.frame_form_fill_23,font=('Times', 10),anchor='w')
        self.cuenta.grid(row=0, column=1, padx=(19,20), pady=10)

        otracuenta = tk.Label(self.frame_form_fill_24, text="Otra Cuenta Bancaria:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        otracuenta.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.otracuenta= ttk.Label(self.frame_form_fill_24,font=('Times', 10),anchor='w')
        self.otracuenta.grid(row=0, column=1, padx=(30,20), pady=10)

        #llama a calendario del mismo tkinter
        fecha = tk.Label(frame_form_fill_25, text="Fecha de declaración jurada:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        fecha.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        #llama a calendario del mismo tkinter
        self.mostrarfecha_hoy_m()
        self.cal_o=Calendar(frame_form_fill_25, text="Fecha:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w",selectmode='day',year=int(self.formato_l[6:10]), month=int(self.formato_l[3:5]), day=int(self.formato_l[0:2]))
        self.cal_o.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        self.cal_o.bind("<<CalendarSelected>>", self.mostrarfecha_cal_m)

        # dato = tk.Label(self.frame_form_fill_25, text="Fecha en declaración jurada", font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # dato.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        # self.dato = ttk.Entry(self.frame_form_fill_25,font=('Times', 10))
        # self.dato.grid(row=0, column=1, padx=(0,20), pady=10)

        campana= tk.Label(self.frame_form_fill_26, text="Campaña:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        campana.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.campana= ttk.Label(self.frame_form_fill_26,font=('Times', 10),anchor='w')
        self.campana.grid(row=0, column=1, padx=(95,20), pady=10)

        validez= tk.Label(self.frame_form_fill_27, text="Validez del proyecto:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        validez.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.validez= ttk.Label(self.frame_form_fill_27,font=('Times', 10),anchor='w')
        self.validez.grid(row=0, column=1, padx=(37,20), pady=10)

        proyecto= tk.Label(self.frame_form_fill_28, text="Proyecto:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        proyecto.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.proyecto= ttk.Label(self.frame_form_fill_28,font=('Times', 10),anchor='w')
        self.proyecto.grid(row=0, column=1, padx=(97,20), pady=10)
        
        self.mandar_pdf = tk.Button(self.frame_form_fill_30, font=('Times', 8),height=1,width=15,text='Crear en PDF',command=self.crear_pdf,bg='blue',fg='white')
        # self.mandar_pdf.pack(fill=tk.X,side='bottom',expand=False, padx=20, pady=5,ipadx=5,ipady=2)
        # self.mandar_pdf.grid(row=0,column=0,padx=20,pady=5,sticky='ew')
        # self.frame_form_fill_21.grid_columnconfigure(0, weight=1)  # Columna izquierda
        # self.frame_form_fill_21.grid_columnconfigure(1, weight=0)  # Columna del botón
        # self.frame_form_fill_21.grid_columnconfigure(2, weight=1)
        # # self.frame_form_fill_21.grid_columnconfigure(1,weight=1)
        # self.mandar_pdf.bind("<Return>", (lambda event: self.crear_pdf()))

        # Crear un frame para centrar el botón
        self.frame_button = tk.Frame(self.frame_form_fill_30)
        self.frame_button.grid(row=0, column=0)

        # Crear un botón
        self.mandar_pdf = tk.Button(
            self.frame_button,
            font=('Times', 8),
            text='Crear en PDF',
            command=self.crear_pdf,
            bg='#3a7ff6', 
            fg="#fff",
            width=15,  # Establecer el ancho
            height=1   # Establecer la altura
        )

        # Colocar el botón en el frame
        self.mandar_pdf.pack(padx=20, pady=5)

        # Configurar el frame principal para centrar el botón
        self.frame_form_fill_30.grid_columnconfigure(0, weight=1)

        space = tk.Label(self.frame_form_fill_34, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space1 = tk.Label(self.frame_form_fill_35, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space1.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space2 = tk.Label(self.frame_form_fill_36, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space2.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        # space3 = tk.Label(self.frame_form_fill_37, text="", font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # space3.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        
        # end frame_form_fill
        self.mostrarfecha_cal_l()
        self.mostrarfecha_cal_m()
        self.mainloop()
    
    def configurar_frame(self,event):
        self.c.configure(scrollregion=self.c.bbox('all'))

    def mostrarfecha_hoy_l(self):
        #captura la fecha del sistema
        fecha_seleccionada_h=datetime.now()
        self.formato_l=fecha_seleccionada_h.strftime('%d/%m/%Y')
        # self.fecha_a.config(text=formato)

    def mostrarfecha_hoy_m(self):
        #cambiar el mes a español
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

        #captura la fecha del sistema
        fecha_seleccionada_h=datetime.now()
        self.formato_m=fecha_seleccionada_h.strftime("%d de %B del %Y")

    def mostrarfecha_cal_l(self,event=None):
        fecha_seleccionada = self.cal.get_date()
        #convierte la cadena a un objeto datetime para llamar ala funcion strftime
        fecha_objeto=datetime.strptime(fecha_seleccionada, "%m/%d/%y")
        # #cambia el formato a dia/mes/año
        self.formato_total_l=fecha_objeto.strftime("%d/%m/%Y")

    def mostrarfecha_cal_m(self,event=None):
        # captura la fecha del label
        fecha_seleccionada = self.cal_o.get_date()
        # convierte la cadena a un objeto datetime
        fecha_objeto = datetime.strptime(fecha_seleccionada, "%m/%d/%y")
        # cambia el formato a "19 de Septiembre del 2024"
        self.formato_total_m = fecha_objeto.strftime("%d de %B del %Y")

    def alcerrar(self):
        #askokcancel mensaje al cerrar a la ventana
        if messagebox.askokcancel('Salir','¿Deseas cerrar la ventana?'):
            self.destroy()

    