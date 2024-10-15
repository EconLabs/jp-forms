from sqlmodel import SQLModel, Field
from typing import Optional

class JP304Validator(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_month: str
    end_month: str
    year: str
    name: str
    direction: str
    liaison_officer: str
    title: str
    tel: str

    nombre_agencia_federal_1: str
    catalogo_federal_1: str
    sai_federal_1: str
    titulo_federal_1: str
    aportacion_aprobada_federal_1: str
    fecha_aprobacion_federal_1: str
    aportacion_recibida_federal_1: str
    fecha_recibo_federal_1: str
    aportacion_gastada_federal_1: str
    fecha_gasto_federal_1: str

    nombre_agencia_federal_2: str
    catalogo_federal_2: str
    sai_federal_2: str
    titulo_federal_2: str
    aportacion_aprobada_federal_2: str
    fecha_aprobacion_federal_2: str
    aportacion_recibida_federal_2: str
    fecha_recibo_federal_2: str
    aportacion_gastada_federal_2: str
    fecha_gasto_federal_2: str

    nombre_agencia_federal_3: str
    catalogo_federal_3: str
    sai_federal_3: str
    titulo_federal_3: str
    aportacion_aprobada_federal_3: str
    fecha_aprobacion_federal_3: str
    aportacion_recibida_federal_3: str
    fecha_recibo_federal_3: str
    aportacion_gastada_federal_3: str
    fecha_gasto_federal_3: str

    nombre_agencia_federal_4: str
    catalogo_federal_4: str
    sai_federal_4: str
    titulo_federal_4: str
    aportacion_aprobada_federal_4: str
    fecha_aprobacion_federal_4: str
    aportacion_recibida_federal_4: str
    fecha_recibo_federal_4: str
    aportacion_gastada_federal_4: str
    fecha_gasto_federal_4: str

    nombre_agencia_federal_5: str
    catalogo_federal_5: str
    sai_federal_5: str
    titulo_federal_5: str
    aportacion_aprobada_federal_5: str
    fecha_aprobacion_federal_5: str
    aportacion_recibida_federal_5: str
    fecha_recibo_federal_5: str
    aportacion_gastada_federal_5: str
    fecha_gasto_federal_5: str

    # Local agencies fields
    agencia_local_table_box_1: str
    catalogo_local_1: str
    programa_local_1: str
    aportacion_federal_aprobada_local_1: str
    fecha_aprobacion_local_1: str
    aportacion_federal_recibida_local_1: str
    fecha_recibo_local_1: str
    aportacion_federal_gastada_local_1: str
    fecha_gasto_local_1: str
    numero_cuenta_local_1: str

    agencia_local_table_box_2: str
    catalogo_local_2: str
    programa_local_2: str
    aportacion_federal_aprobada_local_2: str
    fecha_aprobacion_local_2: str
    aportacion_federal_recibida_local_2: str
    fecha_recibo_local_2: str
    aportacion_federal_gastada_local_2: str
    fecha_gasto_local_2: str
    numero_cuenta_local_2: str

    agencia_local_table_box_3: str
    catalogo_local_3: str
    programa_local_3: str
    aportacion_federal_aprobada_local_3: str
    fecha_aprobacion_local_3: str
    aportacion_federal_recibida_local_3: str
    fecha_recibo_local_3: str
    aportacion_federal_gastada_local_3: str
    fecha_gasto_local_3: str
    numero_cuenta_local_3: str

    agencia_local_table_box_4: str
    catalogo_local_4: str
    programa_local_4: str
    aportacion_federal_aprobada_local_4: str
    fecha_aprobacion_local_4: str
    aportacion_federal_recibida_local_4: str
    fecha_recibo_local_4: str
    aportacion_federal_gastada_local_4: str
    fecha_gasto_local_4: str
    numero_cuenta_local_4: str

    agencia_local_table_box_5: str
    catalogo_local_5: str
    programa_local_5: str
    aportacion_federal_aprobada_local_5: str
    fecha_aprobacion_local_5: str
    aportacion_federal_recibida_local_5: str
    fecha_recibo_local_5: str
    aportacion_federal_gastada_local_5: str
    fecha_gasto_local_5: str
    numero_cuenta_local_5: str
