# coding=utf-8

from flask import Flask, render_template

app = Flask (__name__, static_folder='static/', static_url_path='')

@app.route('/')
def index():
    value_proposition = "Cocriar uma nova educação, um novo trabalho e novas relações humanas..."
    return render_template("index.html", vp = value_proposition).encode( "utf-8" )


if __name__ == "__main__":
    app.run()
