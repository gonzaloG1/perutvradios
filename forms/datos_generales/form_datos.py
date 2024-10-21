from forms.datos_generales.form_datos_designer import  FormDatosDesign
from tkinter import PhotoImage, filedialog,Label
from tkinter.messagebox import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from tkinter import filedialog
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
import tkinter
import os
from tkinter import messagebox

class FormDatos(FormDatosDesign):


    def __init__(self,master):
        super().__init__(master)
        # Atributos para las rutas de las imágenes
        self.path_imagei = None
        self.path_imagef = None
        self.path_imagec = None

    def cpm():
        pass

    def elegir_imagen(self):

        self.path_imagei=filedialog.askopenfilename(filetypes=[
            ("image",".jpg"),
            ("image",".jpeg"),
            ("image",".png")
        ])
        
        # if len(self.path_imagei)>0:
        if self.path_imagei: 
            
            imagei=cv2.imread(self.path_imagei)
            imagei = imutils.resize(imagei,height=100)

            imageToShow=imutils.resize(imagei,width=100)
            imageToShow=cv2.cvtColor(imageToShow,cv2.COLOR_BGR2RGB)
            im =Image.fromarray(imageToShow)
            imgi=ImageTk.PhotoImage(image=im)
            # self.InputImage = tk.Label( self.frame_form_fill_0, font=(
            # 'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
            # self.InputImage.pack(fill=tk.X,expand=False,side="right")
            self.InputImage.configure(image=imgi)
            self.InputImage.image=imgi 

            print(type(imagei))
            print(type(imgi))

             

    def eliminar_imagen(self):
            self.InputImage.configure(image='')
            self.InputImage.image='' 
        

    def elegir_firma(self):

        self.path_imagef=filedialog.askopenfilename(filetypes=[
            ("image",".jpg"),
            ("image",".jpeg"),
            ("image",".png"),
        ])

        # if len(path_imagef)>0:
        if self.path_imagef:
            

            imagef=cv2.imread(self.path_imagef)
            imagef = imutils.resize(imagef,height=100)

            imageToShow=imutils.resize(imagef,width=100)
            imageToShow=cv2.cvtColor(imageToShow,cv2.COLOR_BGR2RGB)
            im =Image.fromarray(imageToShow)
            imgf=ImageTk.PhotoImage(image=im)

            # self.InputFirma = tk.Label( self.frame_form_fill_12, font=(
            # 'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
            # self.InputFirma.pack(fill=tk.X,expand=False,side="right")

            self.InputFirma.configure(image=imgf)
            self.InputFirma.image=imgf
        
    def eliminar_firma(self):
            self.InputFirma.configure(image='')
            self.InputFirma.image=''

    def elegir_cobertura(self):


        self.path_imagec=filedialog.askopenfilename(filetypes=[
            ("image",".jpg"),
            ("image",".jpeg"),
            ("image",".png")
        ])
        
        # if len(path_imagec)>0:
        if self.path_imagec:
            
            
            imagec=cv2.imread(self.path_imagec)
            imagec = imutils.resize(imagec,height=100)

            imageToShow=imutils.resize(imagec,width=100)
            imageToShow=cv2.cvtColor(imageToShow,cv2.COLOR_BGR2RGB)
            im =Image.fromarray(imageToShow)
            imgc=ImageTk.PhotoImage(image=im)
            # self.InputCobertura = tk.Label( self.frame_form_fill_21, font=(
            # 'Times', 10), fg="#666a88", bg='#fcfcfc', anchor="w")
            # self.InputCobertura.pack(fill=tk.X,expand=False,side="right")
            self.InputCobertura.configure(image=imgc)
            self.InputCobertura.image=imgc  

    def eliminar_cobertura(self):
            self.InputCobertura.configure(image='')
            self.InputCobertura.image=''

    def abrir_archivo(self):
        
        
        i=0
        path_image=filedialog.askopenfilename(filetypes=[
                ("file",".xlsx"),
                ])
        global archivo
        archivo=openpyxl.load_workbook(path_image)
        for i in range(213):
            i=i+1
            cord='F'+str(i)
            cord1='S'+str(i)   
            cord2='C'+str(i)  
            cord3='O'+str(i)
            cord4='N'+str(i) 
            cord5='Q'+str(i)
            cord6='R'+str(i)
            cord7='W'+str(i)
            cord8='T'+str(i)
            cord9='U'+str(i)
            cord10='AB'+str(i)
            cord11='AC'+str(i)
            cord12='L'+str(i)
            #cord13='no se sabe'+str(i)
            #cord14='no se sabe'+str(i)
            cord15='Z'+str(i)
            cord16='Y'+str(i)
            cord17='J'+str(i)
            cord18='M'+str(i)
            sheet=archivo.active
            a1=sheet[cord]
            dom=sheet[cord1]
            ubi=sheet[cord2]
            titu=sheet[cord3]
            ruc=sheet[cord4]
            leg=sheet[cord5]
            dni=sheet[cord6]
            rnp=sheet[cord7]
            tel=sheet[cord8]
            cor=sheet[cord9]
            web=sheet[cord10]
            fb=sheet[cord11]
            tar=sheet[cord12]
            #bon=sheet[cord13]
            #hor=sheet[cord14]
            bnc=sheet[cord15]
            inter=sheet[cord16]
            info=sheet[cord17]
            tare=sheet[cord12]
            tars=sheet[cord18]
            if str(a1.value)==str(self.nombre_comercial.get()):
                #self.nombre_comercial_lol.config(text=a1.value)
                self.domicilio.config(text=dom.value)
                self.ubicacion.config(text=ubi.value)
                self.titular.config(text=titu.value)
                self.ruc.config(text=ruc.value)
                self.legal.config(text=leg.value)
                self.dni.config(text=dni.value)
                self.rnp.config(text=rnp.value)
                self.tel.config(text=tel.value)
                self.correos.config(text=cor.value)
                self.stream.config(text=web.value)
                self.fb.config(text=fb.value)
                self.tarifa.config(text=tar.value)
                #self.boni.config(text=bon.value)
                #self.funci.config(text=hor.value)
                self.banco.config(text=bnc.value)
                self.cod.config(text=inter.value)
                self.info.config(text=info.value)
                self.estado.config(text=tare.value)
                self.social.config(text=tars.value)

    def otra_radio(self):
          
          for i in range(213):
            i=i+1
            cord='F'+str(i)
            cord1='S'+str(i)   
            cord2='C'+str(i)  
            cord3='O'+str(i)
            cord4='N'+str(i) 
            cord5='Q'+str(i)
            cord6='R'+str(i)
            cord7='W'+str(i)
            cord8='T'+str(i)
            cord9='U'+str(i)
            cord10='AB'+str(i)
            cord11='AC'+str(i)
            cord12='L'+str(i)
            #cord13='no se sabe'+str(i)
            #cord14='no se sabe'+str(i)
            cord15='Z'+str(i)
            cord16='Y'+str(i)
            cord17='J'+str(i)
            cord18='M'+str(i)
            sheet=archivo.active
            a1=sheet[cord]
            dom=sheet[cord1]
            ubi=sheet[cord2]
            titu=sheet[cord3]
            ruc=sheet[cord4]
            leg=sheet[cord5]
            dni=sheet[cord6]
            rnp=sheet[cord7]
            tel=sheet[cord8]
            cor=sheet[cord9]
            web=sheet[cord10]
            fb=sheet[cord11]
            tar=sheet[cord12]
            #bon=sheet[cord13]
            #hor=sheet[cord14]
            bnc=sheet[cord15]
            inter=sheet[cord16]
            info=sheet[cord17]
            tare=sheet[cord12]
            tars=sheet[cord18]
            if str(a1.value)==str(self.nombre_comercial.get()):
                #self.nombre_comercial_lol.config(text=a1.value)
                self.domicilio.config(text=dom.value)
                self.ubicacion.config(text=ubi.value)
                self.titular.config(text=titu.value)
                self.ruc.config(text=ruc.value)
                self.legal.config(text=leg.value)
                self.dni.config(text=dni.value)
                self.rnp.config(text=rnp.value)
                self.tel.config(text=tel.value)
                self.correos.config(text=cor.value)
                self.stream.config(text=web.value)
                self.fb.config(text=fb.value)
                self.tarifa.config(text=tar.value)
                #self.boni.config(text=bon.value)
                #self.funci.config(text=hor.value)
                self.banco.config(text=bnc.value)
                self.cod.config(text=inter.value)
                self.info.config(text=info.value)
                self.estado.config(text=tare.value)
                self.social.config(text=tars.value)

            
    # def comprobar(self):
    #     if self.path_imagei is None or self.path_imagef is None or self.path_imagec is None:
    #         messagebox.showinfo("Hubo un problema", "No existe imagen de tu logo")
    #         messagebox.showinfo("Hubo un problema", "No existe imagen de tu firma")
    #         messagebox.showinfo("Hubo un problema", "No existe imagen de tu cobertura oficial")
    #     else:
    #         self.crear_pdf()
             
             

    def crear_pdf(self):
        # if self.path_imagei is None:
        #     messagebox.showinfo("Hubo un problema", "No existe imagen de tu logo")
        # else:
        #     return

        # if self.path_imagef is None:
        #     messagebox.showinfo("Hubo un problema", "No existe imagen de tu firma")
        # else:
        #     return
        
        # if self.path_imagec is None:
        #     messagebox.showinfo("Hubo un problema", "No existe imagen de tu cobertura oficial")
        # else:
        #     return
        #permite elegir la ruta y el nombre del archivo,solo se crea pdf en este caso
        ruta=filedialog.asksaveasfilename(defaultextension=".pdf",
                                          filetypes=[('PDF files', '*.pdf')],
                                          title='Guardar PDF como')
        if not ruta:
             return
        #muestra solo la ruta del guardado no hasta el archivo creado
        guardado = os.path.dirname(ruta)
        # name=self.nombre_comercial.get()
        #permite guardar la ruta según lo definido en ruta y con el nombre obligatorio despues de ruta
        #my_path=f'{ruta} Datos Generales {name}.pdf'
        my_path=f'{ruta}'
        c = canvas.Canvas(my_path,pagesize=letter)   
        c.translate(inch,inch)# define a large font      
        c.setFillColorRGB(0,0,1) # font colour    
        #c.drawImage(imgi,-0.5*inch,8.8*inch,height=80,width=160)   
        #c.drawImage('imagenes/gaaaaa.png',-0.5*inch,8.8*inch,height=80,width=160)  
        #tkinter.Tk().call('font', 'names')
        c.drawImage(self.path_imagei,-0.5*inch,8.8*inch,height=80,width=160)         
        c.setFillColorRGB(0,0,0) # font colour    
        c.setFont("Helvetica-Bold", 12)  
        c.drawString(1.5*inch,8.6*inch,"DATOS GENERALES Y TARIFA DE EMISORA")
        c.drawString(-0.1*inch,8.4*inch,str(self.formato_total))
        c.drawString(-0.1*inch,8.2*inch,"I.INFORMACION GENERAL")
        c.line(0*inch,8.2*inch,2.03*inch,8.2*inch)    
        c.setFont("Helvetica-Bold", 10)  
        c.drawString(0*inch,7.7*inch,"1. Nombre Comercial:")
        c.drawString(2.1*inch,7.7*inch,self.nombre_comercial.get())
        c.drawString(0*inch,7.4*inch,"2. Domicilio:")
        c.drawString(2.1*inch,7.4*inch,self.domicilio.cget('text'))
        c.drawString(0*inch,7.1*inch,"3. Ubicación de emisora:")
        # ubica=self.ubicacion.cget('text')
        # ubicacion=ubica.replace(" ","")
        c.drawString(2.1*inch,7.1*inch,self.ubicacion.cget('text'))
        c.drawString(0*inch,6.8*inch,"4. Titular de la autorización:")
        c.drawString(2.1*inch,6.8*inch,self.titular.cget('text'))
        c.drawString(0*inch,6.5*inch,"5. RUC N°:")
        c.drawString(2.1*inch,6.5*inch,str(self.ruc.cget('text')))
        c.drawString(0*inch,6.2*inch,"6. Representante legal:")
        c.drawString(2.1*inch,6.2*inch,self.legal.cget('text'))
        c.drawString(0*inch,5.9*inch,"7. DNI:")
        c.drawString(2.1*inch,5.9*inch,str(self.dni.cget('text')))
        c.drawString(0*inch,5.6*inch,"8. Código RNP:")
        c.drawString(2.1*inch,5.6*inch,str(self.rnp.cget('text')))
        c.drawString(0*inch,5.3*inch,"9. Teléfonos:")
        c.drawString(2.1*inch,5.3*inch,str(self.tel.cget('text')))
        c.drawString(0*inch,5*inch,"10. Correos:")
        c.drawString(2.1*inch,5*inch,self.correos.cget('text'))
        c.drawString(0*inch,4.7*inch,"11. Web y señal de streamig:")
        c.drawString(2.1*inch,4.7*inch,str(self.stream.cget('text')))
        c.drawString(0*inch,4.4*inch,"12. Señal en facebook:")
        c.drawString(2.1*inch,4.4*inch,str(self.fb.cget('text')))
        c.setFont("Helvetica-Bold", 12) 
        c.drawString(-0.1*inch,3.9*inch,"II.INFORMACIÓN COMERCIAL")
        c.line(0*inch,3.9*inch,2.3*inch,3.9*inch) 
        c.setFont("Helvetica-Bold", 10)  
        c.drawString(0*inch,3.4*inch,"- Tarifa por segundo:")
        c.drawString(2.1*inch,3.4*inch,self.tarifa.cget('text'))
        c.drawString(0*inch,3.1*inch,"- Bonificaciones:")
        c.drawString(2.1*inch,3.1*inch,"25%")
        c.drawString(0*inch,2.8*inch,"- Banco Cuenta:")
        c.drawString(2.1*inch,2.8*inch,self.banco.cget('text'))
        c.drawString(0*inch,2.5*inch,"- Código Cuenta Interbancaria:")
        c.drawString(2.1*inch,2.5*inch,self.cod.cget('text'))
        c.setFont("Helvetica-Bold", 12) 
        c.drawString(-0.1*inch,1.7*inch,"III.INFORMACIÓN ADICIONAL IMPORTANTE")
        c.line(0*inch,1.7*inch,3.45*inch,1.7*inch) 
        c.setFont("Helvetica", 10)  
 
        linea=self.info.cget('text')
        c.drawString(0*inch,1.2*inch,linea[0:90])
        c.drawString(0*inch,0.9*inch,linea[91:189])
        c.drawString(0*inch,0.6*inch,linea[190:])
        c.line(0,-0.7*inch,6.8*inch,-0.7*inch)    
        c.setFillColorRGB(1,0,0) # font colour   
        c.setFont("Helvetica", 8)  
        c.drawString(0, -0.9*inch, u"\u00A9"+" www.perutvradios.com")    
        c.rotate(45) # rotate by 45 degree     
        c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK    

        c.showPage()  
        c.translate(inch,inch)# define a large font  
        c.setFont("Helvetica-Bold", 12) 

        c.setFont("Helvetica-Bold", 12) 
        c.drawString(-0.1*inch,8.2*inch,"IV.COBERTURA OFICIAL")
        c.line(0*inch,8.2*inch,1.85*inch,8.2*inch) 
        c.drawImage(self.path_imagec,0.1*inch,3.5*inch,height=300,width=500)
        c.drawImage(self.path_imagef,2.3*inch,-0.5*inch,height=100,width=160)
            #vertical
            #linea de abajo
        c.line(0,-0.7*inch,6.8*inch,-0.7*inch)    
        c.setFillColorRGB(1,0,0) # font colour   
        c.setFont("Helvetica", 8)  
        c.drawString(0, -0.9*inch, u"\u00A9"+" www.perutvradios.com")    
        c.rotate(45) # rotate by 45 degree     
        c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK  
         # run the template
        c.setFillColorRGB(0,0,0)
        c.showPage()
        c.save()
        # showinfo(title="Todo fue bien",
        #                       message="PDF creado correctamente,se creo en la siguiente ruta: {}".format(my_path))
        self.mostrar_ruta(guardado)
    def mostrar_ruta(self,ruta):
        ventana=tk.Toplevel()
        ventana.title('Ruta del PDF Datos Generales Creado')
        ventana.geometry('400x100')

        ventana.update_idletasks()#actualiza para detectar tareas pendientes el tamaño correcto
        width=ventana.winfo_width()
        height=ventana.winfo_height()
        screen_width=ventana.winfo_screenwidth()
        screen_height=ventana.winfo_screenheight()
        x=(screen_width//2)-(width//2)
        y=(screen_height//2)-(height//2)
        ventana.geometry(f'{width}x{height}+{x}+{y}')

        #cargar y mostrar el logo
        logo_icon=r"D:\2024\Tesis\software\perutvradios\app escritorio python\logo.png"
        logo=PhotoImage(file=logo_icon)
        ventana.iconphoto(False,logo)

        label=tk.Label(ventana, text='PDF Datos Generales creado correctamente en: ')
        label.pack(pady=5)
        #solo Text tiene el atributo insert
        texto=tk.Text(ventana, height=2, width=50)
        texto.insert(tk.END, ruta)
        texto.pack(pady=5)
        texto.config(state=tk.DISABLED) #Hacer que el texto no sea editable
    
    #     self.copiar_ruta(my_path)

    # def copiar_ruta(self,texto):
    #     #copia el texto al portapapeles
    #     # self.root=tk.Tk() 
    #     # self.root.withdraw() #oculta la ventana principal
    #     self.root.clipboard_clear() #limpia el portapapeles
    #     self.root.clipboard_append(texto) #añade el texto al portapapeles
    #     texto=texto+'df'
    #     self.root.update() #asegurate de que el portapapeles se actualiza
    #     # self.root.destroy()  #cierra la ventana    
