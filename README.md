# Sistema de Gestión de Tareas (Simulado)

Este proyecto simula un sistema básico de gestión de tareas con funcionalidades de:
- Registro e inicio de sesión de usuarios
- Creación y listado de tareas
- Pruebas automatizadas con unittest

## Requisitos
- Python 3.8+
- Flask

## Cómo ejecutar
1. Instalar dependencias:
   pip install -r requirements.txt

2. Iniciar el servidor:
   python app.py

3. Ejecutar pruebas:
   python test_app.py

## Flujo del sistema completo

El usuario se registra con su email y contraseña
➤ Se guarda en el diccionario users

El usuario inicia sesión
➤ Se valida que exista y que la contraseña sea correcta

El usuario crea tareas
➤ Se envía título, descripción y a quién está asignada
➤ Se guarda en la lista tasks

El usuario puede consultar las tareas
➤ Se devuelve la lista como respuesta JSON