from gpiozero import Motor
from time import sleep
from flask import render_template, jsonify, make_response
from services.pix import PixService


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
        if produto == "Amendoim":
            produto1(quantidade)
            response = make_response(
                jsonify(
                    {
                        "message": "Simple server is running",
                        "severity": "danger"}
                ),
                200,
            )
            return response
        elif produto == "Jelly":
            produto2(quantidade)
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


def produto1(tempo):
    motor = Motor(17, 27)
    motor.forward(0.6)
    sleep(tempo*0.5)
    motor.stop()


def produto2(tempo):
    motor = Motor(22, 23)
    motor.backward(0.6)
    sleep(tempo*0.5)
    motor.stop()
