from flask import Flask, render_template
import random
import os

app = Flask(__name__)

images = [
    #"pics/60686531259__A5076E2C-6694-4F69-9A74-5E01D82633CE.jpeg",
    #"pics/IMG_1810.JPG",
    "/static/PuppyPics/20200216_131728.jpg",
    "/static/PuppyPics/20200216_131827.jpg",
    "/static/PuppyPics/20200216_145117.jpg",
    "/static/PuppyPics/20200216_145123.jpg",
    "/static/PuppyPics/20200223_140228.jpg",
    "/static/PuppyPics/20200223_140228.jpg",
    "/static/PuppyPics/20200223_141849.jpg",
    "/static/PuppyPics/20200308_150050.jpg",
    "/static/PuppyPics/20200308_151055.jpg",
    "/static/PuppyPics/20200308_151349.jpg",
    "/static/PuppyPics/20200308_151350.jpg",
    "/static/PuppyPics/20200308_151353.jpg",
    "/static/PuppyPics/20200308_151658.jpg",
    "/static/PuppyPics/20200308_151702.jpg",
    "/static/PuppyPics/20200308_151704.jpg",
    "/static/PuppyPics/20200308_151740.jpg",
    "/static/PuppyPics/20200308_151752.jpg",
    "/static/PuppyPics/20200308_151753.jpg",
    "/static/PuppyPics/20200308_153409.jpg",
    "/static/PuppyPics/20200308_153416.jpg",
    "/static/PuppyPics/20200308_153616.jpg",
    "/static/PuppyPics/20200308_153646.jpg",
    "/static/PuppyPics/20200308_202328.jpg",
    "/static/PuppyPics/20200308_202330.jpg",
]


@app.route('/')
def index():
    dogURL = random.choice(images)
    # dogURL = "/static/PuppyPics/20200216_131728.jpg"
    return render_template("index.html", dogURL=dogURL)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)))