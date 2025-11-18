import unittest
import app

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()
        self.client.testing = True

    def test_registro_usuario_valido(self):
        response = self.client.post('/register', json={
            "email": "usuario@correo.com",
            "password": "seguro123"
        })
        self.assertEqual(response.status_code, 201)

    def test_registro_usuario_existente(self):
        self.client.post('/register', json={
            "email": "existente@correo.com",
            "password": "clave"
        })
        response = self.client.post('/register', json={
            "email": "existente@correo.com",
            "password": "clave"
        })
        self.assertEqual(response.status_code, 400)

    def test_login_correcto(self):
        self.client.post('/register', json={
            "email": "test@correo.com",
            "password": "pass123"
        })
        response = self.client.post('/login', json={
            "email": "test@correo.com",
            "password": "pass123"
        })
        self.assertEqual(response.status_code, 200)

    def test_crear_tarea_valida(self):
        response = self.client.post('/tasks', json={
            "title": "Tarea QA",
            "description": "Revisar pruebas",
            "assigned_to": "tester@correo.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_crear_tarea_sin_titulo(self):
        response = self.client.post('/tasks', json={
            "description": "Sin título",
            "assigned_to": "tester@correo.com"
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
