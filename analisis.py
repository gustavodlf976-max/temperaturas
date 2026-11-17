# ============================================
# Funciones para listas de números (Reto 3)
# ============================================

# Calcular la media de una lista de números
def calcular_media(lista):
    return sum(lista) / len(lista)


# Calcular la temperatura máxima
def calcular_maxima(lista):
    return max(lista)


# Calcular la temperatura mínima
def calcular_minima(lista):
    return min(lista)


# Contar cuántos valores superan un umbral
def contar_mayores(lista, umbral):
    contador = 0
    for t in lista:
        if t > umbral:
            contador += 1
    return contador


# Clasificar una temperatura en Frío, Templado o Caliente
def clasificar_temperaturas(t):
    if t < 20:
        return "Frío"
    elif t >= 25:
        return "Caliente"
    else:
        return "Templado"


# Devolver cada temperatura con su clasificación
def resumen_temperaturas(lista):
    resumen = []
    for t in lista:
        etiqueta = clasificar_temperaturas(t)
        resumen.append((t, etiqueta))
    return resumen


# ============================================
# Funciones para listas de diccionarios (Reto 4)
# ============================================

# Sacar la columna de temperaturas
def extraer_temperaturas(registros):
    valores = []
    for r in registros:
        valores.append(r["temperatura"])
    return valores


# Quedarse solo con los registros de una ciudad
def filtrar_por_ciudad(registros, ciudad):
    resultado = []
    for r in registros:
        if r["ciudad"] == ciudad:
            resultado.append(r)
    return resultado


# Devolver el registro con la temperatura más alta
def dia_mas_caluroso(registros):
    mas_caluroso = registros[0]
    for r in registros:
        if r["temperatura"] > mas_caluroso["temperatura"]:
            mas_caluroso = r
    return mas_caluroso


# Lista de ciudades sin repetir
def obtener_ciudades(registros):
    ciudades = []
    for r in registros:
        if r["ciudad"] not in ciudades:
            ciudades.append(r["ciudad"])
    return ciudades


# Ciudad con la temperatura media más alta
def ciudad_mas_calurosa(registros):
    mejor_ciudad = ""
    mejor_media = -1000
    for ciudad in obtener_ciudades(registros):
        registros_ciudad = filtrar_por_ciudad(registros, ciudad)
        valores_ciudad = extraer_temperaturas(registros_ciudad)
        media = calcular_media(valores_ciudad)
        if media > mejor_media:
            mejor_media = media
            mejor_ciudad = ciudad
    return mejor_ciudad

def agrupar_por_ciudad(registros):
    grupos = {}
    for r in registros:
        ciudad = r["ciudad"]
        if ciudad not in grupos:
            grupos[ciudad] = []
        grupos[ciudad].append(r["temperatura"])
    return grupos

def media_por_ciudad(registros):
    grupos = agrupar_por_ciudad(registros)
    resultado = {}
    for ciudad, valores in grupos.items():
        resultado[ciudad] = calcular_media(valores)
    return resultado

def maxima_por_ciudad(registros):
    grupos = agrupar_por_ciudad(registros)
    resultado = {}
    for ciudad, valores in grupos.items():
        resultado[ciudad] = calcular_maxima(valores)
    return resultado