from flask import render_template

from server.instance import server
app = server.app


@app.route('/qrcode')
def qrcode():
    quantidade = server.quantidadeProduto
    produto = server.produto
    qrcode = server.qrcode
   # entregarProduto()
    return render_template('qrcode.html', qrcode=qrcode, quantidade=quantidade, produto=produto)
