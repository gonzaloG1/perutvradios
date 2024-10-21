import tkinter as tk
# import util.generic as utl
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from tkinter import PhotoImage

class FormDatosDesign(tk.Toplevel):
    
    

    def __init__(self,master):
        super().__init__(master)
        self.title('Generación de PDF de Datos Generales y Tarifa de Emisora')
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
        # self.frame_form_1.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        self.frame_form_1.bind('<Configure>',self.configurar_frame)

        #asociar el evento de cerrar con una función
        self.protocol('WM_DELETE_WINDOW',self.alcerrar)

        def my_upper(*args):
            str1.set(str1.get().upper())
        str1=tk.StringVar()
        str1.trace('w',my_upper)
        

        # frame_form_top
        frame_form_top = tk.Frame(
            self.frame_form_1, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=None,expand=False)
        title = tk.Label(frame_form_top, text="Generación de PDF de Datos Generales y Tarifa de Emisora", font=(
            'Times', 20), fg="#000000", bg='#25ccb8', pady=25)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        # end frame_form_top

        # frame_form_fill
        frame_form_fill_0_1 = tk.Frame(
            self.frame_form_1, height=52,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_0_1.pack(fill=tk.BOTH)
        frame_form_fill_0 = tk.Frame(
            self.frame_form_1, height=51,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill_0.pack(fill=tk.BOTH)
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
        self.frame_form_fill_25 = tk.Frame(
            self.frame_form_1, height=25,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_25.pack(fill=tk.BOTH)
        self.frame_form_fill_26 = tk.Frame(
            self.frame_form_1, height=24,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_26.pack(fill=tk.BOTH)
        self.frame_form_fill_27 = tk.Frame(
            self.frame_form_1, height=23,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_27.pack(fill=tk.BOTH)
        self.frame_form_fill_28 = tk.Frame(
            self.frame_form_1, height=22,  bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form_fill_28.pack(fill=tk.BOTH)
        
        self.InputImage = tk.Label(frame_form_fill_0, font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.InputImage.pack(fill=tk.X,expand=False,side="right")  

        self.InputFirma = tk.Label( self.frame_form_fill_12, font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.InputFirma.pack(fill=tk.X,expand=False,side="right")

        self.InputCobertura = tk.Label( self.frame_form_fill_20, font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.InputCobertura.pack(fill=tk.X,expand=False,side="right")

        fecha = tk.Label(frame_form_fill_0_1, text="Fecha de creación:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        fecha.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        #llama a calendario del mismo tkinter
        self.mostrarfecha()
        self.cal=Calendar(frame_form_fill_0_1, text="Fecha:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w",selectmode='day',year=int(self.formato[6:10]), month=int(self.formato[3:5]), day=int(self.formato[0:2]))
        self.cal.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        self.cal.bind("<<CalendarSelected>>", self.mostrarfecha_cal)
        # self.fecha_s=tk.Label(frame_form_fill_0_1,text='Fecha seleccionada: ',font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # self.fecha_s.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        # self.fecha_a=ttk.Label(frame_form_fill_0_1,font=('Times', 10))
        # self.fecha_a.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        # self.botonf = tk.Button(frame_form_fill_0_1, font=('Times', 10),width=25,text='Mostrar fecha',command=self.mostrarfecha_cal)
        # self.botonf.pack(fill=None,expand=True,side='left', padx=20, pady=5)
        # self.botonf.bind("<Return>", (lambda event: self.mostrarfecha_cal()))

        self.logo1 = tk.Label(frame_form_fill_0, text="Logo:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.logo1.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.logo_e = tk.Button(frame_form_fill_0, font=('Times', 10),width=25,text='Elimina logo',command=self.eliminar_imagen)
        self.logo_e.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.logo_e.bind("<Return>", (lambda event: self.eliminar_imagen()))
        self.logo = tk.Button(frame_form_fill_0, font=('Times', 10),width=25,text='Selecciona logo',command=self.elegir_imagen)
        self.logo.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.logo.bind("<Return>", (lambda event: self.elegir_imagen()))
        self.instruccion = tk.Label(frame_form_fill_0, text="Solo escoja un logo y elimine cuando no necesite", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.instruccion.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        nombre_comercial = tk.Label(frame_form_fill, text="Nombre comercial:", font=(
          'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        nombre_comercial.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.nombre_comercial = ttk.Entry(frame_form_fill, textvariable=str1,font=('Times', 10))
        self.nombre_comercial.pack(fill=None,expand=True,side='left', padx=20, pady=5)

        excel = tk.Button(frame_form_fill,width=35, text="Cargar datos desde Hoja de cálculo(Excel) ", font=(
            'Times', 10), bg='#3a7ff6', fg="#fff", command=self.abrir_archivo)
        excel.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        excel.bind("<Return>", (lambda event: self.abrir_archivo()))
        

        domicilio = tk.Label(frame_form_fill_1, text="Domicilio:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        domicilio.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.domicilio = ttk.Label(frame_form_fill_1, font=('Times', 10))
        self.domicilio.grid(row=0, column=1, padx=(113,20), pady=10)

        ubicacion = tk.Label(frame_form_fill_2, text="Ubicación de emisora:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        ubicacion.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.ubicacion = ttk.Label(frame_form_fill_2, font=('Times', 10))
        self.ubicacion.grid(row=0, column=1, padx=(47,20), pady=10)

        titular = tk.Label(frame_form_fill_3, text="Titular de la autorización:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        titular.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.titular = ttk.Label(frame_form_fill_3, font=('Times', 10))
        self.titular.grid(row=0, column=1, padx=(28,20), pady=10)

        ruc = tk.Label(frame_form_fill_4, text="RUC N°:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        #utilizar grid para usar cuadro y alinear mejor los datos
        ruc.grid(row=0, column=0, padx=20, pady=10, sticky='W')
        # ruc.pack(side='left', padx=20, pady=10)
        #padx (65,20) 20 es el eje de x es la misma columna y 65 es el punto en el eje x
        self.ruc = ttk.Label(frame_form_fill_4, font=('Times', 10))
        self.ruc.grid(row=0, column=1, padx=(118,20), pady=10)

        legal = tk.Label(frame_form_fill_5, text="Representante legal:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        legal.grid(row=0, column=0, padx=20, pady=10, sticky='W')
        self.legal = ttk.Label(frame_form_fill_5, font=('Times', 10))
        self.legal.grid(row=0, column=1, padx=(55,20), pady=10)

        dni = tk.Label(frame_form_fill_6, text="DNI:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        dni.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.dni = ttk.Label(frame_form_fill_6, font=('Times', 10))
        self.dni.grid(row=0, column=1, padx=(138,20), pady=10)

        rnp = tk.Label(frame_form_fill_7, text="Código RNP:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        rnp.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.rnp = ttk.Label(frame_form_fill_7, font=('Times', 10))
        self.rnp.grid(row=0, column=1, padx=(93,20), pady=10)

        tel = tk.Label(frame_form_fill_8, text="Teléfonos:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        tel.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.tel = ttk.Label(frame_form_fill_8, font=('Times', 10))
        self.tel.grid(row=0, column=1, padx=(105,20), pady=10)

        correos = tk.Label(frame_form_fill_9, text="Correos:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        correos.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.correos = ttk.Label(frame_form_fill_9, font=('Times', 10))
        self.correos.grid(row=0, column=1, padx=(117,20), pady=10)

        stream = tk.Label(frame_form_fill_10, text="Web y señal de streaming:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        stream.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.stream = ttk.Label(frame_form_fill_10, font=('Times', 10))
        self.stream.grid(row=0, column=1, padx=(20,20), pady=10)


        fb = tk.Label(frame_form_fill_11, text="Señal en facebook:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        fb.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.fb = ttk.Label(frame_form_fill_11, font=('Times', 10))
        self.fb.grid(row=0, column=1, padx=(60,20), pady=10)

        firma = tk.Label(self.frame_form_fill_12, text="Firma de representante legal:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        firma.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        des = tk.Label(self.frame_form_fill_12, text="Elija una firma y elimine cuando deje de usar", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        des.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.firma_e = tk.Button(self.frame_form_fill_12, font=('Times', 10),width=30,text='Elimina firma de representante legal',command=self.eliminar_firma)
        self.firma_e.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.firma_e.bind("<Return>", (lambda event: self.elegir_firma()))
        self.firma = tk.Button(self.frame_form_fill_12, font=('Times', 10),width=30,text='Selecciona firma de representante legal',command=self.elegir_firma)
        self.firma.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.firma.bind("<Return>", (lambda event: self.elegir_firma()))

        tarifa = tk.Label(self.frame_form_fill_13, text="Tarifa por segundo:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        tarifa.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.tarifa = ttk.Label(self.frame_form_fill_13,font=('Times', 10))
        self.tarifa.grid(row=0, column=1, padx=(55,20), pady=10)

        boni = tk.Label(self.frame_form_fill_14, text="Bonificaciones:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        boni.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.boni = ttk.Label(self.frame_form_fill_14,text="25%",font=('Times', 10))
        self.boni.grid(row=0, column=1, padx=(75,20), pady=10)

        banco = tk.Label(self.frame_form_fill_15, text="Banco Cuenta:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        banco.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.banco = ttk.Label(self.frame_form_fill_15,font=('Times', 10))
        self.banco.grid(row=0, column=1, padx=(80,20), pady=10)

        cod = tk.Label(self.frame_form_fill_16, text="Código Cuenta Interbancaria:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        cod.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.cod = ttk.Label(self.frame_form_fill_16,font=('Times', 10))
        self.cod.grid(row=0, column=1, padx=(0,20), pady=10)

        info = tk.Label(self.frame_form_fill_17, text="Información:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        info.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.info = ttk.Label(self.frame_form_fill_17,font=('Times', 10),anchor='w')
        self.info.grid(row=0, column=1, padx=(90,20), pady=10)

        estado = tk.Label(self.frame_form_fill_18, text="Tarifa del estado:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        estado.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.estado = ttk.Label(self.frame_form_fill_18,font=('Times', 10),anchor='w')
        self.estado.grid(row=0, column=1, padx=(65,20), pady=10)

        social = tk.Label(self.frame_form_fill_19, text="Tarifa social:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        social.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        self.social = ttk.Label(self.frame_form_fill_19,font=('Times', 10),anchor='w')
        self.social.grid(row=0, column=1, padx=(90,20), pady=10)
        
        oficial = tk.Label(self.frame_form_fill_20, text="Cobertura oficial:", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        oficial.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        des = tk.Label(self.frame_form_fill_20, text="Elija 1 cobertura y elimina al usar", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        des.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)
        self.oficial_e = tk.Button(self.frame_form_fill_20, font=('Times', 8),width=25,text='Elimina cobertura oficial',command=self.eliminar_cobertura)
        self.oficial_e.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.oficial_e.bind("<Return>", (lambda event: self.eliminar_cobertura()))
        self.oficial = tk.Button(self.frame_form_fill_20, font=('Times', 8),width=25,text='Selecciona cobertura oficial',command=self.elegir_cobertura)
        self.oficial.pack(fill=None,side='right',expand=True, padx=20, pady=5)
        self.oficial.bind("<Return>", (lambda event: self.elegir_cobertura()))
        
        # rutap = tk.Label(self.frame_form_fill_21, text="Ruta del archivo:", font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # rutap.grid(row=0, column=0, padx=20, pady=10,sticky='W')
        # self.rutap = ttk.Entry(self.frame_form_fill_21,font=('Times', 10))
        # self.rutap.grid(row=0, column=1, padx=(65,20), pady=10)

        self.mandar_pdf = tk.Button(self.frame_form_fill_21, font=('Times', 8),height=1,width=15,text='Crear en PDF',command=self.crear_pdf,bg='blue',fg='white')
        # self.mandar_pdf.pack(fill=tk.X,side='bottom',expand=False, padx=20, pady=5,ipadx=5,ipady=2)
        # self.mandar_pdf.grid(row=0,column=0,padx=20,pady=5,sticky='ew')
        # self.frame_form_fill_21.grid_columnconfigure(0, weight=1)  # Columna izquierda
        # self.frame_form_fill_21.grid_columnconfigure(1, weight=0)  # Columna del botón
        # self.frame_form_fill_21.grid_columnconfigure(2, weight=1)
        # # self.frame_form_fill_21.grid_columnconfigure(1,weight=1)
        # self.mandar_pdf.bind("<Return>", (lambda event: self.crear_pdf()))

        # Crear un frame para centrar el botón
        self.frame_button = tk.Frame(self.frame_form_fill_21)
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
        self.frame_form_fill_21.grid_columnconfigure(0, weight=1)

        space = tk.Label(self.frame_form_fill_23, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space1 = tk.Label(self.frame_form_fill_24, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space1.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space2 = tk.Label(self.frame_form_fill_25, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space2.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space3 = tk.Label(self.frame_form_fill_26, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space3.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        space4 = tk.Label(self.frame_form_fill_27, text="", font=(
            'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        space4.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        # space5 = tk.Label(self.frame_form_fill_28, text="", font=(
        #     'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
        # space5.pack(fill=tk.X,side='left',expand=False, padx=20, pady=5)

        #5353ec
        #scrollbar vertical
        
        # end frame_form_fill
        # print(self.mostrarfecha)
        self.mostrarfecha_cal()
        self.mainloop()

    def configurar_frame(self,event):
        self.c.configure(scrollregion=self.c.bbox('all'))

    def mostrarfecha(self):
        #captura la fecha del sistema
        fecha_seleccionada_h=datetime.now()
        self.formato=fecha_seleccionada_h.strftime('%d/%m/%Y')
        # self.fecha_a.config(text=formato)

    def mostrarfecha_cal(self,event=None):
        fecha_seleccionada = self.cal.get_date()
        #convierte la cadena a un objeto datetime para llamar ala funcion strftime
        fecha_objeto=datetime.strptime(fecha_seleccionada, "%m/%d/%y")
        # #cambia el formato a dia/mes/año
        self.formato_total=fecha_objeto.strftime("%d/%m/%Y")
        # self.fecha_a.config(text=f'{formato}')

    def alcerrar(self):
        #askokcancel mensaje al cerrar a la ventana
        if messagebox.askokcancel('Salir','¿Deseas cerrar la ventana?'):
            self.destroy()
    # def fecha(self):
    #     if 


    