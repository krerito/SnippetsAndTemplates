import os
from concurrent.futures import ThreadPoolExecutor

def obtener_tamaño(archivo):
    try:
        print(f"Procesando: {archivo}")  # Mostrar el archivo que se está procesando
        return os.path.getsize(archivo), archivo
    except Exception as e:
        print(f"Error procesando {archivo}: {e}")
        return None

def obtener_archivos_mas_pesados(ruta, top_n=10, num_workers=5):
    archivos = []
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        
        # Recorrer la carpeta y subcarpetas
        for raiz, dirs, files in os.walk(ruta):
            for nombre in files:
                archivo = os.path.join(raiz, nombre)
                futures.append(executor.submit(obtener_tamaño, archivo))
                
        for future in futures:
            resultado = future.result()
            if resultado:  # Añadir solo si obtener_tamaño fue exitoso
                tamaño, archivo = resultado
                archivos.append((tamaño, archivo))
    
    # Ordenar los archivos por tamaño de manera descendente
    archivos.sort(reverse=True)
    
    # Obtener los top_n archivos más pesados
    archivos_pesados = archivos[:top_n]
    
    return archivos_pesados

# Uso de la función con una ruta de carpeta de ejemplo
ruta_carpeta = "" #Cambiar por la direccion que analizaremos
archivos_pesados = obtener_archivos_mas_pesados(ruta_carpeta)
for tamaño, archivo in archivos_pesados:
    print(f"{archivo}: {tamaño/1024/1024:.2f} MB")
