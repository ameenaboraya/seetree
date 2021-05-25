from flask import Flask , render_template

app = Flask (__name__)

@app.route("/")

def homepage():
    return render_template("homepage.html", pagetitle="Homepage")#render m7zer lno html mbkom string..#pagetitle 3shan albase


@app.route("/about")

def about():
    return render_template("about.html",pagetitle="About")#render m7zer lno html mbkom string..


if __name__=="__main__":

    app.run(debug=True, port=9000)