# coding=utf-8

from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Vamos construir uma ponte entre o significado da educação e significado do trabalho para a humanidade do futuro... É um grande desafio e precisaremos de sua ajuda."


if __name__ == "__main__":
    app.run()
