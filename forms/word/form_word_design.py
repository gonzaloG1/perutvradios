import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from docx import Document
from docx.shared import Inches
import os
from tkinter import PhotoImage


class FormWordDesign(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title('Inserción de logo y firma en documentos Word de PCM')
        self.geometry('1000x600')
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0)

        logo_icon = r"D:\2024\Tesis\software\perutvradios\app escritorio python\logo.png"
        icon = PhotoImage(file=logo_icon)
        self.iconphoto(False, icon)

        # Centrar la ventana en la pantalla principal
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

        #ventana vinculada a ventana principal
        self.transient(master)
        self.grab_set() #bloquea interacciones con la ventana principal hasta que se cierre la ventana
        self.protocol('WM_DELETE_WINDOW',self.alcerrar)

        # Frame principal
        self.frame_form_1 = tk.Frame(self, bg='#fcfcfc')
        self.frame_form_1.pack(expand=True)

        self.protocol('WM_DELETE_WINDOW',self.alcerrar)

        # Título centrado
        title = tk.Label(self.frame_form_1, text="Inserción de logo y firma en documentos Word de PCM",
                         font=('Times', 20), fg="#000000", bg='#25ccb8', pady=20)
        title.pack(pady=(10, 20))

        # Listbox centrado
        self.listbox = tk.Listbox(self.frame_form_1, height=15, width=80, font=('Times', 10),
                                  fg="#666a88", bg='#fcfcfc', selectbackground='#a3c4f7')
        self.listbox.pack(pady=(0, 20))

        # Frame para los botones centrados
        button_frame = tk.Frame(self.frame_form_1, bg='#fcfcfc')
        button_frame.pack(pady=10)

        # Botón para seleccionar archivos Word
        self.btn_select = tk.Button(button_frame, text="Seleccionar Word", command=self.abrir_word,
                                     font=('Times', 10), bg='#3a7ff6', fg="#fff", width=15)
        self.btn_select.pack(side="left", padx=5)

        # Botón para insertar imágenes
        self.btn_insertar_imagenes = tk.Button(button_frame, text="Insertar Imágenes", command=self.insertar_imagenes,
                                                font=('Times', 10), bg='#3a7ff6', fg="#fff", width=15)
        self.btn_insertar_imagenes.pack(side="left", padx=5)

        self.mainloop()

    def alcerrar(self):
        #askokcancel mensaje al cerrar a la ventana
        if messagebox.askokcancel('Salir','¿Deseas cerrar la ventana?'):
            self.destroy()

    # def verificador(self):
    #     if messagebox.askokcancel('Salir','¿Desear insertar imagenes a estos documentos?'):
            