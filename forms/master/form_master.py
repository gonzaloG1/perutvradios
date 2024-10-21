import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from forms.cpm.form_cpm import FormCpm
from forms.datos_generales.form_datos import FormDatos
#import util.generic as utl
from forms.master.form_master_1 import Form_master_1
from forms.word.form_word import FormWord
from forms.word.form_word_design import FormWordDesign


class MasterPanel(Form_master_1):

    def __init__(self):
        super().__init__()
    
    def userDatos(self):
        FormDatos(self.ventana) # llama a formdatos con el panel como padre
        # FormDatos().mainloop()

    def userCpm(self):
        FormCpm(self.ventana)

    def userWord(self):
        FormWord(self.ventana)

    # def userWord(self):
    #     FormWord()
        # FormWord().mainloop()

    
        
