from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database.models import *

# Configura a conexão com o banco de dados
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Dados de vendas a serem inseridos
sales_data = [
    {"nome_cliente": "Cliente A", "produto": "Produto X", "valor": 99.99, "data_venda": datetime(2024, 1, 1, 10, 0), "user_id": 1},
    {"nome_cliente": "Cliente B", "produto": "Produto Y", "valor": 49.99, "data_venda": datetime(2024, 1, 2, 11, 0), "user_id": 1},
    {"nome_cliente": "Cliente C", "produto": "Produto Z", "valor": 19.99, "data_venda": datetime(2024, 1, 3, 12, 0), "user_id": 1},
    {"nome_cliente": "Cliente D", "produto": "Produto X", "valor": 89.99, "data_venda": datetime(2024, 1, 4, 13, 0), "user_id": 1},
    {"nome_cliente": "Cliente E", "produto": "Produto Y", "valor": 59.99, "data_venda": datetime(2024, 1, 5, 14, 0), "user_id": 1},
    {"nome_cliente": "Cliente F", "produto": "Produto Z", "valor": 29.99, "data_venda": datetime(2024, 1, 6, 15, 0), "user_id": 1},
    {"nome_cliente": "Cliente G", "produto": "Produto X", "valor": 79.99, "data_venda": datetime(2024, 1, 7, 16, 0), "user_id": 1},
    {"nome_cliente": "Cliente H", "produto": "Produto Y", "valor": 39.99, "data_venda": datetime(2024, 1, 8, 17, 0), "user_id": 1},
    {"nome_cliente": "Cliente I", "produto": "Produto Z", "valor": 9.99, "data_venda": datetime(2024, 1, 9, 18, 0), "user_id": 1},
    {"nome_cliente": "Cliente J", "produto": "Produto X", "valor": 99.99, "data_venda": datetime(2024, 1, 10, 19, 0), "user_id": 1},
    {"nome_cliente": "Cliente K", "produto": "Produto Y", "valor": 49.99, "data_venda": datetime(2024, 1, 11, 20, 0), "user_id": 1},
    {"nome_cliente": "Cliente L", "produto": "Produto Z", "valor": 19.99, "data_venda": datetime(2024, 1, 12, 21, 0), "user_id": 1},
    {"nome_cliente": "Cliente M", "produto": "Produto X", "valor": 89.99, "data_venda": datetime(2024, 1, 13, 22, 0), "user_id": 1},
    {"nome_cliente": "Cliente N", "produto": "Produto Y", "valor": 59.99, "data_venda": datetime(2024, 1, 14, 23, 0), "user_id": 1},
    {"nome_cliente": "Cliente O", "produto": "Produto Z", "valor": 29.99, "data_venda": datetime(2024, 1, 15, 9, 0), "user_id": 1},
    {"nome_cliente": "Cliente P", "produto": "Produto X", "valor": 79.99, "data_venda": datetime(2024, 1, 16, 10, 0), "user_id": 1},
    {"nome_cliente": "Cliente Q", "produto": "Produto Y", "valor": 39.99, "data_venda": datetime(2024, 1, 17, 11, 0), "user_id": 1},
    {"nome_cliente": "Cliente R", "produto": "Produto Z", "valor": 9.99, "data_venda": datetime(2024, 1, 18, 12, 0), "user_id": 1},
    {"nome_cliente": "Cliente S", "produto": "Produto X", "valor": 99.99, "data_venda": datetime(2024, 1, 19, 13, 0), "user_id": 1},
    {"nome_cliente": "Cliente T", "produto": "Produto Y", "valor": 49.99, "data_venda": datetime(2024, 1, 20, 14, 0), "user_id": 1}
]

# Insere os dados de vendas no banco de dados
for sale in sales_data:
    new_sale = Venda(**sale)
    session.add(new_sale)

# Confirma as transações
session.commit()
