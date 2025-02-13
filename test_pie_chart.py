import sys
import os

# Agregar la ruta src al sys.path para que Python lo reconozca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from jp_imports.data_viz import gen_pie_chart
import pandas as pd

# Datos de prueba
data = pd.DataFrame({
    'country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Germany'],
    'value': [120, 80, 95, 60, 110],
    'year': [2024, 2024, 2024, 2024, 2024],
    'month': [1, 1, 2, 2, 3],
    'quarter': [1, 1, 1, 1, 2]
})

# Generar el gráfico
chart = gen_pie_chart("monthly", data)

# Mostrar el gráfico
if chart:
    chart.show()



