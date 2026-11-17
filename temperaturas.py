from datos import temperaturas
from analisis import (
    extraer_temperaturas,
    calcular_media,
    calcular_maxima,
    calcular_minima,
    contar_mayores,
    filtrar_por_ciudad,
    dia_mas_caluroso,
    obtener_ciudades,
    ciudad_mas_calurosa,
    agrupar_por_ciudad,
    media_por_ciudad,
    maxima_por_ciudad

)

# Extraemos la columna de temperaturas
valores = extraer_temperaturas(temperaturas)

print("=== INFORME DE TEMPERATURAS ===")
print("Número de registros:", len(temperaturas))
print("Máxima:", calcular_maxima(valores))
print("Mínima:", calcular_minima(valores))
print("Media :", round(calcular_media(valores), 2))
print("Días por encima de 20 grados:", contar_mayores(valores, 20))

print("\n=== DÍA MÁS CALUROSO ===")
mas_caluroso = dia_mas_caluroso(temperaturas)
print(mas_caluroso["dia"], mas_caluroso["ciudad"], mas_caluroso["temperatura"])

print("\n=== REGISTROS DE ZARAGOZA ===")
for r in filtrar_por_ciudad(temperaturas, "Zaragoza"):
    print(r["dia"], r["temperatura"])

print("maxima:", maxima_por_ciudad(temperaturas))

maximas = maxima_por_ciudad(temperaturas)
mejor_ciudad = ""
mejor_maxima = -1000
for ciudad, maxima in maximas.items():
    if maxima > mejor_maxima:
        mejor_maxima = maxima
        mejor_ciudad = ciudad
print("Ciudad con la máxima más alta:", mejor_ciudad, mejor_maxima)
