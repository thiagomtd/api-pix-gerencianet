from crypt import methods
from time import sleep
from flask import render_template
from flask import request
from gpiozero import Motor
from time import sleep

from server.instance import server
app = server.app


@app.route('/qrcode')
def qrcode():
    quantidade = request.args.get("quantidade")
    produto = request.args.get("produto")
    qrcode = server.aqui
    return render_template('qrcode.html', qrcode=qrcode, quantidade=quantidade, produto=produto)


def entregarProduto(produto, quantidade):
    amendoim = Motor(17, 27)
    jelly = Motor(22, 23)

    if produto == "Amendoim":
        amendoim.forward()
        sleep(quantidade*5)
        amendoim.stop()
    if produto == "Jelly":
        jelly.forward()
        sleep(quantidade*5)
        jelly.stop()

    return render_template('selecionar.html')
