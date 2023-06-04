from flask import Flask, render_template, request

from functions import get_entities

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    results = []
    num_of_results = 0
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']

        values = get_entities(choice, rawtext)
        results = values[0]
        num_of_results = values[1]

    return render_template("index.html", results=results, num_of_results=num_of_results)


if __name__ == '__main__':
    app.run(debug=True)