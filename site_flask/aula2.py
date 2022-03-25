from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    variavel = "adivinhe o numero correto"

    if request.method == "GET":
        return render_template("a2_index.html", variavel=variavel)
    else:
        numero = random.randint(1,5)
        palpite = request.form.get(numero)

        if numero == palpite:
            return '<h1> vc acertou <h1>'
        else:
            return '<h1> vc errou <h1>'   

if(__name__ == "__main__"):
    app.run()