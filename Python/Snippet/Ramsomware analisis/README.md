
# Forensic File Size Analyzer

## Description

This Python script performs a basic forensic analysis to identify the largest files in a directory and its subdirectories. It is particularly useful for finding files that may have been altered in size due to ransomware encryption, such as \`.pst\` files used by Microsoft Outlook.

## Features

- **Concurrent File Processing**: Leverages multi-threading to speed up the file size retrieval process.
- **Top N File Listing**: Can customize the number of top heavy files to retrieve.
- **Error Handling**: Gracefully handles and logs errors without stopping the analysis.

## Functions

### `obtener_tamaño(archivo)`
```python
def obtener_tamaño(archivo):
    try:
        print(f"Procesando: {archivo}")  # Mostrar el archivo que se está procesando
        return os.path.getsize(archivo), archivo
    except Exception as e:
        print(f"Error procesando {archivo}: {e}")
        return None
```
Retrieves the size of a specified file and handles exceptions.

### `obtener_archivos_mas_pesados(ruta, top_n=10, num_workers=5)`
```python
def obtener_archivos_mas_pesados(ruta, top_n=10, num_workers=5):
    # ... (rest of the function)
```
Finds and sorts the heaviest files in a given directory.

## Usage

Replace the `ruta_carpeta` variable with the path of the directory to analyze. Run the script, and it will print out the largest files in descending order by size.

```python
ruta_carpeta = "/path/to/directory"  # Replace with the actual path
archivos_pesados = obtener_archivos_mas_pesados(ruta_carpeta)
for tamaño, archivo in archivos_pesados:
    print(f"{archivo}: {tamaño/1024/1024:.2f} MB")
```

## Contributing

Suggestions and contributions are always welcome. This is a Forensic File Size Analyzer , if you have any other template that may help people in this topic, please contact me  to create the push or, create a better system for help people with this.
