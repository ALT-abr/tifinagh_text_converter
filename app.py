from flask import Flask, render_template, request
from converter import convert_to_tifinagh

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultat = ''

    if request.method == 'POST':
        message = request.form['message']
        resultat = convert_to_tifinagh(message)

    return render_template('index.html, resultat=resultat)')

if __name__ == '__main__':
    app.run(debug=True)
