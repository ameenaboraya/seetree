from flask import Flask , render_template
from PIL import Image , ImageStat
import  urllib.request
import numpy as np



app = Flask (__name__)

@app.route("/", methods=['GET'])

def homepage():
    return render_template("homepage.html")#render m7zer lno html mbkom string..



@app.route('/health',methods=['GET'])
def starting_url():
    # status_code = Response(status=200)
    return render_template("health.html"),200







#the route where all the work are done
@app.route('/stats/<IMAGE_FILE_NAME>/<FUNC_NAME>',methods=['GET'])
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
        if FUNC_NAME[0] != 'p' or not FUNC_NAME[1:].isnumeric() or int(FUNC_NAME[1:]) < 0 or int(FUNC_NAME[1:]) > 100:
            return render_template("page404.html"), 404


    if(FUNC_NAME=='min'):
        minimum= [x[0] for x in stat.extrema]
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=minimum, text=' Min values for each band in the image is')
    if (FUNC_NAME == 'max'):
        maximum = [x[1] for x in stat.extrema]
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=maximum, text=' Max values for each band in the image is')
    if (FUNC_NAME=='mean'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.mean, text=' Mean values for each band in the image is')
    if (FUNC_NAME == 'median'):
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=stat.median, text=' median values for each band in the image is')
    if FUNC_NAME[0] == 'p' and FUNC_NAME[1:].isnumeric() and int(FUNC_NAME[1:]) >= 0 and int(FUNC_NAME[1:]) <= 100:
        pixels = list(img.getdata())
        percentile= np.percentile(pixels, int(FUNC_NAME[1:]))
        return render_template("showresults.html", IMG_NAME=IMAGE_FILE_NAME, value=percentile,text= FUNC_NAME+' value  in the image is')

if __name__=="__main__":

    app.run(debug=True,host="0.0.0.0", port=5000)
