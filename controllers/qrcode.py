from crypt import methods
from flask import render_template
from flask import request

from server.instance import server
app = server.app


@app.route('/qrcode')
def qrcode():
    quantidade = request.args.get("quantidade")
    produto = request.args.get("produto")
    qrcode = server.aqui
    return render_template('qrcode.html', qrcode=qrcode, quantidade=quantidade, produto=produto)
