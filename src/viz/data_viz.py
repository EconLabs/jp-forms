import pandas as pd
from src.viz.data_viz import gen_pie_chart

# Dataset vacío esperando que lo llenen con datos reales
data = pd.DataFrame(columns=['country', 'value', 'year', 'month', 'quarter'])

# Prueba básica para verificar que la función no falla con un DataFrame vacío
try:
    chart = gen_pie_chart("monthly", data)
    chart.save("test_chart.html")
    print("✅ Gráfico generado correctamente. Revisa test_chart.html")
except Exception as e:
    print(f"❌ Error en la función: {e}")

