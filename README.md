# taf_app_ia
Trabajo académico final escrito: Genera una aplicación de Inteligencia Artificial que use librerías de software libre a través de herramientas colaborativas


🛒 Proyecto Mini-Comisariato con Python
📌 Descripción
Este proyecto simula un mini-comisariato utilizando datos ficticios generados con la librería Faker. Se construyen dos datasets:

CSV con productos de supermercado.

SQL (SQLite) con productos plásticos (juguetes, envases, utensilios, etc.).

El objetivo es aplicar técnicas de recolección, análisis y visualización de datos usando Pandas y Matplotlib, integrando ambas fuentes en un dataset final para análisis.

⚙️ Tecnologías utilizadas
Python 3.10+

Pandas → análisis y manipulación de datos.

Matplotlib → visualización de datos.

SQLite3 → base de datos ligera.

Faker → generación de datos ficticios en español.

Jupyter Lab → entorno interactivo para notebooks.


🚀 Instalación y ejecución
1. Clonar el repositorio
Terminal
git clone https://github.com/tu_usuario/mini-comisariato.git
cd mini-comisariato
2. Crear entorno virtual (opcional pero recomendado)
   
Terminal

python -m virtualen nombre_del_entorno

source nombre_del_entorno/bin/activate   # Linux/Mac

nombre_del_entorno\Scripts\activate      # Windows

4. Instalar dependencias
   
Terminal

pip install -r requirements.txt

6. Ejecutar Jupyter Lab

Terminal

jupyter lab

Abrir el archivo notebook_proyecto.ipynb y ejecutar las celdas.

📊 Visualizaciones generadas
Ventas totales por producto (CSV) → gráfico de barras.

Ventas mensuales (SQL) → gráfico de líneas.

Ventas totales por producto (Dataset final) → gráfico de barras integrando ambos datasets.

Producto más vendido por mes → gráfico de barras con etiquetas del producto ganador.

✅ Resultados
Se integraron dos fuentes de datos distintas (CSV y SQL).

Se identificaron los productos más vendidos y los meses con mayor volumen de ventas.

Se generó un dataset final limpio (mini_comisariato_final.csv) listo para análisis.
