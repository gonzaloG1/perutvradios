from forms.cpm.form_cpm_design import FormCpmDesign
from tkinter import PhotoImage, filedialog
from tkinter.messagebox import *
# import tkinter as tk
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
# import numpy as np
from tkinter import filedialog
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
import os


class FormCpm(FormCpmDesign):

    def __init__(self,master):
        super().__init__(master)
        # Atributos para las rutas de las imágenes
        self.path_imagei = None
        self.path_imagef = None

    def cpm():
        pass

    def elegir_imagen(self):

        global imagei,path_imagei

        path_imagei=filedialog.askopenfilename(filetypes=[
            ("image",".jpg"),
            ("image",".jpeg"),
            ("image",".png")
        ])
        
        if len(path_imagei)>0:
            
            
            imagei=cv2.imread(path_imagei)
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

            # print(type(imagei))
            # print(type(imgi))

             

    def eliminar_imagen(self):
            self.InputImage.configure(image='')
            self.InputImage.image='' 
        

    def elegir_firma(self):

        global imagef,path_imagef

        path_imagef=filedialog.askopenfilename(filetypes=[
            ("image",".jpg"),
            ("image",".jpeg"),
            ("image",".png"),
        ])

        if len(path_imagef)>0:
            

            imagef=cv2.imread(path_imagef)
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

      

    def eliminar_logo_in(self):
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
            cord='E'+str(i)
            cord1='L'+str(i)   
            cord2='AF'+str(i)  
            cord3='AG'+str(i)
            cord4='N'+str(i) 
            cord5='O'+str(i)
            cord6='Q'+str(i)
            cord7='U'+str(i)
            cord8='T'+str(i)
            cord9='I'+str(i)
            cord10='AH'+str(i)
            cord11='V'+str(i)
            cord12='W'+str(i)
            cord13='X'+str(i)
            cord14='AA'+str(i)
            cord15='Z'+str(i)
            cord16='Y'+str(i)
            cord17='K'+str(i)
            cord18='J'+str(i)
            cord19='AC'+str(i)
            cord20='H'+str(i)
            cord21='AD'+str(i)
            cord22='AE'+str(i)
            cord23='AI'+str(i)
            cord24='AJ'+str(i)
            cord25='AK'+str(i)
            cord26='R'+str(i)
            cord27='AL'+str(i)
            sheet=archivo.active
            a1=sheet[cord]
            mcsdc=sheet[cord1]
            med=sheet[cord2]
            com=sheet[cord3]
            nro=sheet[cord4]
            bon=sheet[cord5]
            pre=sheet[cord6]
            igv=sheet[cord7]
            let=sheet[cord8]
            rep=sheet[cord9]
            car=sheet[cord10]
            amasi=sheet[cord11]
            amano=sheet[cord12]
            dom=sheet[cord13]
            dep=sheet[cord14]
            pro=sheet[cord15]
            dis=sheet[cord16]
            tel=sheet[cord17]
            correo=sheet[cord18]
            reg=sheet[cord19]
            dni=sheet[cord20]
            bbva=sheet[cord21]
            bcn=sheet[cord22]
            cam=sheet[cord23]
            proy=sheet[cord24]
            val=sheet[cord25]
            tot=sheet[cord26]
            otrobbva=sheet[cord27]
            if str(a1.value)==str(self.nombre_comercial.get()):
                #self.nombre_comercial_lol.config(text=a1.value)
                self.mcsdc.config(text=mcsdc.value)
                self.medio.config(text=med.value)
                self.compra.config(text=com.value)
                self.nro.config(text=nro.value)
                self.bonificacion.config(text=bon.value)
                self.preciou.config(text=pre.value)
                self.igv.config(text=igv.value)
                self.letra.config(text=let.value)
                self.representante.config(text=rep.value)
                self.cargo.config(text=car.value)
                if str(amasi.value)=='x':
                    texto='Si({}) No()'.format(amasi.value)
                    self.amazonia.config(text=texto)  
                elif str(amano.value)=='x':
                    texto='Si() No({})'.format(amano.value)
                    self.amazonia.config(text=texto)
                self.domicilio.config(text=dom.value)
                self.departamento.config(text=dep.value)
                self.provincia.config(text=pro.value)
                self.distrito.config(text=dis.value)
                self.telefono.config(text=tel.value)
                self.correo.config(text=correo.value)
                self.registro.config(text=reg.value)
                self.dni.config(text=dni.value)
                self.cuenta.config(text=otrobbva.value)
                self.otracuenta.config(text=(bcn.value+' '+bbva.value))
                self.campana.config(text=cam.value)
                self.proyecto.config(text=proy.value)
                self.validez.config(text=val.value)
                self.contacto.config(text=rep.value)
                self.preciot.config(text=tot.value)
    def otra_radio(self):
         
         for i in range(213):
            i=i+1
            cord='E'+str(i)
            cord1='L'+str(i)   
            cord2='AF'+str(i)  
            cord3='AG'+str(i)
            cord4='N'+str(i) 
            cord5='O'+str(i)
            cord6='Q'+str(i)
            cord7='U'+str(i)
            cord8='T'+str(i)
            cord9='I'+str(i)
            cord10='AH'+str(i)
            cord11='V'+str(i)
            cord12='W'+str(i)
            cord13='X'+str(i)
            cord14='AA'+str(i)
            cord15='Z'+str(i)
            cord16='Y'+str(i)
            cord17='K'+str(i)
            cord18='J'+str(i)
            cord19='AC'+str(i)
            cord20='H'+str(i)
            cord21='AD'+str(i)
            cord22='AE'+str(i)
            cord23='AI'+str(i)
            cord24='AJ'+str(i)
            cord25='AK'+str(i)
            cord26='R'+str(i)
            cord27='AL'+str(i)
            sheet=archivo.active
            a1=sheet[cord]
            mcsdc=sheet[cord1]
            med=sheet[cord2]
            com=sheet[cord3]
            nro=sheet[cord4]
            bon=sheet[cord5]
            pre=sheet[cord6]
            igv=sheet[cord7]
            let=sheet[cord8]
            rep=sheet[cord9]
            car=sheet[cord10]
            amasi=sheet[cord11]
            amano=sheet[cord12]
            dom=sheet[cord13]
            dep=sheet[cord14]
            pro=sheet[cord15]
            dis=sheet[cord16]
            tel=sheet[cord17]
            correo=sheet[cord18]
            reg=sheet[cord19]
            dni=sheet[cord20]
            bbva=sheet[cord21]
            bcn=sheet[cord22]
            cam=sheet[cord23]
            proy=sheet[cord24]
            val=sheet[cord25]
            tot=sheet[cord26]
            otrobbva=sheet[cord27]
            if str(a1.value)==str(self.nombre_comercial.get()):
                #self.nombre_comercial_lol.config(text=a1.value)
                self.mcsdc.config(text=mcsdc.value)
                self.medio.config(text=med.value)
                self.compra.config(text=com.value)
                self.nro.config(text=nro.value)
                self.bonificacion.config(text=bon.value)
                self.preciou.config(text=pre.value)
                self.igv.config(text=igv.value)
                self.letra.config(text=let.value)
                self.representante.config(text=rep.value)
                self.cargo.config(text=car.value)
                if str(amasi.value)=='x':
                    texto='Si({}) No()'.format(amasi.value)
                    self.amazonia.config(text=texto)  
                elif str(amano.value)=='x':
                    texto='Si() No({})'.format(amano.value)
                    self.amazonia.config(text=texto)
                self.domicilio.config(text=dom.value)
                self.departamento.config(text=dep.value)
                self.provincia.config(text=pro.value)
                self.distrito.config(text=dis.value)
                self.telefono.config(text=tel.value)
                self.correo.config(text=correo.value)
                self.registro.config(text=reg.value)
                self.dni.config(text=dni.value)
                self.cuenta.config(text=otrobbva.value)
                self.otracuenta.config(text=(bcn.value+' '+bbva.value))
                self.campana.config(text=cam.value)
                self.proyecto.config(text=proy.value)
                self.validez.config(text=val.value)
                self.contacto.config(text=rep.value)
                self.preciot.config(text=tot.value)                

    def crear_pdf(self):
        ruta=filedialog.asksaveasfilename(defaultextension=".pdf",
                                          filetypes=[('PDF files', '*.pdf')],
                                          title='Guardar PDF como')
        if not ruta:
             return
        guardado = os.path.dirname(ruta)
        my_path=f'{ruta}'
        #para el tipo de texto
        pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
        addMapping('Calibri', 0, 0, 'Calibri')
        # addMapping('Calibri', 0, 1, 'Calibri1')
        styles = getSampleStyleSheet()
        paragraph = styles['Normal']
        # paragraph1=styles['Normal']
        paragraph.fontName='Calibri'
        # paragraph1.fontName='Calibri1'
        # heading.fontName='Calibri-Bold'
        c = canvas.Canvas(my_path,pagesize=letter)   
        c.translate(inch,inch)# define a large font      
        c.setFillColorRGB(0,0,1) # font colour    
        #c.drawImage(imgi,-0.5*inch,8.8*inch,height=80,width=160)   
        #c.drawImage('imagenes/gaaaaa.png',-0.5*inch,8.8*inch,height=80,width=160)  
        c.drawImage(path_imagei,2.5*inch,8.8*inch,height=80,width=160)         
        c.setFillColorRGB(0,0,0) # font colour    
        # c.setFont("Helvetica-Bold", 12)
        c.setFont('Helvetica-Bold', 12)  
        c.drawString(3*inch,8.6*inch,"ANEXO 1")
        c.drawString(1.5*inch,8.4*inch,"FORMULARIO DE PRESENTACIÓN DE COTIZACIÓN")
        c.drawString(2*inch,8.2*inch,"POR PARTE DE LOS PROVEEDORES")
        c.line(0*inch,8*inch,6.5*inch,8*inch)  
        c.setFont(paragraph.fontName, 10)    
        mcosdc=self.mcsdc.cget('text')
        c.drawString(0*inch,7.8*inch,"Los abajo firmantes aceptamos en su totalidad los términos y condiciones del Proyecto, y por la")
        c.drawString(0*inch,7.6*inch,"presente nos ofrecemos a suministrar los avisos/elementos que se enumeran a continuación, de")
        c.drawString(0*inch,7.4*inch,"conformidad con los requisitos del Proyecto con arreglo a la {} 290-2023-PCM-PNUD.".format(mcosdc))
        
        #c.drawString(2*inch,7.5*inch,"TARIFA PUBLICITARIA 2022")
        c.line(-0.5*inch,7.3*inch,7*inch,7.3*inch) 
        c.setFont(paragraph.fontName, 12) 
        c.drawString(-0.3*inch,7.1*inch,"Descripción del")
        c.drawString(-0.3*inch,6.9*inch,"Servicio")
        c.drawString(1.2*inch,7.1*inch,"Medio de")
        c.drawString(1.2*inch,6.9*inch,"prensa")
        c.drawString(2.2*inch,7.1*inch,"Tipo de")
        c.drawString(2.2*inch,6.9*inch,"Compra")
        c.drawString(3.2*inch,7.1*inch,"N° Avisos")
        c.drawString(3.2*inch,6.9*inch,"requeridos")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(4.5*inch,7.1*inch,"Precio unitario")
        precio=self.preciou.cget('text')

        c.drawString(4.5*inch,6.9*inch,"por aviso")
        #c.drawString(4.5*inch,6.7*inch,"(Exonerado")
        igv=self.igv.cget('text')
        # c.drawString(4.5*inch,6.5*inch,"{} S/.".format(igv))
        c.drawString(4.5*inch,6.7*inch,"{} S/.".format(igv))
        # c.setFont("Helvetica-Bold", 10) 
        c.drawString(6*inch,7.1*inch,"Precio Total")
        c.drawString(6*inch,6.9*inch,"{}".format(igv))
        #c.drawString(6*inch,6.7*inch,"del IGV)")
        c.drawString(6*inch,6.5*inch,"S/.")
        c.line(-0.5*inch,6.4*inch,7*inch,6.4*inch)
        c.setFont(paragraph.fontName, 8) 
      
        c.drawString(-0.45*inch,5.5*inch,self.campana.cget('text'))
        c.setFont(paragraph.fontName, 10) 
        c.drawString(1.1*inch,5.5*inch,self.medio.cget('text'))
        c.setFont(paragraph.fontName, 10) 
        c.drawString(2.2*inch,5.5*inch,self.compra.cget('text'))
        c.setFont(paragraph.fontName, 12) 
        canavi=self.nro.cget('text')
        c.drawString(3.4*inch,6*inch,str(canavi))
        c.drawString(3.2*inch,5.8*inch,"PAGADOS")
        boni=self.bonificacion.cget('text')
        c.drawString(3.4*inch,5.6*inch,str(boni))
        c.drawString(3.2*inch,5.4*inch,"BONIFICADOS")
        c.drawString(4.5*inch,5.5*inch,str(precio))
        total=self.preciot.cget('text')
        
        c.drawString(6*inch,5.5*inch,'s/'+str(total))
        c.line(-0.5*inch,4.4*inch,7*inch,4.4*inch)
        c.setFont(paragraph.fontName, 10)
        c.drawString(-0.3*inch,4.1*inch,"MONTO TOTAL OFERTADO{}".format(igv))
        c.drawString(3.4*inch,4.1*inch,str(int(boni)+int(canavi)))
        c.drawString(6*inch,4.1*inch,'s/'+str(total))
        c.line(-0.5*inch,3.9*inch,7*inch,3.9*inch)

        #vertical
        c.line(-0.5*inch,7.3*inch,-0.5*inch,3.9*inch) 
        c.line(1*inch,7.3*inch,1*inch,4.4*inch) 
        c.line(2*inch,7.3*inch,2*inch,4.4*inch) 
        c.line(3*inch,7.3*inch,3*inch,3.9*inch) 
        c.line(4.4*inch,7.3*inch,4.4*inch,3.9*inch) 
        c.line(5.7*inch,7.3*inch,5.7*inch,3.9*inch)
        c.line(7*inch,7.3*inch,7*inch,3.9*inch) 
        
        c.drawString(0*inch,3.6*inch,"Monto total ofertado:")
        monto=self.letra.cget('text')
        c.drawString(2*inch,3.6*inch,"{}/100 soles".format(monto))
        c.line(2*inch,3.55*inch,6.5*inch,3.55*inch)
        c.drawString(0*inch,3*inch,"Validez de la oferta:")
        c.drawString(2*inch,3*inch,self.validez.cget('text'))
        c.line(2*inch,2.95*inch,6.5*inch,2.95*inch)
        c.drawString(0*inch,2.5*inch,"Toda otra información que no hayamos facilitado automáticamente implica nuestra plena aceptación de")
        c.drawString(0*inch,2.3*inch,"los requisitos, términos y condiciones de la Solicitud de Cotización")
        
        c.drawImage(path_imagef,4.8*inch,1.2*inch,width=140,height=80)
        c.drawString(5*inch,0.9*inch,self.representante.cget('text'))
        c.drawString(5*inch,0.7*inch,self.cargo.cget('text'))
        c.drawString(5*inch,0.5*inch,str(self.formato_total_l))
 
        c.showPage()  
        c.translate(inch,inch)# define a large font  
         
        c.drawImage(path_imagei,2.5*inch,8.8*inch,height=80,width=160) 
        c.setFont("Helvetica-Bold", 12)  
        c.drawString(2.8*inch,8.6*inch,"FORMULARIO 1")
        c.drawString(2.5*inch,8.4*inch,"DATOS DEL OFERENTE")
        c.drawString(0*inch,8.2*inch,"REF.: {}-2022-PCM-PNUD".format(mcosdc))

        c.setFont("Helvetica-Bold", 10)  
        c.drawString(0*inch,7.7*inch,"1. Nombre o Razón social:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(2.1*inch,7.7*inch,self.nombre_comercial.get())
        marca=self.amazonia.cget('text')
        c.setFont("Helvetica-Bold", 10) 
        c.drawString(0*inch,7.4*inch,"2. Marque si están exonerados de IGV.(Ley de la Amazonia):{}".format(marca))
        # c.drawString(2.1*inch,7.4*inch,'lala')
        c.drawString(0*inch,7.1*inch,"3. Dirección Principal:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(2.1*inch,7.1*inch,self.domicilio.cget('text'))
        c.setFont("Helvetica-Bold", 10) 
        c.drawString(0*inch,6.8*inch,"4. Departamento:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(1.2*inch,6.8*inch,self.departamento.cget('text'))
        c.setFont("Helvetica-Bold", 10) 
        c.drawString(2.5*inch,6.8*inch,"Provincia:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(3.2*inch,6.8*inch,self.provincia.cget('text'))
        c.setFont("Helvetica-Bold", 10) 
        c.drawString(5*inch,6.8*inch,"Distrito:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(5.7*inch,6.8*inch,self.distrito.cget('text'))
        c.setFont("Helvetica-Bold", 10) 
        c.drawString(0*inch,6.5*inch,"5. Teléfono N°.:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(2.1*inch,6.5*inch,str(self.telefono.cget('text')))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,6.2*inch,"6. Persona a contactar:")
        c.setFont(paragraph.fontName, 10) 
        c.drawString(2.1*inch,6.2*inch,self.representante.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,5.9*inch,"7. Cargo:")
        c.setFont(paragraph.fontName, 10)
        c.drawString(2.1*inch,5.9*inch,self.cargo.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,5.6*inch,"8. E-mail:")
        c.setFont(paragraph.fontName, 10)
        c.drawString(2.1*inch,5.6*inch,self.correo.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,5.3*inch,"9. Teléfono:")
        c.setFont(paragraph.fontName, 10)
        c.drawString(2.1*inch,5.3*inch,str(self.telefono.cget('text')))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,4.7*inch,"10. Datos del Registro Mercantil de la Empresa: (Ejm: Nº Asiento, Foja, Tomo, Ficha, Partida Electrónica, etc")
        c.drawString(0*inch,4.4*inch,"y/o algún otro dato: ")
        c.setFont(paragraph.fontName, 10)
        c.drawString(0*inch,4.1*inch,self.registro.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,3.8*inch,"11. Nombre del representante legal:")
        c.setFont(paragraph.fontName, 10)
        c.drawString(2.5*inch,3.8*inch,self.representante.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,3.5*inch,"12. Documento de identidad:")
        c.setFont(paragraph.fontName, 10)
        c.drawString(2.1*inch,3.5*inch,self.dni.cget('text'))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,3.2*inch,"13. Número de cuenta bancaria en el BBVA Banco Continental en nuevos soles (20 dígitos):")
        c.setFont(paragraph.fontName, 10)
        c.drawString(0*inch,3*inch,str(self.cuenta.cget('text')))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0*inch,2.7*inch,"14. En caso de no contar con cuenta en el BBVA Banco Continental,")
        c.drawString(0*inch,2.5*inch,"favor indicar el nombre de su banco y número de cuenta interbancaria (20 dígitos):")
        c.setFont(paragraph.fontName, 10)
        c.drawString(0*inch,2.3*inch,str(self.otracuenta.cget('text')))

        c.setFont(paragraph.fontName, 10)
        c.drawImage(path_imagef,4.8*inch,1.2*inch,width=140,height=80)
        c.drawString(5*inch,0.9*inch,self.representante.cget('text'))
        c.drawString(5*inch,0.7*inch,self.cargo.cget('text'))
        c.drawString(5*inch,0.5*inch,str(self.formato_total_l))
        c.showPage()
        c.translate(inch,inch)# define a large font  
         
        c.drawImage(path_imagei,2.5*inch,8.8*inch,height=80,width=160) 
        c.setFont("Helvetica-Bold", 12)  
        c.drawString(2.8*inch,8.6*inch,"FORMULARIO 2")
        c.drawString(2.5*inch,8.4*inch,"DECLARACIÓN JURADA")

        c.setFont(paragraph.fontName, 10)
        c.drawString(0*inch,8.3*inch,"Señores")
        c.drawString(0*inch,8.1*inch,"Proyecto {}".format(self.proyecto.cget('text')))
        c.drawString(0*inch,7.9*inch,"Presidencia del Consejo de Ministros")
        c.drawString(0*inch,7.7*inch,"Presente. -")

        c.drawString(0*inch,7.4*inch,"En relación con la Solicitud de Cotización para el Proyecto{}".format(self.proyecto.cget('text')))
        c.drawString(0*inch,7.2*inch,"{}/2023 el oferente que suscribe declara bajo juramento lo que sigue:".format(mcosdc))

        c.drawString(0*inch,6.9*inch,"(a)")
        c.drawString(0.5*inch,6.9*inch,"Que no está impedido de contratar con el Estado Peruano ni con la Presidencia del Consejo de")
        c.drawString(0.5*inch,6.7*inch,"Ministros y que siempre ha cumplido a satisfacción sus compromisos y obligaciones con éste.")
       
        c.drawString(0*inch,6.4*inch,"(b)") 
        c.drawString(0.5*inch,6.4*inch,"Que entre sus directivos y personal no tiene funcionarios o empleados que sean:") 
        c.drawString(0.5*inch,6.2*inch,"-")
        c.drawString(0.6*inch,6.2*inch,"Presidente o vicepresidente, representante del Congreso, Ministro de Estado ni Vocal de la")
        c.drawString(0.6*inch,6*inch,"Corte Suprema de Justicia de la República del Perú.")
        c.drawString(0.5*inch,5.8*inch,"-")
        c.drawString(0.6*inch,5.8*inch,"Personal directivo, funcionario o empleado de la Presidencia del Consejo de Ministros, que")
        c.drawString(0.6*inch,5.6*inch,"haya ejercido funciones hasta seis (6) meses previos al inicio de la presente convocatoria.")
        c.drawString(0.5*inch,5.4*inch,"-")
        c.drawString(0.6*inch,5.4*inch,"Cónyuge, conviviente o pariente hasta el cuarto grado de consanguinidad y segundo de")
        c.drawString(0.6*inch,5.2*inch,"afinidad de las personas anteriormente mencionadas")
        c.drawString(0.5*inch,5*inch,"-")
        c.drawString(0.6*inch,5*inch,"Persona Jurídica en la que las personas ya mencionadas anteriormente tengan una")
        c.drawString(0.6*inch,4.8*inch,"participación superior al 5% del capital social dentro de los 24 meses anteriores a la")
        c.drawString(0.6*inch,4.6*inch,"convocatoria.")
        c.drawString(0.5*inch,4.4*inch,"-")
        c.drawString(0.6*inch,4.4*inch,"Persona natural o jurídica que haya participado como tal en la elaboración de los estudios o")
        c.drawString(0.6*inch,4.2*inch,"información técnica previa que de origen al proceso de selección y sirva de base para el objeto")
        c.drawString(0.6*inch,4*inch,"del contrato.")

        c.drawString(0*inch,3.7*inch,"(c)")
        c.drawString(0.5*inch,3.7*inch,"Que las personas jurídicas que conforman la asociación o consorcio, así como sus directivos,")
        c.drawString(0.5*inch,3.5*inch,"funcionarios, o representantes; no tengan pendientes investigaciones, procesos ante el Ministerio")
        c.drawString(0.5*inch,3.3*inch,"Público o el Poder Judicial, en los cuales esté involucrado el Estado Peruano.")

        c.drawString(0*inch,3*inch,"(d)")
        c.drawString(0.5*inch,3*inch,"Que, por el hecho de presentar una oferta, nos sometemos plenamente a las bases del concurso,")
        c.drawString(0.5*inch,2.8*inch,"las cuales declaramos haber leído, junto con las normas que la rigen.")
        c.drawString(0.5*inch,2.5*inch,str(self.formato_total_m))

        c.setFont(paragraph.fontName, 10)
        c.drawImage(path_imagef,4.8*inch,1.2*inch,width=140,height=80)
        c.drawString(5*inch,0.9*inch,self.representante.cget('text'))
        c.drawString(5*inch,0.7*inch,self.cargo.cget('text'))
        c.drawString(5*inch,0.5*inch,str(self.formato_total_l))
        # c.drawImage(path_imageli,5*inch,-0.5*inch,width=100,height=50)

        # c.line(0,-0.7*inch,6.8*inch,-0.7*inch)    
        # c.setFillColorRGB(1,0,0) # font colour   
        # c.setFont(paragraph.fontName, 8)  
        # c.drawString(0, -0.9*inch, u"\u00A9"+" www.perutvradios.com")    
        # c.rotate(45) # rotate by 45 degree     
        # c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK  
        #  # run the template
        # c.setFillColorRGB(0,0,0)

        c.save()
        self.mostrar_ruta(guardado)

    def mostrar_ruta(self,ruta):
        ventana=tk.Toplevel()
        ventana.title('Ruta del PDF Datos PCM Creado')
        ventana.geometry('400x100')

        #centrar la ventana en la pantalla
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



        label=tk.Label(ventana, text='PDF Datos PCM creado correctamente en: ')
        label.pack(pady=5)
        #solo Text tiene el atributo insert
        texto=tk.Text(ventana, height=2, width=50)
        texto.insert(tk.END, ruta)
        texto.pack(pady=5)
        texto.config(state=tk.DISABLED) #Hacer que el texto no sea editable

        # copiar=tk.Button(ventana,text="Copiar ruta", bg="lightblue", fg="black", command=self.copiar_ruta)
        # copiar.pack(pady=5)
        # copiar.bind("<Return>", (lambda event: self.copiar_ruta()))

    # def copiar_ruta(self,texto):
    #     #copia el texto al portapapeles
    #     # self.root=tk.Tk() 
    #     # self.root.withdraw() #oculta la ventana principal
    #     self.root.clipboard_clear() #limpia el portapapeles
    #     self.root.clipboard_append(texto) #añade el texto al portapapeles
    #     texto=texto+'df'
    #     self.root.update() #asegurate de que el portapapeles se actualiza