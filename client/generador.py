import json
import random

def generar_nombre(marca, tipo, version):
    # Generar un nombre de producto basado en la marca, tipo y versión
    return f"{marca} {tipo} - {version}"

marcas = ["Apple", "Samsung", "Dell", "HP", "Lenovo", "Sony", "Microsoft", "Asus", "Acer", "LG","Toshiba",
          "Panasonic","MSI","Huawei","Razer","Logitech", "AMD", "Kingston","Philips", "SanDisk","Canon", 
          "Thomas", "Olidata", "IBM"]
tipos = ["Laptop", "Smartphone", "Tablet", "PC de Escritorio", "Impresora", "Monitor", "Auriculares", 
         "Teclado","Mouse","Camara digital", "Cargador","impresora 3D", "Monitor Curvo", 
         "Auriculares Inalambricos", "Camara de Seguridad","Escaner"]
versiones = ["1.2", "Pro", "Lite", "Max", "Plus", "Ultra", "S", "X","1.7","3.5","1.0","1,3","1.8","2.0","2.3",
             "2.7","2.9","4.8", "4.9", "5.0", "Nano"]
year = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]

productos = []

for contador, _ in enumerate(range(100000)):  
    marca = random.choice(marcas)
    tipo = random.choice(tipos)
    version = random.choice(versiones)
    producto = {
        'sku': contador,
        'nombre': generar_nombre(marca, tipo, version),
    }
    productos.append(producto)

# Guardar la lista de productos en un archivo JSON
with open('productos.json', 'w') as archivo:
    json.dump(productos, archivo, indent=4)

print("JSON de productos generado y guardado.")
