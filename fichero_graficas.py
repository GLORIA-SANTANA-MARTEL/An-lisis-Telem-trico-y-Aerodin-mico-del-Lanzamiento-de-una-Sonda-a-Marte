import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

#1 MASAS
def grafica_masas(ax, gauss, lu):
    ax.clear() #limipia la grafica para q no se sobreponga con la anterior si hago un cambio 
    tanques = ["Tanque 1", "Tanque 2", "Tanque 3"]
    ax.plot(tanques, gauss, "o", label="Gauss")  # dibuja masas por Gauss
    ax.plot(tanques, lu, "x", label="LU")  # dibuja masas por LU encima de la de gauss (se superponen
    ax.set_title("Balance de Masas de Propelente") #nombre grafica
    ax.set_xlabel("Tanques de propelente") #nombre eje x
    ax.set_ylabel("Masa [kg]") #nombre eje y
    #mejora 1
    ax.set_ylim(0, 26000)  #fija eje y desde 0 kg para ver la proporción real y dejar hueco arriba
    #mejora 2
    ax.grid(True)  # dibuja líneas de referencia para leer mejor las masas del eje y, el true la enciende, sino asumiria q siempre dberia estar
    ax.legend() #nombre leyenda(que representa cada color etc)



#2 SENSOR PITOT
#3 ALTITUD
#4 DENSIDAD
#5 ACELERACION
#6 MACH 1