from flask import render_template


from server.instance import server
app = server.app


@app.route('/amendoim')
def amendoim():
    return render_template('amendoim.html')


@app.route('/mms')
def mms():
    return render_template('mms.html')
