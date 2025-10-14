def latencia_real(latencia_estimada):
    return latencia_estimada * 1.2

# Cálculos solicitados
latencia_a = latencia_real(200)
latencia_b = latencia_real(149)
latencia_c = latencia_real(74)

print(f"Latencia real para 200 ms: {latencia_a} ms")
print(f"Latencia real para 149 ms: {latencia_b} ms")
print(f"Latencia real para 74 ms: {latencia_c} ms")