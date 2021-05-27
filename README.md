# Junior SW engineer task - SeeTree
Image statistics are common features in AI applications.
In the following assignment you are requested to implement a web server that handles calculation of image statistics. For example, given an image we would like to calculate the min,max,mean values etc.

## Common setup
Clone the repo and install the dependencies.
```bash
git clone https://github.com/ameenaboraya/seetree.git
```
## Usage - By Flask

open Command Prompt and go to the file location then tap 
```bash
py -m pip install -r requirements.txt
set FLASK_APP=seetree-ameen.py
flask run
```
Go over the [localhost](https://127.0.0.0:5000) with port 5000 because flask run with that port

## Usage - By Docker

open Command Prompt and go to the file location then tap
```bash
docker build -t seetree .
```
that's will build the docker image for you then tap
notice: a docker demon must be running before building the image
```bash
docker run -d -p 5000:5000 seetree
```
Go over the [localhost](https://127.0.0.0:5000)


## Work
This is the homepage , you are requested to choose a photo and a function:

<img width="1438" alt="Screen Shot 2021-05-28 at 0 56 54" src="https://user-images.githubusercontent.com/82150100/119903268-26414500-bf51-11eb-9f22-cbdb28177132.png">




/health : will respond with “OK” to any request
<img width="1438" alt="Screen Shot 2021-05-28 at 1 12 17" src="https://user-images.githubusercontent.com/82150100/119904915-d748df00-bf53-11eb-913b-7eb07a7737ba.png">



This is the result page:

/stats/IMAGE_FILE_NAME/FUNC_NAME : will show you the  FUNC_NAME on the
pixels of given IMAGE_FILE_NAME , We have five supported function:min, max , median , pX where 0<=X<=100

We have ten images ,they are stored in a bucket named :seetree-demo-open .
The server  respond correctly to requests on any image that exists in the bucket


Example for Request to /stats/IMG_9.jpg/min , respond with the correct min value in the
image
<img width="1438" alt="Screen Shot 2021-05-28 at 1 10 16" src="https://user-images.githubusercontent.com/82150100/119904512-30fcd980-bf53-11eb-8ca1-865c0f9bfaa8.png">


The server  respond with error code 404 if an image does not exist or the function is not supported
code 404 for image:
<img width="1438" alt="Screen Shot 2021-05-28 at 1 23 06" src="https://user-images.githubusercontent.com/82150100/119904777-918c1680-bf53-11eb-8328-4042cbe82406.png">


code 404 for function
<img width="1438" alt="Screen Shot 2021-05-28 at 1 25 45" src="https://user-images.githubusercontent.com/82150100/119904826-a8326d80-bf53-11eb-896d-ce8ae13c12f7.png">
