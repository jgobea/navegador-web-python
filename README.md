# Navegador Web en Python

Un simulador de navegador web en consola implementado en Python.

## Características

- Historial de navegación (usando Pilas)
- Gestión de pestañas (usando Lista Doblemente Enlazada)
- Sistema de descargas (usando Colas)
- Visualización de páginas HTML

## Comandos Disponibles

### Historial de Navegación
- `ir <url o ip>`: Visitar una página
- `atras`: Volver a la página anterior
- `adelante`: Avanzar a la página siguiente
- `mostrar_historial`: Mostrar todas las páginas visitadas

### Gestión de Pestañas
- `nueva_pestana <url>`: Abrir una nueva pestaña
- `cerrar_pestana`: Cerrar la pestaña actual
- `cambiar_pestana <n>`: Cambiar a la pestaña número n
- `mostrar_pestanas`: Mostrar todas las pestañas abiertas

### Gestión de Descargas
- `descargar <url>`: Iniciar la descarga de un archivo
- `mostrar_descargas`: Mostrar el estado de la cola de descargas
- `cancelar_descarga <n>`: Cancelar la descarga número n

### Visualización de Páginas
- `listar_paginas`: Mostrar todas las páginas HTML disponibles
- `mostrar_contenido <url> <modo>`: Mostrar el contenido de una página
