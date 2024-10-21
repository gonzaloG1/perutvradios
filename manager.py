from tkinter import *
from tkinter import messagebox
from bdm import Datos
from forms.login.form_login import FormLogin
from forms.login.form_login_designer import FormLoginDesigner
from forms.master.form_master import MasterPanel
from forms.master.form_master_1 import Form_master_1
from forms.registration.form import FormRegister

class Manager(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # padre_instance = None
        # controlador_instance = None
        # my_obj= FormLogin(padre_instance, controlador_instance)
        # my_obj.__init__()
        self.menu()
        # container=FormLoginDesigner(self)
        # container.pack(side=TOP,fill=BOTH,expand=True)
        # container.configure(bg="green")
        # container=Frame(self)
        # container.pack(side=TOP,fill=BOTH,expand=True)
        # container.configure(bg="green")
        self.frames={}
        # for i in (FormLogin,FormRegister,MasterPanel):
            # frame=i(self)
            # self.frames[i]=frame
            # frame=i(self)
            # self.frames[i]
        # self.show_frame(FormLogin)        
        
        

    def show_frame(self):
        frame=self.frames
        frame.tkraise()

    # def show_frame(self,container):
    #     frame=self.frames[container]
    #     frame.tkraise()

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

    