from flask import render_template


from server.instance import server
app = server.app


@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html')
