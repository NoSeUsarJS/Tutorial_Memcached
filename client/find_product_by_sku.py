import json

def find_product_by_sku (id, file_path="./productos.json"):
    with open(file_path, 'r') as file:
        data = json.load(file)

        for product in data:
            if product['sku'] == id:
                return product

        return None