# main.py
# Programa principal: el que el usuario ejecuta.
# Importa y utiliza todas las funciones del módulo logica_mision.

from logica_mision import (
    calcular_combustible,
    configurar_nave,
    obtener_coordenadas,
    registrar_tripulantes,
)

if __name__ == "__main__":

    print("=" * 50)
    print("   🚀 SISTEMA DE CONTROL DE MISIÓN ESPACIAL")
    print("=" * 50)

    # ── 1. Configurar nave usando argumentos por nombre (orden cambiado) ──
    print("\n[ CONFIGURACIÓN DE NAVE ]")
    configurar_nave(estado="Alerta Máxima", nombre="Apolo XIII", modelo="Interestelar-X")

    # ── 2. Calcular combustible necesario ──
    print("\n[ CÁLCULO DE COMBUSTIBLE ]")
    distancia_km = 384_400          # distancia a la Luna en km
    consumo      = 0.85             # litros por km
    combustible  = calcular_combustible(distancia_km, consumo)
    print(f"   Distancia      : {distancia_km:,} km")
    print(f"   Consumo por km : {consumo} L/km")
    print(f"   ⛽ Combustible total necesario: {combustible:,.1f} litros")

    # ── 3. Obtener coordenadas y desempaquetar la tupla ──
    print("\n[ COORDENADAS ACTUALES ]")
    x, y, z = obtener_coordenadas()   # unpacking de la tupla
    print(f"   📍 X = {x}")
    print(f"   📍 Y = {y}")
    print(f"   📍 Z = {z}")

    # ── 4. Registrar tripulantes con *args (4+ nombres) ──
    print("\n[ REGISTRO DE TRIPULANTES ]")
    registrar_tripulantes(
        "Valentina López",
        "Carlos Mendoza",
        "Sofía Ramírez",
        "Diego Fernández",
        "Ana Torres",
    )

    print("\n" + "=" * 50)
    print("   ✅ Sistemas listos. ¡Misión en marcha!")
    print("=" * 50)
