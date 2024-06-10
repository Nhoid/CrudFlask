from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

from database.database import session
from database.models import User, Userschema
from config.config import Config
from vendas.vendas_controller import vendas_controller

app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

app.register_blueprint(vendas_controller, url_prefix='/v1')


@app.route('/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User(email, password)

    session.add(user)
    session.commit()

    user = session.query(User).filter_by(email=email).first()

    return jsonify({'id': user.id, 'email': user.email}), 201


@app.route('/auth/login', methods=['POST'])
def get_user():

    data = request.get_json()

    # recebe os dados passados
    user_email = data.get('email')
    user_password = data.get('password')

    #busca usuario
    user = session.query(User).filter_by(email=user_email).first()

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    if not user.check_password(user_password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    acess_token = create_access_token(identity=user_email)

    return jsonify({"token": acess_token}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
