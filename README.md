# 🚀 TP3 - Modularización y Funciones en Python

**Laboratorio de Aplicaciones II · 6° G · 2026**

---

## ¿Qué es un módulo en Python?

Un **módulo** es simplemente un archivo `.py` que contiene funciones, variables o clases que podemos reutilizar en otros programas.  
En lugar de escribir todo el código en un solo archivo gigante, separamos la lógica en módulos. Esto hace que el código sea más **ordenado, legible y fácil de mantener**.

En este proyecto usamos dos archivos:

| Archivo | Rol |
|---|---|
| `logica_mision.py` | **Módulo** → contiene todas las funciones (herramientas) |
| `main.py` | **Programa principal** → importa y usa esas funciones |

---

## 🛠 Funciones creadas y para qué sirven

### 1. `calcular_combustible(distancia, consumo_por_km)`
Multiplica la distancia por el consumo y **retorna** el resultado.  
Permite saber cuánto combustible necesita la nave antes de despegar.

### 2. `configurar_nave(nombre, modelo="Explorador", estado="Óptimo")`
Configura la nave imprimiendo sus datos. Usa **argumentos con valores por defecto**, por lo que si no se indica modelo o estado, se usan los valores predeterminados automáticamente.

### 3. `obtener_coordenadas()`
No recibe parámetros. **Retorna una tupla** `(x, y, z)` con la posición actual en el espacio. En `main.py` se usa **desempaquetado (unpacking)** para leer cada coordenada por separado.

### 4. `registrar_tripulantes(*args)`
Acepta **cualquier cantidad de nombres** gracias a `*args`. Itera con un `for` e imprime a todos los tripulantes a bordo.

---

## ▶️ Cómo ejecutar el proyecto

```bash
# Clona el repositorio
git clone https://github.com/TU_USUARIO/tp3-funciones-python.git
cd tp3-funciones-python

# Ejecuta el programa principal
python main.py
```

Ambos archivos deben estar en la **misma carpeta** para que la importación funcione.

---

## 💻 Ejemplo de salida

```
==================================================
   🚀 SISTEMA DE CONTROL DE MISIÓN ESPACIAL
==================================================

[ CONFIGURACIÓN DE NAVE ]
✅ Nave configurada exitosamente:
   → Nombre : Apolo XIII
   → Modelo : Interestelar-X
   → Estado : Alerta Máxima

[ CÁLCULO DE COMBUSTIBLE ]
   Distancia      : 384,400 km
   Consumo por km : 0.85 L/km
   ⛽ Combustible total necesario: 326,740.0 litros

[ COORDENADAS ACTUALES ]
   📍 X = 142.7
   📍 Y = -38.5
   📍 Z = 9003.1

[ REGISTRO DE TRIPULANTES ]
👩‍🚀 Tripulantes a bordo:
   → Valentina López
   → Carlos Mendoza
   → Sofía Ramírez
   → Diego Fernández
   → Ana Torres

==================================================
   ✅ Sistemas listos. ¡Misión en marcha!
==================================================
```

---

> *"La lógica es el superpoder del siglo XXI."*
