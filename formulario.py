from pydoc import text
from shutil import which
from tkinter import Tk, Label, Button, Entry, Frame, END, font
import pandas as pd

formulario = Tk()
formulario.config(bg='black')
formulario.geometry('560x388')
formulario.resizable(0,0)
formulario.title('Formulario python')

frame1 = Frame(formulario, bg='gray')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(formulario, bg='gray')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text='nombre', width=10).grid(column=0, row=0, pady=20, padx=10)
ingresa_nombre = Entry(frame1, width=35, font=('Arial',12))
ingresa_nombre.grid(column=1, row=0)

apellido = Label(frame1, text='Apellido', width=10).grid(column=0, row=1, pady=20, padx=10)
ingresa_apellido = Entry(frame1, width=35, font=('Arial',12))
ingresa_apellido.grid(column=1, row=1)

edad = Label(frame1, text='Edad', width=10).grid(column=0, row=2, pady=20, padx=10)
ingresa_edad = Entry(frame1, width=35, font=('Arial',12))
ingresa_edad.grid(column=1, row=2)

correo = Label(frame1, text='Correo', width=10).grid(column=0, row=3, pady=20, padx=10)
ingresa_correo = Entry(frame1, width=35, font=('Arial',12))
ingresa_correo.grid(column=1, row=3)

telefono = Label(frame1, text='Telefono', width=10).grid(column=0, row=4, pady=20, padx=10)
ingresa_telefono = Entry(frame1, width=35, font=('Arial',12))
ingresa_telefono.grid(column=1, row=4)

agregar = Button(frame1, width=10, font=('Arial',12, 'bold'), text='Agregar', bg='silver', bd=5)
agregar.grid(columnspan=2, row=5, pady=20, padx=10)

archivo = Label(frame2, text='Ingrese Nombre del archivo', width=25, bg='olive', font=('Arial',12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx=10)

nombre_archivo = Entry(frame2, width=23, font=('Arial',12), highlightbackground='green', highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx=10)

guardar = Button(frame2, width=10, font=('Arial',12, 'bold'), text='Guardar', bg='silver', bd=5)
guardar.grid(column=0, row=2, pady=20, padx=10)


formulario.mainloop()