# coding=utf-8

from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Vamos cocriar novos significados para a educação e o trabalho para a humanidade... É um grande desafio e precisaremos muito de sua ajuda!"


if __name__ == "__main__":
    app.run()
