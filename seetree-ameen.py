from flask import Flask , render_template
from PIL import Image , ImageStat
import  urllib.request

app = Flask (__name__)

@app.route("/")

def homepage():
    return render_template("homepage.html", pagetitle=" Ameen Flask")#render m7zer lno html mbkom string..



@app.route('/health')
def starting_url():
    # status_code = Response(status=200)
    return render_template("health.html"),200



@app.route("/page404")

def page404():
    return render_template("page404.html",pagetitle="404")#render m7zer lno html mbkom string..


@app.route("/page404image")

def page404image():
    return render_template("page404image.html",pagetitle="404")#render m7zer lno html mbkom string..



#the route where all the work are done
@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>')
def starting_work(IMAGE_FILE_NAME,FUNC_NAME):
    # get the picture
    url = "https://storage.googleapis.com/seetree-demo-open/{}".format(IMAGE_FILE_NAME)

    # try to open it if it exist or had open permission
    try:
        urllib.request.urlretrieve(url, "local-filename.jpg")
    except Exception:
        return render_template("page404image.html"), 404

    # save the img localy
    img = Image.open("local-filename.jpg")



    stat = ImageStat.Stat(img)
    if(not (FUNC_NAME=='min' or FUNC_NAME=='max' or FUNC_NAME=='mean' or FUNC_NAME=='median')):
        return render_template("page404.html"), 404

    if(FUNC_NAME=='min'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.extrema, text=' Min values for each band in the image is')
    if (FUNC_NAME == 'max'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.extrema, text=' Max values for each band in the image is')
    if (FUNC_NAME=='mean'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.mean, text=' Mean values for each band in the image is')
    if (FUNC_NAME == 'median'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.median, text=' median values for each band in the image is')











if __name__=="__main__":

    app.run(debug=True, port=5000)