from flask import render_template


from server.instance import server
app = server.app


@app.route('/selecionar')
def selecionar():
    return render_template('selecionar.html')
