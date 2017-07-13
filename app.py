# coding=utf-8

from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Cocriar novos significados para a educação e para o trabalho na humanidade... É um grande desafio e precisaremos muito de sua ajuda!"


if __name__ == "__main__":
    app.run()
