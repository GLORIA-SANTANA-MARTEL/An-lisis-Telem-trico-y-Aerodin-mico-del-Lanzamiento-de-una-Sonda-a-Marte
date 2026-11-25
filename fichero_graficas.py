import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from numpy import linspace
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
  #mejora 3
    ax.
    ax.legend() #nombre leyenda(que representa cada color etc)


#2 SENSOR 
def grafica_sensor(ax, voltaje, presion, coeficintes):
    ax.clear()
    ax.plot(voltaje, presion, "o", label="Datos sensor")  # dibuja los puntos experimentales de la tabla


    ax.set_title("Calibración del Sensor de Presión Dinámica")
    ax.set_xlabel("Volataje del sensor [V]")
    ax.set_ylabel("Presión dinámica [kPa]")
    ax.legend()


#3 ALTITUD
def grafica_altitud()
    ax.clear()

    ax.set_title("Reconstruccion de la trayectoria, altitud")
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.legend()


#4 DENSIDAD
def grafica_densidad()
    ax.clear()

    ax.set_title("Estimación de la densidad atmosférica")
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.legend()

#5 ACELERACION
def grafica_aceleracion()
    ax.clear()

    ax.set_title("Calculo de la aceleración estructural")
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.legend()

#6 MACH 1
def grafica_mach1()
    ax.clear()

    ax.set_title("Instante crítico de Mach 1")
    ax.set_xlabel("")
    ax.set_ylabel("")

    ax.legend()