import unittest
from database.models import User

from app import app, session


class TestAuth(unittest.TestCase):
    def setUp(self):
        # Configuração do Flask para usar o arquivo de configuração de teste
        app.config.from_pyfile('config/config.ini')
        app.testing = True
        self.app = app.test_client()

    def test_register_user(self):
        # Dados de exemplo para o registro de usuário
        data = {
            "email": "test@example.com",
            "password": "password123"
        }

        # Faz a solicitação POST para o endpoint de registro de usuário
        response = self.app.post('/auth/register', json=data)

        # Verifica se o status da resposta é 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Verifica se o usuário foi adicionado ao banco de dados corretamente
        user = session.query(User).filter_by(email=data['email']).first()
        self.assertIsNotNone(user)

        session.delete(user)
        session.commit()

    def test_get_user(self):
        # Dados de exemplo para o login de usuário
        data = {
            "email": "test@example.com",
            "password": "password123"
        }

        # Adiciona um usuário de exemplo ao banco de dados
        user = User(email=data['email'], password=data['password'])
        session.add(user)
        session.commit()

        # Faz a solicitação POST para o endpoint de login de usuário
        response = self.app.post('/auth/login', json=data)

        # Verifica se o status da resposta é 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica se o token de acesso foi retornado na resposta
        json_data = response.get_json()
        self.assertIn('token', json_data)

        session.delete(user)
        session.commit()

if __name__ == '__main__':
    unittest.main()
