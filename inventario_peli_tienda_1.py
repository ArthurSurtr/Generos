import psycopg2 as psy
import pandas as pd

# Conexión a la base de datos
conn = psy.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="vxaw6410",
    port=5432)

# Consulta para obtener el número de clases por materia
query = """
 SELECT*FROM pelis_por_zona;
"""

# Extraer datos y convertirlos a un DataFrame de pandas
df = pd.read_sql(query, conn)

# Cerrar la conexión
conn.close()

df.to_csv("Tabla_pelis_por_zona.csv", index=False)

print("Se guardo con exito")
