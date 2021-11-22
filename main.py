from flask import Flask, render_template

app = Flask(__name__)
# route -> deliciasgeladas.com/contatos
# função -> o que você quer exibir naquela página
#template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/sabores/<sabor_balas>")
def sabores(sabor_balas):
    return render_template("sabores.html", sabor_balas=sabor_balas)

# colocar o site no ar
if __name__== "__main__":
     app.run(debug=True)

     #servidor do heroku





