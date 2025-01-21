import os
import pandas as pd
from sqlalchemy import create_engine

# Conectar ao banco (ajuste os parâmetros conforme necessário)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/economizze")
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files", "MICRODADOS_ENEM_2023.csv")

# Ler o CSV
df = pd.read_csv(file_path, sep=";", encoding="latin1")


# Carregar no banco de dados
df.to_sql("enem_microdados", engine, if_exists="append", index=False)