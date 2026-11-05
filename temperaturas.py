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
