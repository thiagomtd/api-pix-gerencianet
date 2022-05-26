from flask import render_template

from server.instance import server
app = server.app


@app.route('/produto1')
def produto1():
    return render_template('produto1.html')


@app.route('/produto2')
def produto2():
    return render_template('produto2.html')
