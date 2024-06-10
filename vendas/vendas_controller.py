from datetime import datetime

from flask_jwt_extended import jwt_required, get_jwt_identity
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from sqlalchemy import and_
from sqlalchemy.exc import SQLAlchemyError

from database.database import session
from database.models import Vendaschema, Venda, User
from flask import Flask, jsonify, request, Blueprint, send_file

vendas_controller = Blueprint('vendas_controller', __name__)


# get vendas /sales
@vendas_controller.route("/sales", methods=['GET'])
@jwt_required()
def get_vendas():
    vends = session.query(Vendaschema).all()
    #current_user = get_jwt_identity()
    #print(current_user)
    if not vends:
        return jsonify({"message": "Venda não encontrada"}), 404

    return jsonify(vends)


#post /sales : nome_cliente, produto, valor, data_venda
@vendas_controller.route("/sales", methods=['POST'])
@jwt_required()
def new_vendas():
    data = request.get_json()

    current_user = get_jwt_identity()

    user = session.query(User).filter_by(email=current_user).first()

    if user is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    nome_cliente = data.get('nome')
    produto = data.get('produto')
    valor = data.get('valor')
    data_venda = datetime.strptime(data['data'], "%Y-%m-%d")

    venda = Venda(nome_cliente, produto, valor, data_venda, user.id)
    session.add(venda)
    session.commit()

    return jsonify({"message": "venda criada com sucesso"}), 201


#put /sales/:id editar venda nome_cliente, produto, valor, data_venda
@vendas_controller.route("/sales/<id>", methods=['PUT'])
@jwt_required()
def edit_vendas(id):
    data = request.get_json()

    #Pega valores recebidos
    nome_cliente = data.get('nome')
    produto = data.get('produto')
    valor = data.get('valor')
    data_venda = data.get('data')

    #Pega venda a ser atualizada
    venda = session.query(Venda).filter_by(id=id).first()

    if venda is None:
        return jsonify({"error": "Venda não encontrada"}), 404

    #atualiza os campos
    if nome_cliente:
        venda.nome_cliente = nome_cliente
    if produto:
        venda.produto = produto
    if valor is not None:
        venda.valor = float(valor)
    if data_venda:
        venda.data_venda = datetime.strptime(data_venda, "%Y-%m-%d")

    session.commit()

    return jsonify({"message": "Venda atualizada com sucesso"}), 200


#delete sales/:id exlcuir uma venda
@vendas_controller.route("/sales/<id_venda>", methods=['DELETE'])
@jwt_required()
def delete_vendas(id_venda):
    try:
        venda = session.query(Venda).filter_by(id=id_venda).first()
        if venda is None:
            return jsonify({"error": "Venda não encontrada"}), 404

        session.delete(venda)
        session.commit()
        return jsonify({"message": "Venda excluída com sucesso"}), 200
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({"error": "Erro ao excluir a venda"}), 500


#Get /sales/pdf?start_date=dd-mm-yyyy&end_date=dd-mm-yyyy
@vendas_controller.route("/sales/pdf", methods=['GET'])
@jwt_required()
def get_pdf():
    # Obtém as datas passadas como parâmetros na URL
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    if not start_date_str or not end_date_str:
        return jsonify({'error': 'Uma data de inicio e fim são requisitadas'}), 400

    # Converte as strings de data para objetos datetime
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

    vendas = session.query(Venda).filter(and_(Venda.data_venda >= start_date, Venda.data_venda <= end_date)).all()

    if not vendas:
        return jsonify({"error": "Nenhuma venda foi encontrada nesse periodo"})

    pdf_filename = "sales_report.pdf"
    pdf_generator(vendas, pdf_filename)

    return send_file(pdf_filename, as_attachment=True, mimetype='application/pdf', download_name=pdf_filename)

# função para gerar pdf
def pdf_generator(vendas, name):
    pdf_filename = name
    pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
    # Conteúdo do relatório
    content = []

    # Adiciona título do relatório
    styles = getSampleStyleSheet()
    title = Paragraph("Relatório de Vendas", styles['Title'])
    content.append(title)
    content.append(Paragraph("\n", styles['Normal']))

    # Cabeçalho da tabela
    table_data = [["ID", "Cliente", "Produto", "Valor", "Data da Venda"]]
    # Adiciona dados das vendas à tabela
    for venda in vendas:
        table_data.append([
            venda.id,
            venda.nome_cliente,
            venda.produto,
            f"${venda.valor:.2f}",  # Formata o valor como moeda
            venda.data_venda.strftime('%d-%m-%Y')  # Formata a data da venda
        ])
    # Cria a tabela
    table = Table(table_data)
    # Aplica estilo à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)
    # Adiciona a tabela ao conteúdo do PDF
    content.append(table)
    # Constrói o PDF
    pdf.build(content)
