from flask import Flask, request, jsonify # type: ignore
from models import users, tasks

app = Flask(__name__)

# Registro
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

    if users.get(email) == password:
        return jsonify({"message": "Login exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

# Crear tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    assigned_to = data.get("assigned_to")

    if not title:
        return jsonify({"error": "El título es obligatorio"}), 400

    task = {
        "title": title,
        "description": description,
        "assigned_to": assigned_to,
        "status": "pendiente"
    }
    tasks.append(task)
    return jsonify({"message": "Tarea creada"}), 201

# Ver todas las tareas
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks), 200

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)

