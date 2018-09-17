from flask import Flask, render_template, jsonify, request

app = Flask(__name__,
            static_folder='../dist/static',
            template_folder='../dist')


@app.route('/comment')
def comment():
    if request.method == 'post':
        pass
    elif request.method == 'get':
        pass


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
