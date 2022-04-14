from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def blog():
    return "Hello, from App!"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    res = [f'<b>You want path:</b> {request.method} {request.url_root} {request.full_path}<br><br>']
    res.append("<b>Headers</b>")
    for k,v in request.headers.items(): 
        res.append(f'{k:>30} : {v}')
    return '<br>'.join(res)


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)
