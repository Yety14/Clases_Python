import pandas as pd

# Creamos una tabla simulada con notas de alumnos
datos = {
    'Estudiante': ['Ana', 'Juan', 'Sofía', 'Carlos'],
    'Examen_1': [7, 4, 8, 3],
    'Examen_2': [6, 9, 5, 2]
}
df = pd.DataFrame(datos)

# ¿Quiénes aprobaron ambos exámenes?
# ❌ ESTO DA ERROR EN PANDAS:
# aprobados = df[(df['Examen_1'] >= 5) and (df['Examen_2'] >= 5)]

# ✅ ESTO SÍ FUNCIONA (Usando el operador bit a bit '&'):
aprobados = df[(df['Examen_1'] >= 5) & (df['Examen_2'] >= 5)]

print(aprobados)