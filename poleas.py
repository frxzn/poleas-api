import json
import pandas as pd
import numpy as np
from scipy.interpolate import griddata, interp1d

diametros_catalogo = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230,
                      240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 380, 400, 420, 440, 450, 480, 500, 550, 600]

df_catalogo = pd.DataFrame(diametros_catalogo, columns=["diametro"])

# Cargar TODOS las tablas interpoladas:
# TABLA POTENCIA POR CORREA PERFIL "A" INTERPOLADA.

data_pot_A = [[0.78, 0.91, 1.03, 1.16, 1.28, 1.4, 1.55, 1.69, 1.83, 2, 2.17, 2.35, 2.59, 2.82, 3.27, 3.72],
              [0.97, 1.14, 1.3, 1.46, 1.61, 1.77, 1.96, 2.14,
                  2.33, 2.54, 2.76, 3, 3.3, 3.59, 4.17, 4.75],
              [1.31, 1.54, 1.77, 2, 2.22, 2.44, 2.71, 2.97, 3.24,
                  3.54, 3.84, 4.18, 4.59, 5.01, 5.81, 6.59],
              [2.04, 2.45, 2.86, 3.26, 3.65, 4.04, 4.49, 4.94, 5.38, 5.88, 6.37, 6.92, 7.57, 8.2, 9.36, 10.4]]

df_pot_A_columns = [75, 80, 85, 90, 95, 100, 106,
                    112, 118, 125, 132, 140, 150, 160, 180, 200]

df_pot_index = [720, 960, 1440, 2880]

df_pot_A = pd.DataFrame(
    data_pot_A, columns=df_pot_A_columns, index=df_pot_index)

coordenadas_A = []
for i in df_pot_A.index:
    for j in df_pot_A.columns:

        coordenadas_A.append((i, j))

points_A = np.array(coordenadas_A)
valores_A = df_pot_A.values.reshape(64,)

grid_xA, grid_yA = np.mgrid[720:2880:2161j, 75:200:126j]
xi_A = grid_xA, grid_yA

arr_A = griddata(points_A, valores_A, xi_A)

df_int_A = pd.DataFrame(arr_A)
df_int_A.index = range(720, 2881)
df_int_A.columns = range(75, 201)

# TABLA POTENCIA POR CORREA PERFIL "B" INTERPOLADA.

data_pot_B = [[2.59, 2.86, 3.17, 3.55, 3.92, 4.3, 4.67, 5.04, 5.41, 5.85, 6.28, 6.71, 7.21, 8.27, 9.47],
              [3.28, 3.63, 4.02, 4.51, 5, 5.48, 5.96, 6.43,
                  6.9, 7.46, 8.01, 8.56, 9.19, 10.51, 12],
              [4.52, 5.01, 5.57, 6.26, 6.94, 7.61, 8.28, 8.93,
                  9.57, 10.33, 11.08, 11.81, 12.65, 14.37, 16.24],
              [7.25, 8.07, 8.97, 10.06, 11.11, 12.11, 13.05, 13.95]]

df_pot_B_columns = [125, 132, 140, 150, 160, 170,
                    180, 190, 200, 212, 224, 236, 250, 280, 315]

df_pot_B = pd.DataFrame(
    data_pot_B, columns=df_pot_B_columns, index=df_pot_index)

coordenadas_B = []
for i in df_pot_B.index:
    for j in df_pot_B.columns:

        coordenadas_B.append((i, j))

points_B = np.array(coordenadas_B)
valores_B = df_pot_B.values.reshape(60,)

grid_xB, grid_yB = np.mgrid[720:2880:2161j, 125:315:191j]
xi_B = grid_xB, grid_yB

arr_B = griddata(points_B, valores_B, xi_B)

df_int_B = pd.DataFrame(arr_B)
df_int_B.index = range(720, 2881)
df_int_B.columns = range(125, 316)

# TABLA POTENCIA POR CORREA PERFIL "C" INTERPOLADA.

data_pot_C = [[7.22, 7.94, 8.65, 9.35, 10.17, 11.03, 11.89, 13.85, 16.04, 18.42, 19.71, 20.97, 23.41, 26.18],
              [9.09, 10, 10.91, 11.8, 12.82, 13.91, 14.98, 17.41,
                  20.08, 22.93, 24.44, 25.9, 28.65, 31.63],
              [12.3, 13.54, 14.74, 15.94, 17.29, 18.7, 20.07, 23.09, 26.23, 29.33],
              [12.70125, 13.9825, 15.21875, 16.4575, 17.84875, 19.29875, 20.70625, 23.8, 26.99875, 30.13]]

df_pot_C_columns = [200, 212, 224, 236, 250,
                    265, 280, 315, 355, 400, 425, 450, 500, 560]

df_pot_C = pd.DataFrame(
    data_pot_C, columns=df_pot_C_columns, index=df_pot_index)

coordenadas_C = []
for i in df_pot_C.index:
    for j in df_pot_C.columns:

        coordenadas_C.append((i, j))

points_C = np.array(coordenadas_C)
valores_C = df_pot_C.values.reshape(56,)

grid_xC, grid_yC = np.mgrid[720:1500:781j, 200:560:361j]
xi_C = grid_xC, grid_yC

arr_C = griddata(points_C, valores_C, xi_C)

df_int_C = pd.DataFrame(arr_C)
df_int_C.index = range(720, 1501)
df_int_C.columns = range(200, 561)

# Cargar TODAS las funciones del ábaco:
# ÁBACO CORREA PERFIL "A".

x1A = [0, 1, 2, 2.5]
y1A = [100, 800, 3000, 5000]

x2A = [2.5, 40]
y2A = [100, 2880]

x3A = [25, 30, 40]
y3A = [5000, 4000, 2880]

x4A = [2.5, 25]
y4A = [5000, 5000]

# plt.loglog(x1A, y1A, x2A, y2A, x3A, y3A, x4A, y4A) "CORRER PARA CHEQUEAR ÁBACO"

f1A = interp1d(x1A, y1A)  # azul
f2A = interp1d(x2A, y2A)  # naranja
f3A = interp1d(x3A, y3A)  # verde
f4A = interp1d(x4A, y4A)  # rojo


def esta_dentro_A(potencia_diseño, velocidad_polea_motora):

    esta_adentro_A = False

    if 0 < potencia_diseño <= 2.5:
        if 100 <= velocidad_polea_motora <= float(f1A(potencia_diseño)):
            esta_adentro_A = True

    if 2.5 < potencia_diseño <= 25:
        if float(f2A(potencia_diseño)) <= velocidad_polea_motora <= float(f4A(potencia_diseño)):
            esta_adentro_A = True

    if 25 < potencia_diseño <= 40:
        if float(f2A(potencia_diseño)) <= velocidad_polea_motora <= float(f3A(potencia_diseño)):
            esta_adentro_A = True

    return esta_adentro_A

# ÁBACO CORREA PERFIL "B".


x1B = [1.6, 19.5]
y1B = [100, 1900]

x2B = [19.5, 6.5]
y2B = [1900, 5000]

x3B = [6, 80]
y3B = [100, 1900]

x4B = [80, 26]
y4B = [1900, 5000]

x5B = [6.5, 26]
y5B = [5000, 5000]

x6B = [1.6, 6]
y6B = [100, 100]

# plt.loglog(x1B, y1B, x2B, y2B, x3B, y3B, x4B, y4B, x5B, y5B, x6B, y6B) "CORRER PARA CHEQUEAR ÁBACO"

f1B = interp1d(x1B, y1B)  # azul
f2B = interp1d(x2B, y2B)  # naranja
f3B = interp1d(x3B, y3B)  # verde
f4B = interp1d(x4B, y4B)  # rojo
f5B = interp1d(x5B, y5B)  # lila
f6B = interp1d(x6B, y6B)  # marron


def esta_dentro_B(potencia_diseño, velocidad_polea_motora):

    esta_adentro_B = False

    if 1.6 < potencia_diseño <= 6:
        if float(f6B(potencia_diseño)) <= velocidad_polea_motora <= float(f1B(potencia_diseño)):
            esta_adentro_B = True

    if 6 < potencia_diseño <= 6.5:
        if float(f3B(potencia_diseño)) <= velocidad_polea_motora <= float(f1B(potencia_diseño)):
            esta_adentro_B = True

    if 6.5 < potencia_diseño <= 19.5:
        if float(f3B(potencia_diseño)) <= velocidad_polea_motora <= float(f1B(potencia_diseño)) or float(f2B(potencia_diseño)) <= velocidad_polea_motora <= float(f5B(potencia_diseño)):
            esta_adentro_B = True

    if 19.5 < potencia_diseño <= 26:
        if float(f3B(potencia_diseño)) <= velocidad_polea_motora <= float(f5B(potencia_diseño)):
            esta_adentro_B = True

    if 26 < potencia_diseño <= 80:
        if float(f3B(potencia_diseño)) <= velocidad_polea_motora <= float(f4B(potencia_diseño)):
            esta_adentro_B = True

    return esta_adentro_B

# ÁBACO CORREA PERFIL "C".


x1C = [4.2, 20]
y1C = [100, 700]

x2C = [20, 10]
y2C = [700, 3800]

x3C = [10, 400]
y3C = [3800, 3800]

x4C = [40, 130]
y4C = [100, 700]

x5C = [130, 90]
y5C = [700, 1440]

x6C = [90, 400]
y6C = [1440, 1440]

x7C = [4.2, 40]
y7C = [100, 100]

# plt.loglog(x1C, y1C, x2C, y2C, x3C, y3C, x4C, y4C, x5C, y5C, x6C, y6C, x7C, y7C) "CORRER PARA CHEQUEAR ÁBACO"

f1C = interp1d(x1C, y1C)  # azul
f2C = interp1d(x2C, y2C)  # naranja
f3C = interp1d(x3C, y3C)  # verde
f4C = interp1d(x4C, y4C)  # rojo
f5C = interp1d(x5C, y5C)  # lila
f6C = interp1d(x6C, y6C)  # marron
f7C = interp1d(x7C, y7C)  # rosita


def esta_dentro_C(potencia_diseño, velocidad_polea_motora):

    esta_adentro_C = False

    if 4.2 < potencia_diseño <= 10:
        if float(f7C(potencia_diseño)) <= velocidad_polea_motora <= float(f1C(potencia_diseño)):
            esta_adentro_C = True

    if 10 < potencia_diseño <= 20:
        if float(f7C(potencia_diseño)) <= velocidad_polea_motora <= float(f1C(potencia_diseño)) or float(f2C(potencia_diseño)) <= velocidad_polea_motora <= float(f3C(potencia_diseño)):
            esta_adentro_C = True

    if 20 < potencia_diseño <= 40:
        if float(f7C(potencia_diseño)) <= velocidad_polea_motora <= float(f3C(potencia_diseño)):
            esta_adentro_C = True

    if 40 < potencia_diseño <= 90:
        if float(f4C(potencia_diseño)) <= velocidad_polea_motora <= float(f3C(potencia_diseño)):
            esta_adentro_C = True

    if 90 < potencia_diseño <= 130:
        if float(f4C(potencia_diseño)) <= velocidad_polea_motora <= float(f5C(potencia_diseño)):
            esta_adentro_C = True

    if 130 < potencia_diseño <= 400:
        if float(f6C(potencia_diseño)) <= velocidad_polea_motora <= float(f3C(potencia_diseño)):
            esta_adentro_C = True

    return esta_adentro_C


def seleccionar_poleas(potencia_motor, velocidad_polea_motora, relac_transmision, fact_servicio):

    potencia_motor = float(potencia_motor)
    velocidad_polea_motora = float(velocidad_polea_motora)
    relac_transmision = float(relac_transmision)
    fact_servicio = float(fact_servicio)
    potencia_correa = 1

    diametro1_1canal_A = 0
    diametro2_1canal_A = 0
    diametro1_1canal_B = 0
    diametro2_1canal_B = 0
    diametro1_1canal_C = 0
    diametro2_1canal_C = 0

    diametro1_2canales_A = 0
    diametro2_2canales_A = 0
    diametro1_2canales_B = 0
    diametro2_2canales_B = 0
    diametro1_2canales_C = 0
    diametro2_2canales_C = 0

    diametro1_3canales_A = 0
    diametro2_3canales_A = 0
    diametro1_3canales_B = 0
    diametro2_3canales_B = 0
    diametro1_3canales_C = 0
    diametro2_3canales_C = 0

    diametro1_4canales_A = 0
    diametro2_4canales_A = 0
    diametro1_4canales_B = 0
    diametro2_4canales_B = 0
    diametro1_4canales_C = 0
    diametro2_4canales_C = 0

    # Cálculo Potencia de diseño:
    potencia_diseño = potencia_motor * fact_servicio

    # Cálculo diámetro mínimo:
    diametro_minimo = (60000*10)/(3.14*velocidad_polea_motora)

    lista_df = []

    if esta_dentro_A(potencia_diseño, velocidad_polea_motora):
        lista_df.append(df_int_A)

    if esta_dentro_B(potencia_diseño, velocidad_polea_motora):
        lista_df.append(df_int_B)

    if esta_dentro_C(potencia_diseño, velocidad_polea_motora):
        lista_df.append(df_int_C)

    # INICIO LÓGICA DEL PROGRAMA:
    for df_int in lista_df:

        if df_int.size == df_int_A.size:

            perfil = "A"

        elif df_int.size == df_int_B.size:

            perfil = "B"

        elif df_int.size == df_int_C.size:

            perfil = "C"

        entrar_4canales_A = True
        entrar_3canales_A = True
        entrar_2canales_A = True
        entrar_1canal_A = True
        entrar_4canales_B = True
        entrar_3canales_B = True
        entrar_2canales_B = True
        entrar_1canal_B = True
        entrar_4canales_C = True
        entrar_3canales_C = True
        entrar_2canales_C = True
        entrar_1canal_C = True

        entrar_4canales = True
        entrar_3canales = True
        entrar_2canales = True
        entrar_1canal = True

        while True:

            diametro_1 = 0
            diametro_2 = 0

            for i in range(len(df_catalogo)):

                if df_catalogo["diametro"][i] >= diametro_minimo:

                    diametro_1 = df_catalogo["diametro"][i]

                    for j in range(len(df_catalogo)):

                        if diametro_1 * (relac_transmision - relac_transmision*0.03) <= df_catalogo["diametro"][j] <= diametro_1 * (relac_transmision + relac_transmision*0.03):

                            diametro_2 = df_catalogo["diametro"][j]
                            break

                    if diametro_2 > 0:

                        break

            for columna in df_int.columns:

                if diametro_1 <= columna:

                    for filas in df_int.index.values:

                        if velocidad_polea_motora <= filas:

                            potencia_correa = df_int[columna][filas]
                            break
                    break

            cantidad_correas = potencia_diseño / potencia_correa

            if 3 < cantidad_correas <= 4 and entrar_4canales:

                if perfil == "A" and entrar_4canales_A:

                    diametro1_4canales_A = diametro_1
                    diametro2_4canales_A = diametro_2
                    entrar_4canales_A = False

                elif perfil == "B" and entrar_4canales_B:

                    diametro1_4canales_B = diametro_1
                    diametro2_4canales_B = diametro_2
                    entrar_4canales_B = False

                elif perfil == "C" and entrar_4canales_C:

                    diametro1_4canales_C = diametro_1
                    diametro2_4canales_C = diametro_2
                    entrar_4canales_C = False

                else:
                    entrar_4canales = False

            elif 2 < cantidad_correas <= 3 and entrar_3canales:

                if perfil == "A" and entrar_3canales_A:

                    diametro1_3canales_A = diametro_1
                    diametro2_3canales_A = diametro_2
                    entrar_3canales_A = False

                elif perfil == "B" and entrar_3canales_B:

                    diametro1_3canales_B = diametro_1
                    diametro2_3canales_B = diametro_2
                    entrar_3canales_B = False

                elif perfil == "C" and entrar_3canales_C:

                    diametro1_3canales_C = diametro_1
                    diametro2_3canales_C = diametro_2
                    entrar_3canales_C = False

                else:
                    entrar_3canales = False

            elif 1 < cantidad_correas <= 2 and entrar_2canales:

                if perfil == "A" and entrar_2canales_A:

                    diametro1_2canales_A = diametro_1
                    diametro2_2canales_A = diametro_2
                    entrar_2canales_A = False

                elif perfil == "B" and entrar_2canales_B:

                    diametro1_2canales_B = diametro_1
                    diametro2_2canales_B = diametro_2
                    entrar_2canales_B = False

                elif perfil == "C" and entrar_2canales_C:

                    diametro1_2canales_C = diametro_1
                    diametro2_2canales_C = diametro_2
                    entrar_2canales_C = False

                else:
                    entrar_2canales = False

            elif cantidad_correas <= 1 and entrar_1canal:

                if perfil == "A" and entrar_1canal_A:

                    diametro1_1canal_A = diametro_1
                    diametro2_1canal_A = diametro_2
                    entrar_1canal_A = False

                elif perfil == "B" and entrar_1canal_B:

                    diametro1_1canal_B = diametro_1
                    diametro2_1canal_B = diametro_2
                    entrar_1canal_B = False

                elif perfil == "C" and entrar_1canal_C:

                    diametro1_1canal_C = diametro_1
                    diametro2_1canal_C = diametro_2
                    entrar_1canal_C = False

                else:
                    entrar_1canal = False
            else:

                diametro_minimo = diametro_1 + 1

                if diametro_minimo > 600:

                    #"No hay solucion"
                    break

    resultados = {
        'perfil_A': {
            1: {
                'min': int(diametro1_1canal_A),
                'max': int(diametro2_1canal_A),
            },
            2: {
                'min': int(diametro1_2canales_A),
                'max': int(diametro2_2canales_A),
            },
            3: {
                'min': int(diametro1_3canales_A),
                'max': int(diametro2_3canales_A),
            },
            4: {
                'min': int(diametro1_4canales_A),
                'max': int(diametro2_4canales_A),
            },
        },
        'perfil_B': {
            1: {
                'min': int(diametro1_1canal_B),
                'max': int(diametro2_1canal_B),
            },
            2: {
                'min': int(diametro1_2canales_B),
                'max': int(diametro2_2canales_B),
            },
            3: {
                'min': int(diametro1_3canales_B),
                'max': int(diametro2_3canales_B),
            },
            4: {
                'min': int(diametro1_4canales_B),
                'max': int(diametro2_4canales_B),
            },
        },
        'perfil_C': {
            1: {
                'min': int(diametro1_1canal_C),
                'max': int(diametro2_1canal_C),
            },
            2: {
                'min': int(diametro1_2canales_C),
                'max': int(diametro2_2canales_C),
            },
            3: {
                'min': int(diametro1_3canales_C),
                'max': int(diametro2_3canales_C),
            },
            4: {
                'min': int(diametro1_4canales_C),
                'max': int(diametro2_4canales_C),
            },
        },
    }

    return resultados