import sys
import tkinter
from tkinter import ttk

Ventana_principal= tkinter.Tk()

valor_radio= tkinter.StringVar()
r1=ttk.Radiobutton(Ventana_principal, text='Si', value='1', variable=valor_radio)
r1.pack(ipadx=50, ipady=50)
r2=ttk.Radiobutton(Ventana_principal, text='No', value='2', variable=valor_radio)
r2.pack(ipadx=50, ipady=50)
r3=ttk.Radiobutton(Ventana_principal, text='Talvez', value='3', variable=valor_radio)
r3.pack(ipadx=50, ipady=50)

def reinicar ():
 valor_radio.set("")

boton= ttk.Button(Ventana_principal, text='Reinicio', command=reinicar)
boton.pack()
boton.pack(ipadx=10, ipady=10, side='left')




Ventana_principal.mainloop()
