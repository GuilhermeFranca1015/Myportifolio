from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    button_python = None


    if request.method == "POST":

# Verificar qual botão de projeto foi clicado
        button_python = request.form.get("button_python")


    return render_template(
        "index.html",
        button_python=button_python,

)


if __name__ == "__main__":
    app.run(debug=True)
