import pandas as pd
import altair as alt

def gen_pie_chart(time_frame: str, data: pd.DataFrame):
    """
    Genera un gráfico de pastel basado en el periodo de tiempo seleccionado.

    Parámetros:
        time_frame (str): El período de tiempo ('monthly', 'qrt', 'yearly').
        data (pd.DataFrame): Datos con información de países y exportaciones/importaciones.

    Retorna:
        alt.Chart: Gráfico de pastel de Altair.
    """
    # Validación del parámetro time_frame
    if time_frame not in ["monthly", "qrt", "yearly"]:
        raise ValueError("El parámetro time_frame debe ser 'monthly', 'qrt' o 'yearly'.")

    # Filtrar datos según la selección de tiempo
    if time_frame == "monthly":
        filtered_data = data[data["month"] == 1]  # Puedes hacer que esto sea dinámico
    elif time_frame == "qrt":
        filtered_data = data[data["quarter"] == 1]  # Ajusta según la columna en tu dataset
    else:
        filtered_data = data[data["year"] == data["year"].max()]  # Último año disponible

    # Crear gráfico de pastel con Altair
    pie_chart = alt.Chart(filtered_data).mark_arc().encode(
        theta=alt.Theta("value", type="quantitative"),
        color=alt.Color("country", type="nominal"),
        tooltip=["country", "value"]
    ).properties(
        title=f"Distribución de exportaciones/importaciones - {time_frame.capitalize()}"
    )

    return pie_chart

