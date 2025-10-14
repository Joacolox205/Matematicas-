def calcular_latencia_real(latencia_estimada):
    
    return latencia_estimada * 1.20

latencias_estimadas = [200, 149, 74]
for latencia in latencias_estimadas:
    latencia_real = calcular_latencia_real(latencia)
    print(f"Latencia estimada: {latencia} ms -> Latencia real: {latencia_real:.2f} ms")