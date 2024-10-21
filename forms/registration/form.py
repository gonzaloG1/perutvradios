from bdm import Datos
from forms.login.form_login_designer import FormLoginDesigner
from forms.master.form_master_1 import Form_master_1
from forms.registration.form_designer import FormRegisterDesigner
# from persistence.repository.auth_user_repository import AuthUserRepositroy
# from persistence.model import Auth_User
from tkinter import messagebox
# import util.encoding_decoding as end_dec
from bdm import Datos
from tkinter import *

class FormRegister(FormRegisterDesigner):

    def __init__(self,padre,controlador):
        super().__init__(padre,controlador)
        # self.padre=padre
        self.controlador=controlador

    def eje_consulta(self,consulta,parametros=()):
        db=Datos()
        db.consultar(consulta,parametros)

    def registro(self):
        user=self.etiqueta_usuario.get()
        pas=self.etiqueta_password.get()
        if len(pas)<6:
            messagebox.showinfo(title="Error",message="Contraseña demasiado corta debe ser mayor a 5")
            self.etiqueta_usuario.delete(0,END)
            self.etiqueta_password.delete(0,END)
        else:
            consulta="INSERT INTO usuarios VALUES(?,?,?)"
            parametros=(None,user,pas)
            self.eje_consulta(consulta,parametros)
            self.control1()

    def control1(self):
        self.controlador.show_frame(Form_master_1)

    
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

    # def register(self):
    #     if(self.isConfirmationPassword()):                    
    #         user = Auth_User()
    #         user.username = self.usuario.get()
    #         user_db: Auth_User = self.auth_repository.getUserByUserName(
    #             self.usuario.get())

    #         if not (self.isUserRegister(user_db)):
    #             user.password = end_dec.encrypted(self.password.get())
    #             self.auth_repository.insertUser(user)
    #             messagebox.showinfo(
    #                 message="Se registro el usuario", title="Mensaje")     
    #             self.ventana.destroy()     
                  

    # def isUserRegister(self, user: Auth_User):
    #     status: bool = False
    #     if(user != None):
    #         status = True
    #         messagebox.showerror(
    #             message="El usuario ya existe", title="Mensaje")
    #     return status
    
    # def isConfirmationPassword(self):
    #     status: bool = True
    #     if(self.password.get() != self.confirmation.get()):
    #         status = False
    #         messagebox.showerror(
    #             message="La contraseña no coinciden por favor verifica el registro", title="Mensaje")
    #         self.password.delete(0, tk.END)                
    #         self.confirmation.delete(0, tk.END) 
    #     return status