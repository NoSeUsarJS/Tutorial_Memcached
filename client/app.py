import time
import numpy as np
import memcache
import os
from find_product_by_sku import find_product_by_sku

class CacheClient:
    def __init__(self):
        servers = ['mc1:11211', 'mc2:11211']
        self.mc = memcache.Client(servers)
        self.mc.flush_all()
        print(f"Active memcached instances: {len(self.mc.get_stats())}")

    def get(self, key):
        start_time = time.time()  # Inicio del temporizador

        response = self.mc.get(key)
        
        if response != None:
            elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
            print(f"Time taken (cache): {1000*elapsed_time:.5f} miliseconds")
            return response
        else:
            # Simulamos un retraso aletorio de 1 a 3 segundos, con una distribución normal en 2
            start_time = time.time()
            print(f"Key not found in cache...")

            # Si no está en el caché, buscar en el JSON
            value = find_product_by_sku(int(key))
            value = str(value)
            if value:
                elapsed_time = time.time() - start_time
                print(f"Key found in JSON {1000*elapsed_time:.5f} miliseconds. Adding to cache...")
                
                # Agregando la llave-valor al caché
                self.mc.set(key, value)
                
                return value
            else:
                elapsed_time = time.time() - start_time  # Calcula el tiempo transcurrido
                print(f"Time taken: {1000*elapsed_time:.5f} miliseconds")
                print("Key not found.")
                return None
            
    def simulate_searches(self, n_searches):
        #Normal distribution
        keys_to_search = np.random.normal(50, 10, n_searches)
        keys_to_search = [int(round(num)) % 100000 for num in keys_to_search]

        # Métricas
        time_with_cache = 0
        avoided_json_lookups = 0

        count = 0
        for key in keys_to_search:
            # clear console
            count += 1
            print("\033[H\033[J")
            print(f"Searching : {count}/{n_searches}")
            start_time = time.time()
            self.get(str(key))
            elapsed_time = time.time() - start_time
            time_with_cache += elapsed_time

            if 1000*elapsed_time < 10:
                avoided_json_lookups += 1
                
        print(f"Number of times JSON lookup was avoided: {avoided_json_lookups}")
        print(f"Time with cache: {1000*time_with_cache}")
        

if __name__ == '__main__':

    client = CacheClient()

    while True:
        print("\nChoose an operation:")
        print("1. Get")
        print("2. Simulate Searches")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = client.get(key)
            if value is not None:
                print(f"Value: {value}")
        elif choice == "2":
            n_searches = int(input("Enter the number of searches you want to simulate: "))
            client.simulate_searches(n_searches)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")