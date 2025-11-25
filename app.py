from flask import Flask, request, jsonify  # type: ignore
from models import users, tasks

app = Flask(__name__)

# Registro de usuarios
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Datos incompletos"}), 400

    if email in users:
        return jsonify({"error": "Usuario ya registrado"}), 400

    users[email] = password
    return jsonify({"message": "Usuario registrado"}), 201

# Inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if email not in users:
        return jsonify({"error": "Usuario no registrado"}), 404

    if users[email] != password:
        return jsonify({"error": "Contraseña incorrecta"}), 401

    return jsonify({"message": "Login exitoso"}), 200

# Crear tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    # Si es una sola tarea (dict), lo convertimos en lista para tratarlo igual
    if isinstance(data, dict):
        data = [data]

    created = []

    for item in data:
        title = item.get("title")
        description = item.get("description")
        assigned_to = item.get("assigned_to")

        if not title:
            return jsonify({"error": "El título es obligatorio en una o más tareas"}), 400

        task = {
            "title": title,
            "description": description,
            "assigned_to": assigned_to,
            "status": "pendiente"
        }
        tasks.append(task)
        created.append(task)

    return jsonify({"message": f"{len(created)} tareas creadas", "tareas": created}), 201


# Obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
