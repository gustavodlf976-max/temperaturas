from analisis import  (
    calcular_media,
    contar_mayores,
    clasificar_temperaturas,
    resumen_temperaturas
)
temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=calcular_media(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)

print(temperaturas)

print("La media de las temperaturas es:", media)
print("La temperatura máxima es:", maxima)
print("La temperatura mínima es:", minima)

umbral_calor=22.0   

if maxima > umbral_calor:
    print("¡Cuidado! La temperatura máxima ha superado el umbral de calor.", umbral_calor)
else:
    print("La temperatura máxima está dentro del rango seguro.")    

#contar temperaturas superiores al umbral
print(f"El número de dias por encima de {umbral_calor} es:", contar_mayores(temperaturas, umbral_calor))

for i in range(1, len(temperaturas)):
    diferencia = temperaturas[i] - temperaturas[i-1]

    if diferencia > 0:
        tendencia = "subió"
    elif diferencia < 0:
        tendencia = "bajó"
    else:
        tendencia = "se mantuvo igual"  
    print(f"Dia {i}: -> Dia {i+1}: La temperatura {tendencia} en {round(diferencia, 2)} Grados.")

print ("------Clasificación de temperaturas------")

print (resumen_temperaturas(temperaturas))


