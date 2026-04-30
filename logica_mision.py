# logica_mision.py
# Módulo de lógica: contiene todas las funciones (herramientas) de la misión.


def calcular_combustible(distancia, consumo_por_km):
    """
    Calcula el combustible necesario para un viaje.
    Recibe la distancia y el consumo por kilómetro.
    Retorna el total de combustible requerido.
    """
    total = distancia * consumo_por_km
    return total


def configurar_nave(nombre, modelo="Explorador", estado="Óptimo"):
    """
    Configura la nave con nombre, modelo y estado.
    modelo y estado tienen valores por defecto.
    Imprime un mensaje de confirmación.
    """
    print(f"✅ Nave configurada exitosamente:")
    print(f"   → Nombre : {nombre}")
    print(f"   → Modelo : {modelo}")
    print(f"   → Estado : {estado}")


def obtener_coordenadas():
    """
    Retorna una tupla con las coordenadas actuales (x, y, z)
    que representan la posición en el espacio.
    """
    x = 142.7
    y = -38.5
    z = 9003.1
    return (x, y, z)


def registrar_tripulantes(*args):
    """
    Recibe una cantidad variable de nombres de tripulantes (*args).
    Imprime la lista de quiénes están a bordo.
    """
    print("👩‍🚀 Tripulantes a bordo:")
    for nombre in args:
        print(f"   → {nombre}")
