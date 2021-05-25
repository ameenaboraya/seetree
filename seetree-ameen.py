from flask import Flask , render_template

app = Flask (__name__)

@app.route("/")

def homepage():
    return render_template("homepage.html", pagetitle=" Ameen Flask")#render m7zer lno html mbkom string..


@app.route("/page404")

def page404():
    return render_template("page404.html",pagetitle="404")#render m7zer lno html mbkom string..


@app.route("/page404image")

def page404image():
    return render_template("page404image.html",pagetitle="404")#render m7zer lno html mbkom string..


@app.route("/about")

def about():
    return render_template("about.html",pagetitle="about")#render m7zer lno html mbkom string..







if __name__=="__main__":

    app.run(debug=True, port=9000)