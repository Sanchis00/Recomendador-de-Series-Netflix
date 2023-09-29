'''Programa que te recomienda series o películas de Netflix basándose
en input del usuario (una película o serie que le haya gustado mucho)'''


# Importamos todos los módulos necesarios
from tkinter import *
from tkinter import messagebox
from nltk import *
import pandas as pd

file = "netflix_titles.csv"
datos = pd.read_csv(file)
datos_co = datos.copy()

# Ventana principal

screen = Tk()
screen.title("Recomendacion de Netflix")
screen.geometry("400x500")
screen.resizable(0,0)
screen.config(bg='#542344')
icono = screen.iconbitmap('netflix.ico')



# Etiqueta Instrucciones

instrucciones = Label(screen,text = "Bienvenido. Introduce en inglés tu serie o pelicula favorita:",bg='#542344',fg="white",
                      font=('Helvetica',10,'bold'),justify='center')
instrucciones.grid(row=0,column=1,padx=10,pady=10)



# Funcion encargada de la recomendacion
def ofrecer_usuario(genero,casting,director,peli):
 
    #Listas de variables
    lista_casting = []
    lista_recomendadas = []
    lista_muy_recomendadas = []
    lista_genero = []
    i = 0

    #Bucles para separar el reparto por actores y los generos individualmente
    for cast in casting:
        lista_casting.append(cast)

    for gen in genero:
        lista_genero.append(gen)
    
 
    # Algoritmo de recomendación
    
    for index,dato2 in datos_co.iterrows():
        if dato2['title'].lower() != peli.lower():
            casting_x = str(dato2['cast']).split(',')
            genero_x = str(dato2['listed_in']).split(',')
            recomendacion = dato2['title']
            for c in casting_x:
                if c in lista_casting:
                    i+=1
                    if i>2:
                        for g in genero_x:
                            if g in lista_genero:
                                
                                if len(lista_recomendadas)< 10 and recomendacion not in lista_recomendadas: lista_recomendadas.append(recomendacion)
                                if dato2['director'] == director:
                                    if recomendacion not in lista_muy_recomendadas: lista_muy_recomendadas.append(recomendacion)

                        
                                
    if lista_recomendadas == [] and lista_muy_recomendadas == []: messagebox.showinfo(message="No hay ninguna recomendación óptima")
    else: messagebox.showinfo(title="Recomendaciones",message=f"Recomendaciones: {lista_recomendadas}\nRecomendaciones mas optimas: {lista_muy_recomendadas}")
    
    
# Funcion encargada de recibir el input del usuario y enviarlo a la funcion anterior
def procesar_info():
    try:
        peli_serie_usuario = input_user.get()
        for index,dato in datos_co.iterrows():
            if dato['title'].lower() == peli_serie_usuario.lower():
                genero = dato['listed_in'].split(',')
                casting = str(dato['cast']).split(',')
                director = dato['director']
        return ofrecer_usuario(genero, casting,director,peli_serie_usuario)        
    except:
        messagebox.showerror(title="Error",message="Puede que la serie / pelicula no se encuentre en Netflix, o no esté escrita correctamente")
    
    
# Caja de texto para el input
input_user = Entry(screen,justify='center',bg='gray',font=('Helvetica',12,'bold'),fg='white')
input_user.grid(row=1,column=1,pady=10)

# Boton Buscar Recomendaciones que activa el proceso
boton_recomendar = Button(screen,justify='center',text="Buscar recomendaciones",bg='lightblue',fg='#542344',command=procesar_info)
boton_recomendar.grid(row=2,column=1)

# Instrucciones
lab_inst = Label(screen,justify='center',font=('Helvetica',11,'bold'),bg='#542344',fg='white',text="Este sistema te recomendará películas / series que\ntengan, al menos, dos actores y un género en común. \nSi, además, coinciden en su director, el sistema las\npresentará como muy recomendadas")
lab_inst.grid(row=6,column=1,pady=50)

lab_inst = Label(screen,justify='center',font=('Helvetica',11,'bold'),bg='black',fg='white',text="IMPORTANTE: La base de datos\n en la que está basado el programa data de 2021, por\n lo que puede que con la peliculas actuales no\n funcione la recomendacion")
lab_inst.grid(row=7,column=1,pady=30)



screen.mainloop()