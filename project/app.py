from flask import Flask

# o nome 'app' é padrão
# __name__ = "__main__" -> quando for criada de forma manual
app = Flask(__name__)

# criando uma roda 
# retorna uma string com formado http
@app.route("/")
def hello_word():
    return "Hello Word" # texto estático

@app.route("/about")
def about():
    return "Página sobre"

# usamos dessa forma apenas para servidores locais
if __name__ == "__main__":
    app.run(debug=True) # mostra os Log para mostrar como está funcionando a rota 
