import numpy as np
from fichero_matematico import my_Gauss, my_LU, regression_vandermonde, polynomial

#0.DATOS DE PARTIDA

# 1. Datos para calibracion del tubo Pitot (Voltaje [V] vs Presion [kPa])
V_sensor = np.array([0.5, 1.2, 2.3, 3.1, 4.0, 4.8])
P_sensor = np.array([10.1, 25.5, 48.0, 65.2, 83.9, 101.3])
# 2. Modelo atmosferico terrestre simplificado (Altitud [m] vs Densidad [kg/m^3])
altitudes_tab = np.array([0, 5000, 10000, 15000, 20000, 25000, 30000])
densidades_tab = np.array([1.225, 0.736, 0.413, 0.194, 0.088, 0.040, 0.018])
# 3. Telemetria de vuelo: Tiempo [s] (muestreo a 1 Hz durante 2 min)
t_vuelo = np.linspace(0, 120, 121)
# Perfil de velocidad simulado [m/s] (modelo logistico)
v_vuelo = 2500 * (1 / (1 + np.exp(-0.05 * (t_vuelo- 60))))- 118

#1.BALANCE DE MASAS DE PROPELENTE
def calcular_masas():
    A = np.array([[1.0, 1.0, 1.0],[1.0, 1.0, -1.0],[1.0, -2.0, 0.0]])
    b = np.array([50000.0, 15000.0, 0.0])
##GAUSS
    resultado_gauss=my_Gauss(A.copy(), b.copy())
##LU
    resultado_lu=my_LU(A.copy(), b.copy())
    return resultado_gauss, resultado_lu


#2.CALIBRACION DEL SENSOR DE PRESION DINAMICA
def calibrar_sensor():
    coeficientes=regression_vandermonde(V_sensor, P_sensor, 2)
    return coeficientes

#3.ESTIMACION DE LA DENSIDAD ATMOSFERICA


#4.
#5.
#6.

