from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Para conectar os pontos entre o futuro da humanidade, a educação no presente e as práticas do passado. Em breve..."


if __name__ == "__main__":
    app.run()
