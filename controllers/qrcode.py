from flask import render_template, jsonify, make_response
from services.pix import PixService
#import controllers.motores as motores

from server.instance import server
app = server.app


@app.route('/qrcode')
def qrcode():
    quantidade = server.quantidadeProduto
    produto = server.produto
    qrcode = server.qrcode
    return render_template('qrcode.html', qrcode=qrcode, quantidade=quantidade, produto=produto)


@app.route('/validar')
def validar():
    pix_service = PixService()
    verificar_pagamento = pix_service.get_saldo()
    quantidade = server.quantidadeProduto
    produto = server.produto

    if verificar_pagamento != server.saldo:
        if produto == "Disquete":
            # motores.motor2(quantidade)
            response = make_response(
                jsonify(
                    {
                        "message": "Simple server is running",
                        "severity": "danger"}
                ),
                200,
            )
            return response
        elif produto == "Chiquete":
            # motores.motor1(quantidade)
            response = make_response(
                jsonify(
                    {
                        "message": "Simple server is running",
                        "severity": "danger"}
                ),
                200,
            )
            return response

    response = make_response(
        jsonify(
            {
                "message": "Simple server is running",
                "severity": "danger"}
        ),
        401,

    )

    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
