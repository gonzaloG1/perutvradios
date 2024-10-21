from tkinter import messagebox
from tkinter import *
from bdm import Datos
from forms.login.form_login_designer import FormLoginDesigner
# from forms.master.form_master import MasterPanel
from forms.master.form_master_1 import Form_master_1
# from persistence.repository.auth_user_repository import AuthUserRepositroy
# import util.encoding_decoding as end_dec
# from persistence.model import Auth_User
from tkinter import messagebox
# from build_db import Datos
import sqlite3
from tkinter import *
from forms.registration.form_designer import FormRegisterDesigner


class FormLogin(FormLoginDesigner):
    def __init__(self,padre,controlador):
        super().__init__()
        # self.frames={}
        # self.padre=padre
        self.controlador=controlador
        
    # def show_frame(self,container):
    #     frame=self.frames[container]
    #     frame.tkraise()    

    def control1(self):
        self.controlador.show_frame(Form_master_1)

    def control2(self):
        self.controlador.show_frame(FormRegisterDesigner)
    def login(self):
        with sqlite3.connect("database.db") as conn:
            cursor=conn.cursor()
            user=self.etiqueta_usuario.get()
            pas=self.etiqueta_password.get()
            consulta="SELECT*FROM usuarios WHERE name=? AND password=?"
            parametros=(user,pas)
            cursor.execute(consulta,parametros)
            #si existe en cursor
            if cursor.fetchall():
                self.control1
            else:
                self.etiqueta_usuario.delete(0,END)
                self.etiqueta_password.delete(0,END)
                messagebox.showerror(title="Error",message="Usuario y/o contraseña incorrecta")
            cursor.close()

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
    # def __init__(self):
    #     self.auth_repository = AuthUserRepositroy()
    #     super().__init__()

    # def verificar(self):
    #     user_db: Auth_User = self.auth_repository.getUserByUserName(
    #         self.usuario.get())
    #     if(self.isUser(user_db)):
    #         self.isPassword(self.password.get(), user_db)

    # def userRegister(self):
    #     FormRegister().mainloop()


    # def isUser(self, user: Auth_User):
    #     status: bool = True
    #     if(user == None):
    #         status = False
    #         messagebox.showerror(
    #             message="El usuario no existe por favor registrese", title="Mensaje")
    #     return status

    # def isPassword(self, password: str, user: Auth_User):
    #     b_password = end_dec.decrypt(user.password)
    #     if(password == b_password):
    #         self.ventana.destroy()
    #         MasterPanel()
    #     else:
    #         messagebox.showerror(
    #             message="La contraseña no es correcta", title="Mensaje")
            
    # 