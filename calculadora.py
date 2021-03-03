from tkinter import *

#ventana
wn = Tk()
wn.title('Calculator')

i = 0


#Entrada
e_text = Entry(wn, font= ('sans-serif 20'))
e_text.grid(row= 0, column= 0, columnspan= 4, padx= 5, pady= 5)

def click_boton(valor):
    global i
    e_text.insert(i, valor)
    i +=1

def borrar():
    e_text.delete(0, END)
    i = 0


def hacer_operacion():
    ecuacion = e_text.get()
    resultado = eval(ecuacion)
    e_text.delete(0, END)
    e_text.insert(0,resultado)
    i = 0


#botones
boton1 = Button(wn, text= "1", width= 4, height= 2, command= lambda: click_boton(1))
boton2 = Button(wn, text= '2', width= 5, height= 2, command= lambda: click_boton(2))
boton3 = Button(wn, text= '3', width= 5, height= 2, command= lambda: click_boton(3))
boton4 = Button(wn, text= '4', width= 5, height= 2, command= lambda: click_boton(4))
boton5 = Button(wn, text= '5', width= 5, height= 2, command= lambda: click_boton(5))
boton6 = Button(wn, text= '6', width= 5, height= 2, command= lambda: click_boton(6))
boton7 = Button(wn, text= '7', width= 5, height= 2, command= lambda: click_boton(7))
boton8 = Button(wn, text= '8', width= 5, height= 2, command= lambda: click_boton(8))
boton9 = Button(wn, text= '9', width= 5, height= 2, command= lambda: click_boton(9))
boton0 = Button(wn, text= '0', width= 13, height= 2, command= lambda: click_boton(0))

boton_borrar = Button(wn, text= 'C', width= 5, height= 2, command= lambda: borrar())
boton_parentesis1 = Button(wn, text= '(', width= 5, height= 2, command= lambda: click_boton('('))
boton_parentesis2 = Button(wn, text= ')', width= 5, height= 2, command= lambda: click_boton(')'))
boton_coma = Button(wn, text= ',', width= 5, height= 2, command= lambda: click_boton(','))

boton_div = Button(wn, text= '/', width= 5, height= 2, command= lambda: click_boton('/'))
boton_mult = Button(wn, text= 'x', width= 5, height= 2, command= lambda: click_boton('*'))
boton_suma = Button(wn, text= '+', width= 5, height= 2, command= lambda: click_boton('+'))
boton_resta = Button(wn, text= '-', width= 5, height= 2, command= lambda: click_boton('-'))
boton_igual = Button(wn, text= '=', width= 5, height= 2, command= lambda: hacer_operacion())

#botones en pantalla

boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_coma.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)





















wn.mainloop()
