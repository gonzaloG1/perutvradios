import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage

class Form_master_1():

    def userDatos():
        pass
                                      
    def __init__(self,master=None):
        self.master=master
        self.ventana = tk.Tk()
        self.ventana.title('Pagina principal')
        self.ventana.resizable(3, 3)
        self.ventana.geometry("1500x350")

        logo_icon=r"D:\2024\Tesis\software\perutvradios\app escritorio python\logo.png"
        icon = PhotoImage(file=logo_icon)
        self.ventana.iconphoto(False, icon)
        
        #centrar la ventana en la pantalla principal
        self.ventana.update_idletasks()
        width=self.ventana.winfo_width()
        height=self.ventana.winfo_height()
        screen_width=self.ventana.winfo_screenwidth()
        screen_height=self.ventana.winfo_screenheight()
        x=(screen_width//2)-(width//2)
        y=(screen_height//2)-(height//2)
        self.ventana.geometry(f'{width}x{height}+{x}+{y}')

        # Título en la parte superior
        title_frame = tk.Frame(self.ventana, bg='#fcfcfc')
        title_frame.pack(side="top", fill=tk.X, pady=10)
        

        logo_path = r"D:\2024\Tesis\software\perutvradios\app escritorio python\logo.png"

        

        # Cargar el logo
        self.logo = tk.PhotoImage(file=logo_path)
        self.label_logo = tk.Label(master, image=self.logo)
        self.label_logo.pack(pady=20)

        # Frame para los botones
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        #asociar el evento de cerrar con una función
        self.ventana.protocol('WM_DELETE_WINDOW',self.alcerrar)

        # Botones distribuidos horizontalmente
        button_frame = tk.Frame(frame_form_fill, bg='#fcfcfc')
        button_frame.pack(side="top", pady=20)


        general = tk.Button(button_frame, text="Generación de PDF de Datos Generales y Tarifa de Emisora", font=('Times', 15), 
                            bg='#FC0E03', bd=0, fg="#fff", width=150, command=self.userDatos)
        general.grid(row=0, column=0, padx=10,sticky='ew')

        cpm = tk.Button(button_frame, text="Generación de PDF de Datos PCM", font=('Times', 15), 
                        bg='#FC0E03', bd=0, fg="#fff", width=150, command=self.userCpm)
        cpm.grid(row=0, column=1, padx=10, sticky='ew')

        word = tk.Button(button_frame, text="Inserción de logo y firma en documentos Word de PCM", font=('Times', 15), 
                         bg='#FC0E03', bd=0, fg="#fff", width=150,command=self.userWord)
        word.grid(row=0, column=2, padx=10, sticky='ew')

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        self.ventana.mainloop()

    def alcerrar(self):
        #askokcancel mensaje al cerrar a la ventana
        if messagebox.askokcancel('Salir','¿Deseas cerrar la ventana?'):
            self.ventana.destroy()

    


    