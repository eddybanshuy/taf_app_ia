# Importar librerías necesarias
import pandas as pd
from faker import Faker
import random
import sqlite3

# Inicializar Faker en español
fake = Faker('es_ES')

# Definir categorías de productos
productos = ["Arroz", "Azúcar", "Aceite", "Leche", "Pan", "Carne", "Pollo", "Huevos", "Queso", "Café"]

# Generar 5000 registros
data = []
for _ in range(5000):
    producto = random.choice(productos)
    precio = round(random.uniform(0.5, 20), 2)   # precio entre 0.5 y 20 dólares
    cantidad = random.randint(1, 10)             # cantidad entre 1 y 10
    fecha = fake.date_between(start_date="-1y", end_date="today")  # fechas del último año
    cliente = fake.name()
    ciudad = fake.city()
    
    data.append([producto, precio, cantidad, fecha, cliente, ciudad])

# Crear DataFrame
df = pd.DataFrame(data, columns=["Producto", "Precio", "Cantidad", "Fecha", "Cliente", "Ciudad"])

# Guardar en CSV
df.to_csv("mini_comisariato.csv", index=False, encoding="utf-8-sig")

#Visualizar data
print(df.head())

#Script para generar la dataset sql de productos de plasticos
# Lista de productos plásticos
productos_plasticos = [
    "Juguete de plástico", "Envase plástico", "Botella PET", "Cubo organizador",
    "Utensilio de cocina plástico", "Tupper", "Pelota plástica", "Muñeco de plástico",
    "Cubo de basura plástico", "Silla plástica"
]

# Generar 5000 registros aleatorios
data_sql = []
for _ in range(5000):
    producto = random.choice(productos_plasticos)
    precio = round(random.uniform(1, 50), 2)   # precios entre 1 y 50 dólares
    cantidad = random.randint(1, 20)           # cantidad entre 1 y 20
    fecha = fake.date_between(start_date="-1y", end_date="today")
    cliente = fake.name()
    ciudad = fake.city()
    
    data_sql.append([producto, precio, cantidad, fecha, cliente, ciudad])

# Crear DataFrame
df_sql = pd.DataFrame(data_sql, columns=["Producto", "Precio", "Cantidad", "Fecha", "Cliente", "Ciudad"])

# Conectar a SQLite y crear tabla
conn = sqlite3.connect("comisariato.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas_plasticos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT,
    precio REAL,
    cantidad INTEGER,
    fecha TEXT,
    cliente TEXT,
    ciudad TEXT
)
""")

# Insertar datos
df_sql.to_sql("ventas_plasticos", conn, if_exists="replace", index=False)

# Confirmar registros
cursor.execute("SELECT COUNT(*) FROM ventas_plasticos")
print("Registros en la base de datos de plásticos:", cursor.fetchone()[0])

conn.commit()
conn.close()
