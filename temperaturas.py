temperaturas=[18.5, 21.2, 19.8, 23.1, 25.4]

media=sum(temperaturas)/len(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)

print(temperaturas)

print("La media de las temperaturas es:", media)
print("La temperatura máxima es:", maxima)
print("La temperatura mínima es:", minima)

umbral_calor=30.0   

if maxima > umbral_calor:
    print("¡Cuidado! La temperatura máxima ha superado el umbral de calor.", umbral_calor)
else:
    print("La temperatura máxima está dentro del rango seguro.")    

contador=0

for t in temperaturas:
    if t > 20:
        contador += 1

print("El número de dias por encima de 20°C es:", contador)

for i in range(1, len(temperaturas)):
    diferencia = temperaturas[i] - temperaturas[i-1]

    if diferencia > 0:
        tendencia = "subió"
    elif diferencia < 0:
        tendencia = "bajó"
    else:
        tendencia = "se mantuvo igual"  
    print(f"Dia {i}: -> Dia {i+1}: La temperatura {tendencia} en {round(diferencia, 2)} Grados.")