import matplotlib.pyplot as plt
from fichero_fisico import calcular_masas, calibrar_sensor
from fichero_graficas import grafica_masas

#1.BALANCE DE MASAS DE PROPELENTE
gauss, lu = calcular_masas()
print(gauss)
print(lu)

## GRAFICA MASAS
fig, ax = plt.subplots(1, 1)
grafica_masas(ax, gauss, lu)
plt.show()


#2.CALIBRACION DEL SENSOR DE PRESION DINAMICA
coeficientes = calibrar_sensor()
print(coeficientes)


