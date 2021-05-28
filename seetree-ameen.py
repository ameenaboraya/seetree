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





img_dict={}
img_dict['IMG_1.jpg'] = {}
img_dict['IMG_2.jpg'] = {}
img_dict['IMG_3.jpg'] = {}
img_dict['IMG_4.jpg'] = {}
img_dict['IMG_5.jpg'] = {}
img_dict['IMG_6.jpg'] = {}
img_dict['IMG_7.jpg'] = {}
img_dict['IMG_8.jpg'] = {}
img_dict['IMG_9.jpg'] = {}
img_dict['IMG_10.jpg'] = {}

@app.route('/stats/<IMAGE_NUM>/<FUNC_NAME>',methods=['GET'])
def showresults(IMAGE_NUM,FUNC_NAME):

    # get the picture
    url = "https://storage.googleapis.com/seetree-demo-open/{}".format(IMAGE_NUM)

    try:
        urllib.request.urlretrieve(url,"imagenum.jpg")#the urllib. request module is used to open or download a file over HTTP
    except Exception:
        return render_template("page404image.html"), 404

    # save the image

    img = Image.open("imagenum.jpg")



    stat = ImageStat.Stat(img)
    if(not (FUNC_NAME=='min' or FUNC_NAME=='max' or FUNC_NAME=='mean' or FUNC_NAME=='median')):
        if FUNC_NAME[0] != 'p' or not FUNC_NAME[1:].isnumeric() or int(FUNC_NAME[1:]) < 0 or int(FUNC_NAME[1:]) > 100:
            return render_template("page404.html"), 404




    if(FUNC_NAME=='min'):
        if IMAGE_NUM in img_dict:
            if FUNC_NAME in img_dict[IMAGE_NUM]:
                minimum = img_dict[IMAGE_NUM][FUNC_NAME]
                return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=minimum,text=' Min values for each band in the image is')


        minimum= [x[0] for x in stat.extrema]
        img_dict[IMAGE_NUM][FUNC_NAME] = minimum

        return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=minimum, text=' Min values for each band in the image is')





    if (FUNC_NAME == 'max'):
        if IMAGE_NUM in img_dict:
            if FUNC_NAME in img_dict[IMAGE_NUM]:
                maximum = img_dict[IMAGE_NUM][FUNC_NAME]

                return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=maximum,
                                       text=' Max values for each band in the image is')
        maximum = [x[1] for x in stat.extrema]
        img_dict[IMAGE_NUM][FUNC_NAME] = maximum


        return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=maximum, text=' Max values for each band in the image is')




    if (FUNC_NAME=='mean'):
        if IMAGE_NUM in img_dict:
            if FUNC_NAME in img_dict[IMAGE_NUM]:
                mean = img_dict[IMAGE_NUM][FUNC_NAME]

                return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=mean,
                                       text=' Mean values for each band in the image is')


        mean=stat.mean
        img_dict[IMAGE_NUM][FUNC_NAME] = mean
        return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=mean, text=' Mean values for each band in the image is')




    if (FUNC_NAME == 'median'):
        if IMAGE_NUM in img_dict:
            if FUNC_NAME in img_dict[IMAGE_NUM]:
                median = img_dict[IMAGE_NUM][FUNC_NAME]
                return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=median, text=' median values for each band in the image is')



        median=stat.median
        img_dict[IMAGE_NUM][FUNC_NAME] = median
        return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=median, text=' median values for each band in the image is')





    if FUNC_NAME[0] == 'p' and FUNC_NAME[1:].isnumeric() and int(FUNC_NAME[1:]) >= 0 and int(FUNC_NAME[1:]) <= 100:
        if IMAGE_NUM in img_dict:
            if FUNC_NAME in img_dict[IMAGE_NUM]:
                percentile = img_dict[IMAGE_NUM][FUNC_NAME]

                return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=percentile,
                                       text=FUNC_NAME + ' value  in the image is')

        pixels = list(img.getdata())
        percentile= np.percentile(pixels, int(FUNC_NAME[1:]))

        img_dict[IMAGE_NUM][FUNC_NAME]=percentile
        return render_template("showresults.html", IMG_NAME=IMAGE_NUM, value=percentile,text= FUNC_NAME+' value  in the image is')





if __name__=="__main__":

    app.run(debug=True,host="0.0.0.0", port=5000)