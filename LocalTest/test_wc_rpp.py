from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configuración del webdriver
driver = webdriver.Chrome()

# Navegar a la página
url = "https://elcomercio.pe/archivo/todas/2023-10-04/"
driver.get(url)

# Esperar a que la página cargue completamente
time.sleep(5)

# Inicializar listas para almacenar los datos
titulos = []
fechas = []
tipos = []

# Hacer scroll hasta el final de la página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(6)

# Extraer datos
titulos_elems = driver.find_elements(By.CLASS_NAME, 'card-title')
fechas_elems = driver.find_elements(By.CLASS_NAME, 'card-date')
tipos_elems = driver.find_elements(By.CLASS_NAME, 'card-category')

for titulo_elem, fecha_elem, tipo_elem in zip(titulos_elems, fechas_elems, tipos_elems):
    titulos.append(titulo_elem.text)
    fechas.append(fecha_elem.text)
    tipos.append(tipo_elem.text)

# Crear DataFrame
data = {'Título': titulos, 'Fecha': fechas, 'Tipo': tipos}
df = pd.DataFrame(data)

# Imprimir DataFrame
print(df)

# Cerrar el navegador
driver.quit()
